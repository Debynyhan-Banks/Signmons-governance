"""ED2 synthetic boundary checks. No real private inputs or provider transport."""
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
spec = importlib.util.spec_from_file_location('prepared_ed2', G / 'APP013_P08_ED2_COMMAND_20261125.py')
x = importlib.util.module_from_spec(spec)
spec.loader.exec_module(x)


def report(phase, state='DISABLED'):
    return {'status': 'ENDPOINT_OBSERVED', 'phase': phase, 'code': 'NONE', 'requests': 1,
            'httpStatus': 200, 'scope': 'MATCH', 'state': state}


def refused(phase, code='ENDPOINT_TRANSPORT_OR_OUTPUT_UNKNOWN', *, drift=False):
    return {'status': 'ENDPOINT_REFUSED', 'phase': phase, 'code': code, 'requests': 1,
            'httpStatus': 200 if drift else None, 'scope': 'DRIFT' if drift else 'UNKNOWN', 'state': 'UNKNOWN'}


def completed(value):
    return subprocess.CompletedProcess([], 0 if value['status'] == 'ENDPOINT_OBSERVED' else 2,
                                       json.dumps(value), '')


class Output(unittest.TestCase):
    def test_each_exact_phase_and_refused_post_preserve_distinct_evidence(self):
        for phase in ('OBSERVE', 'DISABLE', 'VERIFY'):
            for value in (report(phase), refused(phase)):
                self.assertEqual(x.validate_report(completed(value), phase), value)

    def test_verify_enabled_is_observation_and_not_disabled_proof(self):
        value = report('VERIFY', 'ENABLED')
        self.assertEqual(x.validate_report(completed(value), 'VERIFY')['state'], 'ENABLED')

    def test_wrong_phase_extra_fields_private_output_and_boolean_counts_refuse(self):
        values = []
        value = report('OBSERVE'); value['phase'] = 'DISABLE'; values.append(completed(value))
        value = report('OBSERVE'); value['fields'] = {'url': 'MATCH'}; values.append(completed(value))
        value = report('OBSERVE'); value['privatePayload'] = 'PRIVATE_SENTINEL'; values.append(completed(value))
        value = report('OBSERVE'); value['requests'] = True; values.append(completed(value))
        values.extend([subprocess.CompletedProcess([], 0, 'PRIVATE_SENTINEL', ''),
                       subprocess.CompletedProcess([], 0, json.dumps(report('OBSERVE')), 'PRIVATE_SENTINEL'),
                       subprocess.CompletedProcess([], 0, 'x' * 8193, ''),
                       subprocess.CompletedProcess([], 2, json.dumps(report('OBSERVE')), '')])
        for value in values:
            with self.assertRaises(Exception): x.validate_report(value, 'OBSERVE')


class Authority(unittest.TestCase):
    def setUp(self):
        self.scope = json.loads((G / x.SCOPE_FILE).read_text())
        self.scope['commandSha256'] = x.sha(Path(x.__file__))
        self.clock = x.r.m.timestamp(self.scope['window']['start']) + 1

    def decision(self):
        return {'decision': 'APPROVE_ED2_CONDITIONAL_DISABLE_VERIFY_AND_CLEANUP', 'owner': 'Debynyhan Banks',
                'operationId': x.OP, 'scopeSha256': x.r.m.digest(self.scope), 'externalReadAuthorized': True,
                'conditionalDisableAuthorized': True, 'independentCleanupAuthorized': True,
                'terminalReady': True, 'noOverlappingOperation': True,
                'reachableThrough': self.scope['window']['cleanupEnd'], 'paymentAuthorized': False}

    def check(self, decision=None, *, phase='launch', real_guard=False, after_guard=None):
        owner = self.decision() if decision is None else decision
        original = x.r.a.committed
        def read(repo, commit, name):
            if repo != G: return original(repo, commit, name)
            return {x.SCOPE_FILE: json.dumps(self.scope).encode(), x.DECISION_FILE: json.dumps(owner).encode(),
                    Path(x.__file__).name: Path(x.__file__).read_bytes()}[name]
        with patch.object(x.r.a, 'committed', read), patch.object(x.time, 'time', lambda: self.clock):
            if real_guard: return x.authorize('f' * 40, phase)
            with patch.object(x.v, 'source_guard', after_guard or (lambda _: None)), patch.object(x.r, 'guard', lambda _: None):
                return x.authorize('f' * 40, phase)

    def test_synthetic_committed_authority_uses_real_current_source_guards(self):
        self.assertEqual(self.check(real_guard=True)[0], self.scope)

    def test_missing_false_numeric_or_extra_authority_refuses(self):
        for key in ('externalReadAuthorized', 'conditionalDisableAuthorized', 'independentCleanupAuthorized',
                    'terminalReady', 'noOverlappingOperation'):
            for value in (False, 1):
                owner = self.decision(); owner[key] = value
                with self.subTest(key=key, value=value), self.assertRaises(Exception): self.check(owner)
            owner = self.decision(); del owner[key]
            with self.assertRaises(Exception): self.check(owner)
        owner = self.decision(); owner['paymentAuthorized'] = 0
        with self.assertRaises(Exception): self.check(owner)
        owner = self.decision(); owner['extra'] = True
        with self.assertRaises(Exception): self.check(owner)

    def test_source_resource_argv_command_and_boolean_budgets_refuse(self):
        saved = copy.deepcopy(self.scope)
        for key, value in [('sourceCommit', '0' * 40), ('commandSha256', '0' * 64),
                           ('argv', x.ARGV + ['--field-report']), ('limits', {**x.LIMITS, 'mutations': True}),
                           ('limits', {**x.LIMITS, 'https': 4}),
                           ('resources', {**self.scope['resources'], 'apiVersion': 'foreign'})]:
            self.scope = copy.deepcopy(saved); self.scope[key] = value
            with self.subTest(key=key), self.assertRaises(Exception): self.check()

    def test_each_phase_refuses_expiry_before_or_during_source_guards(self):
        for phase, key in [('launch', 'launchCutoff'), ('read', 'readEnd'), ('cleanup', 'verifyEnd')]:
            self.clock = x.r.m.timestamp(self.scope['window'][key])
            with self.subTest(phase=phase), self.assertRaises(Exception): self.check(phase=phase)
            self.clock = x.r.m.timestamp(self.scope['window']['start']) + 1
            def advance(_): self.clock = x.r.m.timestamp(self.scope['window'][key])
            with self.subTest(phase=phase), self.assertRaises(Exception): self.check(phase=phase, after_guard=advance)


class Composition(unittest.TestCase):
    def exercise(self, *, initial='enabled', change='disabled', final='disabled', ready='READY',
                 early_interrupt=False, interrupt_phase=None, fail_constructor=False,
                 unconfirmed_phase=None, integrity_failure=None, publication_interrupt=False,
                 readback_signal=False, publication_failure=False, held_lease=False):
        with tempfile.TemporaryDirectory(prefix='ed2-synthetic-', dir='/private/tmp') as temp:
            root = Path(temp) / 'operation'
            scope = json.loads((G / x.SCOPE_FILE).read_text())
            now = time.time()
            times = dict(start=now - 1, launchCutoff=now + 60, inputCutoff=now + 90,
                         readEnd=now + 105, verifyEnd=now + 170, cleanupEnd=now + 240)
            modes = {'OBSERVE': initial, 'DISABLE': change, 'VERIFY': final}
            rows = {}
            for phase, mode in modes.items():
                rows[phase] = (refused(phase, 'PAYMENT_ENDPOINT_DRIFT', drift=True) if mode == 'drift'
                    else refused(phase, 'KEY_CHECK_HTTP') if mode == 'http'
                    else refused(phase) if mode == 'lost'
                    else report(phase, 'ENABLED' if mode == 'enabled' else 'DISABLED'))
            fixture = ('import json,sys,time; request=json.load(sys.stdin); phase=request["phase"]; '
                'assert set(request)=={"phase","key","endpointId","deadline"}; '
                'assert request["key"].startswith("sk_test_"); assert request["endpointId"].startswith("we_"); '
                'modes=' + repr(modes) + '; rows=' + repr(rows) + '; '
                'time.sleep(30) if modes[phase]=="timeout" else None; '
                'print("PRIVATE_SENTINEL" if modes[phase]=="bad" else json.dumps(rows[phase])); '
                'sys.exit(0 if rows[phase]["status"]=="ENDPOINT_OBSERVED" else 2)')
            prompts, phases, timers, published, instances = [], [], [], [], []
            answers = iter(['sk_test_SYNTHETICONLY000000000000', 'we_SYNTHETICONLY'])
            previous_handler = signal.getsignal(signal.SIGTERM)
            previous_mask = signal.pthread_sigmask(signal.SIG_BLOCK, set())
            def hidden(prompt, cutoff):
                prompts.append(prompt)
                if early_interrupt: x.v.INTERRUPTED.set(True)
                return next(answers)
            def publish(text, **kwargs):
                self.assertEqual(signal.getsignal(signal.SIGTERM), previous_handler)
                self.assertEqual(signal.pthread_sigmask(signal.SIG_BLOCK, set()), previous_mask)
                self.assertNotIn('SYNTHETICONLY', text); self.assertNotIn('PRIVATE_SENTINEL', text)
                published.append(json.loads(text))
            original_init, original_child, original_finish = x.OwnedChild.__init__, x.OwnedChild.child, x.OwnedChild._finish_child
            def construct(io, *args):
                if fail_constructor and len(instances) == 1: raise OSError('PRIVATE_SENTINEL')
                original_init(io, *args); instances.append(io)
            def child(io, argv, **kwargs):
                phase = json.loads(kwargs['input'])['phase']; phases.append(phase); io.test_phase = phase
                self.assertEqual(kwargs['env'], x.ENV)
                self.assertNotIn('SYNTHETICONLY', repr(argv) + repr(kwargs['env']))
                if modes[phase] == 'timeout': kwargs['timeout'] = .15
                if interrupt_phase == phase:
                    timer = threading.Timer(.035, lambda: os.kill(os.getpid(), signal.SIGTERM))
                    timers.append(timer); timer.start()
                value = original_child(io, argv, **kwargs)
                if integrity_failure == 'clock' and phase == 'DISABLE':
                    raise x.r.k.inv.Stop('CLOCK_ROLLBACK')
                return value
            def finish(io, process):
                closed = original_finish(io, process)
                return False if getattr(io, 'test_phase', None) == unconfirmed_phase else closed
            guard_failed = []
            def source_guard(_):
                if integrity_failure == 'source' and phases and phases[-1] == 'DISABLE' and not guard_failed:
                    guard_failed.append(True); raise x.r.m.Stop('SOURCE_DRIFT')
            original_put, original_read = x.PhaseJournal.put, x.v.read_result
            flagged, queued = [], []
            def put(journal, name, value):
                if publication_failure and name == 'closeout.json': raise OSError('PRIVATE_SENTINEL')
                original_put(journal, name, value)
                if publication_interrupt and name == 'result.json' and not flagged:
                    flagged.append(True); signal.getsignal(signal.SIGTERM)(signal.SIGTERM, None)
            def readback(*args, **kwargs):
                value = original_read(*args, **kwargs)
                if readback_signal and not queued:
                    queued.append(True); os.kill(os.getpid(), signal.SIGTERM)
                return value
            with (patch.object(x, 'ROOT', root), patch.object(x, 'LEASE', str(Path(temp) / 'lease')),
                  patch.object(x, 'authorize', lambda *args: (scope, times)),
                  patch.object(x, 'ARGV', [str(Path(x.sys.executable).resolve()), '-I', '-B', '-c', fixture]),
                  patch.object(x.r, 'ct3_hidden', hidden), patch.object(x.r, 'ct3_inputs_valid', lambda *args: None),
                  patch.object(x.v, 'source_guard', source_guard), patch.object(x.r, 'guard', lambda _: None),
                  patch.object(x.OwnedChild, '__init__', construct), patch.object(x.OwnedChild, 'child', child),
                  patch.object(x.OwnedChild, '_finish_child', finish), patch.object(x.PhaseJournal, 'put', put),
                  patch.object(x.v, 'read_result', readback), patch('builtins.input', return_value=ready),
                  patch('builtins.print', side_effect=publish)):
                if held_lease:
                    with x.r.k.lease(x.LEASE), self.assertRaises(Exception): x.execute('f' * 40)
                    self.assertFalse(root.exists()); self.assertEqual(prompts, []); self.assertEqual(phases, [])
                    return None
                try:
                    code = x.execute('f' * 40)
                finally:
                    for timer in timers: timer.join()
                    self.assertEqual(signal.getsignal(signal.SIGTERM), previous_handler)
                    self.assertEqual(signal.pthread_sigmask(signal.SIG_BLOCK, set()), previous_mask)
                stored = json.loads((root / 'result.json').read_text())
                receipts = {p.name: json.loads(p.read_text()) for p in root.iterdir()}
                self.assertNotIn('SYNTHETICONLY', json.dumps(receipts)); self.assertNotIn('PRIVATE_SENTINEL', json.dumps(receipts))
                self.assertTrue(stored['privateReferencesCleared']); self.assertFalse(stored['privateInputsPersisted'])
                self.assertFalse(stored['paymentAuthorized']); self.assertLessEqual(stored['workerInvocations'], 3)
                self.assertLessEqual(phases.count('DISABLE'), 1)
                for phase in stored['phaseReservations']:
                    self.assertEqual(receipts[phase.lower() + '.json'], {'operationId': x.OP, 'phase': phase,
                        'requestReserved': True, 'method': 'POST' if phase == 'DISABLE' else 'GET'})
                self.assertEqual(published[-1]['resultSha256'], x.r.m.digest(stored))
                before = len(prompts)
                with self.assertRaises(FileExistsError): x.execute('f' * 40)
                self.assertEqual(len(prompts), before)
                return code, stored, published[-1], phases, prompts, receipts

    def test_enabled_runs_one_disable_then_independent_disabled_verify(self):
        code, result, _, phases, prompts, _ = self.exercise()
        self.assertEqual(code, 0); self.assertEqual(phases, ['OBSERVE', 'DISABLE', 'VERIFY'])
        self.assertTrue(result['disableAcknowledged']); self.assertTrue(result['finalDisabled'])
        self.assertTrue(result['processCleanupVerified']); self.assertEqual(result['ownedChildCount'], 3)
        self.assertEqual(result['status'], 'ENDPOINT_DISABLED_CONFIRMED')
        self.assertIn('sk_test_', prompts[0]); self.assertIn('we_', prompts[1])

    def test_initially_disabled_skips_post_but_verifies(self):
        code, result, _, phases, _, receipts = self.exercise(initial='disabled')
        self.assertEqual(code, 0); self.assertEqual(phases, ['OBSERVE', 'VERIFY'])
        self.assertFalse(result['disableAttempted']); self.assertFalse(result['disableAcknowledged'])
        self.assertNotIn('disable.json', receipts); self.assertEqual(result['ownedChildCount'], 2)

    def test_initial_drift_or_refusal_never_authorizes_post_or_confirmation(self):
        for mode in ('drift', 'http', 'bad'):
            with self.subTest(mode=mode):
                code, result, _, phases, _, _ = self.exercise(initial=mode)
                self.assertEqual(code, 2); self.assertNotIn('DISABLE', phases)
                self.assertFalse(result['disableAttempted']); self.assertTrue(result['finalDisabled'])
                self.assertEqual(result['status'], 'ENDPOINT_CORRECTION_UNKNOWN')

    def test_lost_or_timed_out_post_never_retries_and_final_read_can_prove_disabled(self):
        for mode in ('lost', 'timeout', 'bad'):
            with self.subTest(mode=mode):
                code, result, _, phases, _, _ = self.exercise(change=mode)
                self.assertEqual(code, 0); self.assertEqual(phases, ['OBSERVE', 'DISABLE', 'VERIFY'])
                self.assertTrue(result['disableAttempted']); self.assertFalse(result['disableAcknowledged'])
                self.assertTrue(result['finalDisabled']); self.assertTrue(result['processCleanupVerified'])
                self.assertTrue(any(f['stage'] == 'DISABLE' for f in result['failureDetails']))

    def test_verify_enabled_drift_http_or_timeout_never_confirms(self):
        for mode in ('enabled', 'drift', 'http', 'timeout'):
            with self.subTest(mode=mode):
                code, result, _, phases, _, _ = self.exercise(final=mode)
                self.assertEqual(code, 2); self.assertFalse(result['finalDisabled'])
                self.assertEqual(phases.count('DISABLE'), 1); self.assertEqual(phases.count('VERIFY'), 1)

    def test_no_ready_or_early_interrupt_starts_no_worker(self):
        for options in ({'ready': 'NO'}, {'early_interrupt': True}):
            with self.subTest(options=options):
                code, result, _, phases, _, receipts = self.exercise(**options)
                self.assertEqual(code, 2); self.assertEqual(phases, []); self.assertEqual(result['workerInvocations'], 0)
                if options.get('early_interrupt'): self.assertIn('interruption.json', receipts)

    def test_interrupted_post_closes_then_authorized_verify_runs_without_success(self):
        code, result, safe, phases, _, receipts = self.exercise(change='timeout', interrupt_phase='DISABLE')
        self.assertEqual(code, 2); self.assertEqual(phases, ['OBSERVE', 'DISABLE', 'VERIFY'])
        self.assertTrue(result['finalDisabled']); self.assertTrue(result['processCleanupVerified'])
        self.assertIn('interruption.json', receipts); self.assertEqual(safe['status'], 'UNKNOWN')

    def test_unknown_owned_closure_blocks_further_workers(self):
        code, result, _, phases, _, _ = self.exercise(unconfirmed_phase='DISABLE')
        self.assertEqual(code, 2); self.assertEqual(phases, ['OBSERVE', 'DISABLE'])
        self.assertFalse(result['processCleanupVerified']); self.assertFalse(result['finalDisabled'])
        self.assertIn('OWNED_PROCESS_UNCONFIRMED', result['residuals'])

    def test_failed_worker_construction_cannot_erase_missing_history(self):
        code, result, _, phases, _, _ = self.exercise(fail_constructor=True)
        self.assertEqual(code, 2); self.assertEqual(phases, ['OBSERVE'])
        self.assertFalse(result['processCleanupVerified']); self.assertEqual(result['workerInvocations'], 2)
        self.assertEqual(result['ownedChildCount'], 1); self.assertFalse(result['finalDisabled'])

    def test_source_or_clock_integrity_failure_cannot_be_cured_by_final_read(self):
        for kind in ('source', 'clock'):
            with self.subTest(kind=kind):
                code, result, _, phases, _, _ = self.exercise(integrity_failure=kind)
                self.assertEqual(code, 2); self.assertEqual(phases, ['OBSERVE', 'DISABLE', 'VERIFY'])
                self.assertTrue(result['finalDisabled']); self.assertFalse(result['integrityVerified'])

    def test_existing_lease_refuses_before_inputs_or_attempt_root(self):
        self.exercise(held_lease=True)

    def test_late_result_publication_signal_persists_veto(self):
        code, _, safe, _, _, receipts = self.exercise(publication_interrupt=True)
        self.assertEqual(code, 2); self.assertIn('interruption.json', receipts); self.assertEqual(safe['status'], 'UNKNOWN')

    def test_pending_signal_during_readback_vetoes_then_reaches_original_handler(self):
        previous = signal.getsignal(signal.SIGTERM); delivered = []
        signal.signal(signal.SIGTERM, lambda *_: delivered.append(True))
        try:
            code, _, safe, _, _, receipts = self.exercise(readback_signal=True)
            self.assertEqual(code, 2); self.assertIn('interruption.json', receipts)
            self.assertEqual(safe['status'], 'UNKNOWN'); self.assertEqual(delivered, [True])
        finally: signal.signal(signal.SIGTERM, previous)

    def test_publication_exception_restores_original_mask_and_handlers(self):
        with self.assertRaises(OSError): self.exercise(publication_failure=True)


if __name__ == '__main__':
    unittest.main()
