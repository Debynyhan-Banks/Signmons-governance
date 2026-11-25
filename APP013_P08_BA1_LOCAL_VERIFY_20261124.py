"""Finite BA1 synthetic verification; no provider or credential operations."""
import copy
import datetime
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import signal
import sqlite3
import subprocess
import sys
import tempfile
import time
import unittest
import urllib.request
import uuid
from unittest.mock import patch

COMMAND = Path(__file__).with_name('APP013_P08_BA1_READ_COMMAND_20261124.py')
spec = importlib.util.spec_from_file_location('ba1_command', COMMAND)
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
PRIVATE = 'BA1_PRIVATE_SENTINEL_DO_NOT_RETAIN'
ACCOUNT = 'billingAccounts/ABCDEF-123456-A1B2C3'
CONFIG = 'a' * 64
REAL_POPEN = subprocess.Popen


def wire(value):
    return json.dumps(value, separators=(',', ':')).encode()


class Clock:
    now = 1795572000.0
    def __call__(self):
        return self.now


def scope(now):
    def stamp(offset):
        return datetime.datetime.fromtimestamp(now + offset, datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    return {'version': 1, 'action': b.ACTION, 'operationId': str(uuid.uuid4()), 'sourceCommit': b.SOURCE,
            'manifestSha256': b.MANIFEST, 'commandSha256': b.m.digest(COMMAND.read_bytes()),
            'configSha256': CONFIG, 'billingAccountSha256': b.ACCOUNT_SHA256,
            'commands': json.loads(json.dumps(b.commands())), 'limits': dict(b.LIMITS),
            'sdkException': b.v.SDK_EXCEPTION, 'allowanceUsd': 0, 'automaticRetryAllowed': False,
            'window': {key: stamp(offset) for key, offset in
                       (('start', -1), ('cutoff', 60), ('readEnd', 180), ('closeoutEnd', 310))}}


class FakeIO:
    def __init__(self):
        self.values = [[{'account': b.m.OWNER, 'status': 'ACTIVE'}],
                       {'projectId': 'signmons', 'billingEnabled': True, 'billingAccountName': ACCOUNT}, {'open': True}]
        self.calls, self.close_calls, self.absence_calls = [], [], []
        self.observed = set()
        self.closed = False
        self.close_value = self.absence_value = True
        self.call_hook = None

    def _owned_run(self, argv, env, deadline):
        self.calls.append((argv, env, deadline))
        self.observed.add(object())
        if self.call_hook:
            self.call_hook(len(self.calls))
        value = self.values[len(self.calls) - 1]
        if isinstance(value, BaseException):
            raise value
        return value if isinstance(value, bytes) else wire(value)

    def close(self, deadline):
        self.close_calls.append(deadline)
        self.closed = True
        if isinstance(self.close_value, BaseException):
            raise self.close_value
        return self.close_value

    def verify_absent(self, deadline):
        self.absence_calls.append(deadline)
        if isinstance(self.absence_value, BaseException):
            raise self.absence_value
        return self.absence_value


class Hooks:
    def __init__(self, clock):
        self.clock, self.io = clock, FakeIO()
        self.factory_calls = self.guard_calls = self.config_calls = 0
        self.guard_hook = self.config_hook = None

    def io_factory(self):
        self.factory_calls += 1
        return self.io

    def guard(self, candidate):
        self.guard_calls += 1
        if self.guard_hook:
            self.guard_hook(candidate, self.guard_calls)

    def configuration(self):
        self.config_calls += 1
        return self.config_hook(self.config_calls) if self.config_hook else CONFIG


class BA1Tests(unittest.TestCase):
    def setUp(self):
        self.clock = Clock()
        self.tmp = tempfile.TemporaryDirectory(prefix='ba1-synthetic-', dir='/private/tmp')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'operation'
        for item in (patch.object(b, 'ACCOUNT_SHA256', hashlib.sha256(ACCOUNT.encode()).hexdigest()),
                     patch.dict(os.environ, {'HOME': '/Users/debynyhanbanks'}, clear=True),
                     patch.object(subprocess, 'Popen', side_effect=AssertionError('unexpected native process')),
                     patch.object(sqlite3, 'connect', side_effect=AssertionError('credential access forbidden')),
                     patch.object(urllib.request, 'urlopen', side_effect=AssertionError('network forbidden')),
                     patch.object(urllib.request, 'build_opener', side_effect=AssertionError('network forbidden'))):
            item.start()
            self.addCleanup(item.stop)
        self.scope = scope(self.clock())
        self.hooks = Hooks(self.clock)

    def fresh(self):
        self.root = Path(self.tmp.name) / str(uuid.uuid4())
        self.hooks = Hooks(self.clock)

    def assert_private_absent(self, value):
        text = json.dumps(value, sort_keys=True)
        for private in (PRIVATE, ACCOUNT, ACCOUNT.split('/')[-1], b.m.OWNER):
            self.assertNotIn(private, text)

    def run_one(self):
        result = b.run(self.scope, hooks=self.hooks, root=self.root)
        self.assert_private_absent(result)
        for path in self.root.iterdir():
            self.assert_private_absent(json.loads(path.read_bytes()))
        self.assertLessEqual(len(self.hooks.io.calls), 3)
        self.assertEqual(len(self.hooks.io.close_calls), 1)
        self.assertEqual(len(self.hooks.io.absence_calls), 1)
        return result

    def readback(self, result, exit_code=None):
        if exit_code is None:
            exit_code = 0 if result['status'] == 'BA1_ACCOUNT_STATUS_OBSERVED' else 2
        return b.readback(self.scope, result['resultSha256'], main_exit=exit_code, root=self.root)

    def test_open_and_enabled_true_false_exact_three_reads_and_safe_readback(self):
        for enabled in (True, False):
            for opened in (True, False):
                self.fresh()
                self.hooks.io.values[1]['billingEnabled'] = enabled
                self.hooks.io.values[2]['open'] = opened
                result = self.run_one()
                self.assertEqual(result['status'], 'BA1_ACCOUNT_STATUS_OBSERVED')
                self.assertIs(result['accountOpen'], opened)
                self.assertIs(result['billingEnabled'], enabled)
                self.assertEqual(result['counts'], {'cli': 3, 'cache': 0, 'https': 0, 'sql': 0})
                self.assertEqual([row[0] for row in self.hooks.io.calls], [d['argv'] for d in b.commands(ACCOUNT)])
                self.assertEqual(self.hooks.io.calls[2][0][4], ACCOUNT)
                self.assertEqual(result['startedCli'], result['observedProcesses'])
                for _, env, end in self.hooks.io.calls:
                    self.assertEqual(env, b.q.sdk_environment(os.environ))
                    self.assertEqual(end, self.clock() + 30)
                self.assertTrue(all(result['closeout'].values()))
                self.assertEqual(self.readback(result), result)

    def test_wrong_owner_project_account_and_full_reference_hash_stop_before_next_read(self):
        for stage, value, expected_calls in (
                (0, [{'account': PRIVATE, 'status': 'ACTIVE'}], 1),
                (1, {'projectId': PRIVATE, 'billingEnabled': True, 'billingAccountName': ACCOUNT}, 2),
                (1, {'projectId': 'signmons', 'billingEnabled': True,
                     'billingAccountName': 'billingAccounts/AAAAAA-BBBBBB-CCCCCC'}, 2),
                (1, {'projectId': 'signmons', 'billingEnabled': True, 'billingAccountName': ACCOUNT.split('/')[-1]}, 2)):
            self.fresh()
            self.hooks.io.values[stage] = value
            result = self.run_one()
            self.assertEqual(result['status'], 'UNKNOWN')
            self.assertEqual(len(self.hooks.io.calls), expected_calls)
            self.assertEqual(self.readback(result), result)

    def test_missing_null_wrong_types_and_extra_fields_never_mean_closed_account(self):
        for value in ({}, {'open': None}, {'open': 'false'}, {'open': 0}, {'open': 1}, {'open': 0.0},
                      {'open': False, 'name': PRIVATE}, [], None):
            self.fresh()
            self.hooks.io.values[2] = value
            result = self.run_one()
            self.assertEqual(result['failure'], 'BA1_OUTPUT')
            self.assertIsNone(result['accountOpen'])
            self.assertEqual(self.readback(result), result)
        for value in ({'projectId': 'signmons', 'billingAccountName': ACCOUNT},
                      {'projectId': 'signmons', 'billingAccountName': ACCOUNT, 'billingEnabled': None},
                      {'projectId': 'signmons', 'billingAccountName': ACCOUNT, 'billingEnabled': 1}):
            self.fresh()
            self.hooks.io.values[1] = value
            result = self.run_one()
            self.assertEqual(result['failure'], 'BA1_PROJECT')
            self.assertEqual(len(self.hooks.io.calls), 2)

    def test_malformed_json_and_generic_failure_are_bounded_and_private(self):
        for value in (b'{"open":true,"open":false}', b'{"open":NaN}', b'not json', b'\xff',
                      b'x' * 65537, OSError(PRIVATE), b.m.Stop('PROCESS_REFUSED'), b.m.Stop('PROCESS_TIMEOUT')):
            self.fresh()
            self.hooks.io.values[2] = value
            result = self.run_one()
            self.assertEqual(result['status'], 'UNKNOWN')
            self.assertEqual(len(self.hooks.io.calls), 3)
            self.assertIsNone(result['accountOpen'])

    def test_replay_and_foreign_root_refuse_before_process(self):
        result = self.run_one()
        count = len(self.hooks.io.calls)
        with self.assertRaisesRegex(b.Stop, 'BA1_REPLAY'):
            b.run(self.scope, hooks=self.hooks, root=self.root)
        self.assertEqual(len(self.hooks.io.calls), count)
        self.assertEqual(self.readback(result), result)
        link = Path(self.tmp.name) / 'foreign'
        link.symlink_to(self.root, target_is_directory=True)
        with self.assertRaisesRegex(b.Stop, 'BA1_REPLAY'):
            b.run(self.scope, hooks=self.hooks, root=link)

    def test_source_config_and_deadline_stop_before_next_dispatch(self):
        for failure in ('source', 'config', 'clock', 'deadline'):
            self.fresh()
            def after_call(_):
                if failure == 'source':
                    self.hooks.guard_hook = lambda *_: (_ for _ in ()).throw(b.Stop('BA1_SOURCE'))
                elif failure == 'config':
                    self.hooks.config_hook = lambda _: 'b' * 64
                else:
                    self.clock.now += -2 if failure == 'clock' else 180
            self.hooks.io.call_hook = after_call
            result = self.run_one()
            self.assertEqual(result['status'], 'UNKNOWN')
            self.assertEqual(len(self.hooks.io.calls), 1)
            self.clock.now = Clock.now

    def test_expired_window_bad_scope_and_unsafe_environment_refuse_before_root(self):
        for field, value in (('action', PRIVATE), ('sourceCommit', 'b' * 40), ('limits', {**b.LIMITS, 'cli': 4}),
                             ('automaticRetryAllowed', True), ('allowanceUsd', True), ('billingAccountSha256', 'f' * 64)):
            candidate = {**self.scope, field: value}
            with self.assertRaises(Exception):
                b.run(candidate, hooks=self.hooks, root=self.root)
        self.clock.now += 60
        with self.assertRaisesRegex(b.Stop, 'BA1_CUTOFF'):
            b.run(self.scope, hooks=self.hooks, root=self.root)
        self.clock.now -= 60
        with patch.dict(os.environ, {'HTTPS_PROXY': PRIVATE}), self.assertRaises(Exception):
            b.run(self.scope, hooks=self.hooks, root=self.root)
        self.assertFalse(self.root.exists())
        self.assertEqual(self.hooks.factory_calls, 0)

    def test_insufficient_read_or_closeout_reserve_refuses(self):
        for field, offset in (('readEnd', 100), ('closeoutEnd', 299)):
            candidate = copy.deepcopy(self.scope)
            candidate['window'][field] = datetime.datetime.fromtimestamp(self.clock() + offset,
                                                                        datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
            with self.assertRaisesRegex(b.Stop, 'BA1_WINDOW'):
                b.run(candidate, hooks=self.hooks, root=self.root)
        self.assertFalse(self.root.exists())

    def test_cleanup_absence_and_missing_handle_history_never_claim_observed(self):
        for name, value in (('close_value', False), ('close_value', OSError(PRIVATE)),
                            ('absence_value', False), ('absence_value', OSError(PRIVATE)), ('history', None)):
            self.fresh()
            if name == 'history':
                self.hooks.io.call_hook = lambda _: self.hooks.io.observed.clear()
            else:
                setattr(self.hooks.io, name, value)
            result = self.run_one()
            self.assertEqual(result['status'], 'UNKNOWN')
            self.assertEqual(result['residuals'], ['LOCAL_CLOSEOUT_UNCONFIRMED'])
            self.assertEqual(self.readback(result), result)

    def test_pending_signal_at_final_environment_step_prevents_dispatch(self):
        original = b.q.sdk_environment
        calls = 0
        def env(value):
            nonlocal calls
            calls += 1
            if calls == 4:
                signal.getsignal(signal.SIGTERM)(signal.SIGTERM, None)
            return original(value)
        with patch.object(b.q, 'sdk_environment', side_effect=env):
            result = self.run_one()
        self.assertEqual(result['counts']['cli'], 1)
        self.assertEqual(result['startedCli'], 0)
        self.assertEqual(self.hooks.io.calls, [])
        self.assertEqual(result['failure'], 'VM2_INTERRUPTED')
        self.assertTrue((self.root / 'interruption.json').exists())
        self.assertEqual(self.readback(result), result)

    def test_signal_after_read_and_during_result_publication_is_durable(self):
        original = b.v.Journal.put
        for point in ('after-read', 'result.json'):
            self.fresh()
            def after_call(count):
                if point == 'after-read' and count == 3:
                    signal.getsignal(signal.SIGTERM)(signal.SIGTERM, None)
            def put(journal, name, value):
                original(journal, name, value)
                if point == name:
                    signal.getsignal(signal.SIGTERM)(signal.SIGTERM, None)
            self.hooks.io.call_hook = after_call
            with patch.object(b.v.Journal, 'put', put):
                result = self.run_one()
            self.assertEqual(result['failure'], 'VM2_INTERRUPTED')
            self.assertEqual(result['status'], 'UNKNOWN')
            self.assertTrue((self.root / 'interruption.json').exists())
            self.assertEqual(self.readback(result), result)

    def test_signal_during_handler_restoration_is_not_erased(self):
        original = signal.signal
        old = signal.getsignal(signal.SIGHUP)
        fired = []
        def install(sig, handler):
            if sig == signal.SIGHUP and handler is old and not fired:
                fired.append(True)
                signal.getsignal(signal.SIGHUP)(signal.SIGHUP, None)
            return original(sig, handler)
        with patch.object(signal, 'signal', side_effect=install):
            result = self.run_one()
        self.assertEqual(fired, [True])
        self.assertEqual(result['failure'], 'VM2_INTERRUPTED')
        self.assertEqual(self.readback(result), result)

    def test_veto_write_failure_and_abnormal_exit_cannot_accept_original_success(self):
        original = b.v.Journal.put
        def put(journal, name, value):
            original(journal, name, value)
            if name == 'result.json':
                signal.getsignal(signal.SIGTERM)(signal.SIGTERM, None)
        with patch.object(b.v.Journal, 'put', put), patch.object(b.v, 'record_interruption', side_effect=OSError(PRIVATE)):
            with self.assertRaises(OSError):
                self.run_one()
        saved = b.q.private_json(self.root / 'result.json')
        with self.assertRaisesRegex(b.Stop, 'BA1_MAIN_EXIT'):
            b.readback(self.scope, b.m.digest(saved), main_exit=2, root=self.root)
        for exit_code in (-15, -9, None, True):
            with self.assertRaisesRegex(b.Stop, 'BA1_MAIN_EXIT'):
                b.readback(self.scope, b.m.digest(saved), main_exit=exit_code, root=self.root)

    def test_result_digest_veto_deletion_and_foreign_files_refuse(self):
        result = self.run_one()
        with self.assertRaises(Exception):
            b.readback(self.scope, 'f' * 64, main_exit=0, root=self.root)
        b.v.record_interruption(self.root, result['resultSha256'])
        with self.assertRaises(Exception):
            self.readback(result)
        (self.root / 'interruption.json').unlink()
        with self.assertRaisesRegex(b.Stop, 'BA1_MAIN_EXIT'):
            self.readback(result, 2)
        (self.root / 'foreign.json').write_bytes(wire({'private': PRIVATE}))
        with self.assertRaisesRegex(b.Stop, 'BA1_CUSTODY'):
            self.readback(result)

    def test_committed_exact_scope_decision_and_command_bytes_required(self):
        suffix = self.scope['operationId'][:8] + '.json'
        names = ('APP013_P08_BA1_SCOPE_20261124_' + suffix, 'APP013_P08_BA1_APPROVAL_20261124_' + suffix)
        decision = {'owner': 'Debynyhan Banks', 'decision': b.DECISION, 'scopeSha256': b.m.digest(self.scope),
                    'operationId': self.scope['operationId'], 'externalReadAuthorized': True,
                    'independentCleanupAuthorized': True, 'sdkException': b.v.SDK_EXCEPTION,
                    'paymentAuthorized': False, 'allowanceUsd': 0}
        docs = {names[0]: wire(self.scope), names[1]: wire(decision), b.COMMAND.name: COMMAND.read_bytes()}
        read = lambda repo, commit, name: docs[name]
        self.assertEqual(b.authorize('c' * 40, *names, read_commit=read), self.scope)
        for key, value in (('externalReadAuthorized', False), ('independentCleanupAuthorized', False),
                           ('paymentAuthorized', True), ('scopeSha256', 'f' * 64), ('allowanceUsd', True)):
            docs[names[1]] = wire({**decision, key: value})
            with self.assertRaisesRegex(b.Stop, 'BA1_AUTHORITY'):
                b.authorize('c' * 40, *names, read_commit=read)
        docs[names[1]] = wire(decision)
        docs[b.COMMAND.name] = b'foreign command'
        with self.assertRaisesRegex(b.Stop, 'BA1_SOURCE'):
            b.authorize('c' * 40, *names, read_commit=read)

    def test_missing_authority_stops_before_native_factory_or_lease(self):
        with (patch.object(b, 'authorize', side_effect=b.Stop('BA1_AUTHORITY')),
              patch.object(b, 'NativeHooks') as factory, patch.object(b.v.sq, 'identity_lease') as lease):
            with self.assertRaisesRegex(b.Stop, 'BA1_AUTHORITY'):
                b.execute('c' * 40, 'scope', 'decision')
        factory.assert_not_called()
        lease.assert_not_called()

    def test_existing_identity_lease_prevents_concurrent_dispatch(self):
        lease_path = str(Path(self.tmp.name) / 'identity.lock')
        with (patch.object(b.v.sq, 'LEASE', lease_path), patch.object(b, 'authorize', return_value=self.scope),
              patch.object(b, 'NativeHooks') as factory, b.v.sq.identity_lease()):
            with self.assertRaises(Exception):
                b.execute('c' * 40, 'scope', 'decision')
            factory.assert_not_called()
        self.assertFalse(self.root.exists())

    def test_actual_owned_child_registration_signal_is_reaped_without_next_dispatch(self):
        handles = []
        actual = b.v.TrackedIO(self.clock, self.scope['operationId'])
        def spawn(argv, **kwargs):
            process = REAL_POPEN([sys.executable, '-I', '-B', '-c', 'print("[]")'], **kwargs)
            handles.append(process)
            signal.getsignal(signal.SIGTERM)(signal.SIGTERM, None)
            return process
        self.hooks.io_factory = lambda: actual
        with patch.object(subprocess, 'Popen', side_effect=spawn):
            result = b.run(self.scope, hooks=self.hooks, root=self.root)
        self.assertEqual(len(handles), 1)
        self.assertIsNotNone(handles[0].poll())
        with self.assertRaises(ProcessLookupError):
            os.killpg(handles[0].pid, 0)
        self.assertEqual(result['startedCli'], 1)
        self.assertEqual(result['observedProcesses'], 1)
        self.assertEqual(result['failure'], 'VM2_INTERRUPTED')
        self.assertTrue(all(result['closeout'].values()))
        self.assertEqual(self.readback(result), result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
