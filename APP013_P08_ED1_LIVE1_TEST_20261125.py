"""Synthetic preparation checks only. No provider client or real private input."""
import copy
import importlib.util
import json
import os
from pathlib import Path
import signal
import subprocess
import tempfile
import threading
import time
import unittest
from unittest.mock import patch

G = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('prepared_ed1', G / 'APP013_P08_ED1_LIVE1_COMMAND_20261125.py')
x = importlib.util.module_from_spec(spec)
spec.loader.exec_module(x)


def report(drift=False):
    fields = dict.fromkeys(x.FIELDS, 'MATCH')
    if drift:
        fields['apiVersion'] = 'MISMATCH'
    return {'status': 'ENDPOINT_REFUSED' if drift else 'ENDPOINT_OBSERVED', 'phase': 'OBSERVE',
            'code': 'PAYMENT_ENDPOINT_DRIFT' if drift else 'NONE', 'requests': 1,
            'httpStatus': 200, 'scope': 'DRIFT' if drift else 'MATCH',
            'state': 'UNKNOWN' if drift else 'DISABLED', 'fields': fields}


def completed(value, code=0):
    return subprocess.CompletedProcess([], code, json.dumps(value), '')


class Output(unittest.TestCase):
    def test_match_and_exit_two_drift_remain_distinct_useful_observations(self):
        self.assertEqual(x.validate_report(completed(report())), report())
        self.assertEqual(x.validate_report(completed(report(True), 2)), report(True))

    def test_missing_fields_is_not_invented_evidence(self):
        value = {'status': 'ENDPOINT_REFUSED', 'phase': 'OBSERVE', 'code': 'KEY_CHECK_HTTP',
                 'requests': 1, 'httpStatus': 403, 'scope': 'UNKNOWN', 'state': 'UNKNOWN'}
        self.assertEqual(x.validate_report(completed(value, 2)), value)

    def test_invalid_labels_extra_fields_and_inconsistent_scope_refuse(self):
        variants = []
        for field in ('privatePayload', 'fields'):
            value = report()
            if field == 'fields':
                value[field]['url'] = 'https://PRIVATE_SENTINEL.invalid'
            else:
                value[field] = 'PRIVATE_SENTINEL'
            variants.append(value)
        value = report(); value['fields']['url'] = 'MISMATCH'; variants.append(value)
        value = report(); value['fields']['disabledStatus'] = 'TYPE_INVALID'; variants.append(value)
        value = report(); value['fields'] = None; variants.append(value)
        value = report(); del value['fields']['apiVersion']; variants.append(value)
        value = report(); value['requests'] = True; variants.append(value)
        for value in variants:
            with self.subTest(value=value), self.assertRaises(Exception):
                x.validate_report(completed(value))

    def test_raw_stderr_non_json_overflow_and_wrong_exit_refuse(self):
        for result in [subprocess.CompletedProcess([], 0, '{}', 'PRIVATE_SENTINEL'),
                       subprocess.CompletedProcess([], 0, 'PRIVATE_SENTINEL', ''),
                       subprocess.CompletedProcess([], 0, 'x' * 8193, ''), completed(report(), 2)]:
            with self.assertRaises(Exception):
                x.validate_report(result)


class Authority(unittest.TestCase):
    def setUp(self):
        self.scope = json.loads((G / x.SCOPE_FILE).read_text())
        self.scope['commandSha256'] = x.sha(G / 'APP013_P08_ED1_LIVE1_COMMAND_20261125.py')
        self.clock = x.r.m.timestamp(self.scope['window']['start']) + 1

    def decision(self):
        return {'decision': 'APPROVE_ED1_ONE_WEBHOOK_READ_AND_CLEANUP', 'owner': 'Debynyhan Banks',
                'operationId': x.OP, 'scopeSha256': x.r.m.digest(self.scope), 'externalReadAuthorized': True,
                'independentCleanupAuthorized': True, 'terminalReady': True, 'noOverlappingOperation': True,
                'reachableThrough': self.scope['window']['cleanupEnd'], 'paymentAuthorized': False}

    def check(self, decision=None, real_guard=False, after_guard=None):
        owner = self.decision() if decision is None else decision
        actual = x.r.a.committed
        def read(repo, commit, name):
            if repo != G:
                return actual(repo, commit, name)
            values = {x.SCOPE_FILE: json.dumps(self.scope).encode(), x.DECISION_FILE: json.dumps(owner).encode(),
                      Path(x.__file__).name: Path(x.__file__).read_bytes()}
            return values[name]
        with patch.object(x.r.a, 'committed', read), patch.object(x.time, 'time', lambda: self.clock):
            if real_guard:
                return x.authorize('f' * 40, 'launch')
            with patch.object(x.v, 'source_guard', after_guard or (lambda _: None)), patch.object(x.r, 'guard', lambda _: None):
                return x.authorize('f' * 40, 'launch')

    def test_exact_synthetic_binding_through_real_current_source_guards(self):
        self.assertEqual(self.check(real_guard=True)[0], self.scope)

    def test_false_numeric_missing_or_extra_approval_refuses(self):
        for key in ('externalReadAuthorized', 'independentCleanupAuthorized', 'terminalReady', 'noOverlappingOperation'):
            for value in (False, 1):
                decision = self.decision(); decision[key] = value
                with self.subTest(key=key, value=value), self.assertRaises(Exception): self.check(decision)
        decision = self.decision(); decision['paymentAuthorized'] = 0
        with self.assertRaises(Exception): self.check(decision)
        decision = self.decision(); decision['extra'] = True
        with self.assertRaises(Exception): self.check(decision)

    def test_source_command_resource_argv_and_boolean_budget_drift_refuse(self):
        original = copy.deepcopy(self.scope)
        for key, value in [('sourceCommit', '0' * 40), ('commandSha256', '0' * 64),
                           ('argv', x.ARGV + ['--other']), ('limits', {**x.LIMITS, 'https': True}),
                           ('resources', {**self.scope['resources'], 'apiVersion': 'foreign'})]:
            self.scope = copy.deepcopy(original); self.scope[key] = value
            with self.subTest(key=key), self.assertRaises(Exception): self.check()

    def test_expired_before_or_during_guards_refuses(self):
        self.clock = x.r.m.timestamp(self.scope['window']['launchCutoff'])
        with self.assertRaises(Exception): self.check()
        self.clock = x.r.m.timestamp(self.scope['window']['start']) + 1
        def advance(_): self.clock = x.r.m.timestamp(self.scope['window']['launchCutoff'])
        with self.assertRaises(Exception): self.check(after_guard=advance)


class Composition(unittest.TestCase):
    def exercise(self, *, drift=False, ready='READY', body=None, interrupt=False, early_interrupt=False):
        with tempfile.TemporaryDirectory(prefix='ed1-synthetic-', dir='/private/tmp') as temp:
            root = Path(temp) / 'operation'
            scope = json.loads((G / x.SCOPE_FILE).read_text())
            now = time.time(); times = dict(start=now - 1, launchCutoff=now + 60, inputCutoff=now + 90,
                                           readEnd=now + 105, cleanupEnd=now + 120)
            value = report(drift)
            code = 2 if drift else 0
            fixture = body or ('import sys,json; v=json.load(sys.stdin); '
                'assert v["phase"]=="OBSERVE"; '
                'assert v["key"].startswith("sk_test_"); '
                'print(' + repr(json.dumps(value)) + '); sys.exit(' + str(code) + ')')
            answers = iter(['sk_test_SYNTHETICONLY000000000000', 'we_SYNTHETICONLY'])
            prompts = []
            def hidden(prompt, cutoff):
                prompts.append(prompt)
                if early_interrupt: x.v.INTERRUPTED.set(True)
                return next(answers)
            previous_handler = signal.getsignal(signal.SIGTERM)
            published = []
            def publish(text, **kwargs):
                self.assertEqual(signal.getsignal(signal.SIGTERM), previous_handler)
                self.assertNotIn('SYNTHETICONLY', text)
                self.assertNotIn('PRIVATE_SENTINEL', text)
                published.append(text)
            original_child = x.OwnedChild.child
            def bounded_child(io, argv, **kwargs):
                if body is not None: kwargs['timeout'] = .15
                return original_child(io, argv, **kwargs)
            timer = None
            with (patch.object(x, 'ROOT', root), patch.object(x, 'LEASE', str(Path(temp) / 'lease')),
                 patch.object(x, 'authorize', lambda *args: (scope, times)),
                 patch.object(x, 'ARGV', [str(Path(x.sys.executable).resolve()), '-I', '-B', '-c', fixture]),
                 patch.object(x.r, 'ct3_hidden', hidden), patch.object(x.r, 'ct3_inputs_valid', lambda *args: None),
                 patch.object(x.v, 'source_guard', lambda *args: None), patch.object(x.r, 'guard', lambda *args: None),
                 patch.object(x.OwnedChild, 'child', bounded_child), patch('builtins.input', return_value=ready),
                 patch('builtins.print', side_effect=publish)):
                if interrupt:
                    timer = threading.Timer(.05, lambda: os.kill(os.getpid(), signal.SIGTERM)); timer.start()
                try: exit_code = x.execute('f' * 40)
                finally:
                    if timer: timer.join()
                result = json.loads((root / 'result.json').read_text())
                self.assertTrue(result['processCleanupVerified'])
                self.assertTrue(result['privateReferencesCleared'])
                self.assertFalse(result['privateInputsPersisted'])
                self.assertNotIn('SYNTHETICONLY', ''.join(p.read_text() for p in root.iterdir()))
                before = len(prompts)
                with self.assertRaises(FileExistsError): x.execute('f' * 40)
                self.assertEqual(len(prompts), before)
                return exit_code, result, (root / 'interruption.json').exists(), prompts

    def test_match_and_drift_with_real_owned_local_child(self):
        for drift in (False, True):
            code, result, interrupted, prompts = self.exercise(drift=drift)
            self.assertEqual(code, 0); self.assertEqual(result['workerExit'], 2 if drift else 0)
            self.assertEqual(result['ownedChildCount'], 1); self.assertFalse(interrupted)
            self.assertIn('sk_test_', prompts[0]); self.assertIn('we_', prompts[1])

    def test_refused_ready_has_no_child_or_hidden_prompt(self):
        code, result, _, prompts = self.exercise(ready='NO')
        self.assertEqual(code, 2); self.assertEqual(result['workerInvocations'], 0); self.assertEqual(prompts, [])

    def test_transport_timeout_closes_real_owned_child_without_retry(self):
        code, result, _, _ = self.exercise(body='import time; time.sleep(30)')
        self.assertEqual(code, 2); self.assertEqual(result['ownedChildCount'], 1)
        self.assertEqual(result['workerInvocations'], 1)

    def test_bad_worker_output_never_reaches_safe_receipt(self):
        code, result, _, _ = self.exercise(body='print("PRIVATE_SENTINEL")')
        self.assertEqual(code, 2); self.assertIsNone(result['report'])

    def test_interruption_before_dispatch_persists_veto(self):
        code, result, interrupted, _ = self.exercise(early_interrupt=True)
        self.assertEqual(code, 2); self.assertEqual(result['workerInvocations'], 0); self.assertTrue(interrupted)

    def test_interruption_during_child_preserves_owned_cleanup_and_veto(self):
        code, result, interrupted, _ = self.exercise(body='import time; time.sleep(30)', interrupt=True)
        self.assertEqual(code, 2); self.assertEqual(result['ownedChildCount'], 1); self.assertTrue(interrupted)


if __name__ == '__main__':
    unittest.main()
