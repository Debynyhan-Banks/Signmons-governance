"""Prepared one-operation command; no native action without exact committed approval."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import time

B = Path('/Users/debynyhanbanks/Web Projects/signmons-backend-r08-recovery')
G = Path('/Users/debynyhanbanks/Web Projects/signmons-governance-r08-recovery')
D = B / 'evidence/APP-013/p08-connected-packet-20261110'
sys.path.insert(0, str(D))
import account_containment_read as r
import vm2_metadata_read as v

OP = '195cb801-cacb-4552-9265-08614c0c0e28'
SOURCE = 'afe3afe5d6c292fa8c721683ac521b615c4b7784'
SCOPE_FILE = 'APP013_P08_ED2_SCOPE_20261125.json'
DECISION_FILE = 'APP013_P08_ED2_DECISION_20261125.json'
ROOT = Path('/private/tmp/p08-ed2-' + OP)
LEASE = '/private/tmp/p08-account-containment.lock'
ARGV = [r.NODE, str(r.ENDPOINT_WORKER), '--endpoint-once']
LIMITS = {'https': 3, 'child': 3, 'sql': 0, 'sdk': 0, 'cache': 0, 'mutations': 1}
ENV = {'PATH': '/usr/bin:/bin:/opt/homebrew/bin', 'LANG': 'C'}
need = r.need


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def expected_resources():
    values = r.ct3_resources()
    return {k: values[k] for k in ('endpointSha256', 'endpointUrl', 'apiVersion', 'node', 'worker')}


def authorize(commit, phase):
    need(re.fullmatch('[a-f0-9]{40}', commit or '') and phase in ('launch', 'read', 'cleanup'), 'ED2_AUTHORITY')
    scope = r.q.strict_json(r.a.committed(G, commit, SCOPE_FILE))
    need(type(scope) is dict and set(scope) == {'action', 'operationId', 'sourceCommit', 'commandSha256',
         'manifestSha256', 'containmentManifestSha256', 'interpreters', 'resources', 'argv',
         'limits', 'window', 'costAllowanceUsd'}, 'ED2_SCOPE')
    need(scope['action'] == 'CONDITIONALLY_DISABLE_EXACT_SANDBOX_WEBHOOK_AND_VERIFY' and scope['operationId'] == OP and
         scope['sourceCommit'] == SOURCE and scope['argv'] == ARGV and
         type(scope['limits']) is dict and scope['limits'] == LIMITS and
         all(type(count) is int for count in scope['limits'].values()) and
         scope['resources'] == expected_resources() and type(scope['costAllowanceUsd']) is int and
         scope['costAllowanceUsd'] == 0, 'ED2_SCOPE')
    command = Path(__file__)
    need(not command.is_symlink() and sha(command) == scope['commandSha256'] and
         r.a.committed(G, commit, command.name) == command.read_bytes(), 'ED2_COMMAND')
    need(scope['interpreters'] == {str(Path(sys.executable).resolve()): sha(Path(sys.executable).resolve()),
         r.NODE: sha(r.NODE)}, 'ED2_INTERPRETER')
    decision = r.q.strict_json(r.a.committed(G, commit, DECISION_FILE))
    need(type(decision) is dict and all(type(decision.get(key)) is bool for key in
         ('externalReadAuthorized', 'conditionalDisableAuthorized', 'independentCleanupAuthorized', 'terminalReady',
          'noOverlappingOperation', 'paymentAuthorized')) and
         decision == {'decision': 'APPROVE_ED2_CONDITIONAL_DISABLE_VERIFY_AND_CLEANUP', 'owner': 'Debynyhan Banks',
         'operationId': OP, 'scopeSha256': r.m.digest(scope), 'externalReadAuthorized': True, 'conditionalDisableAuthorized': True,
         'independentCleanupAuthorized': True, 'terminalReady': True, 'noOverlappingOperation': True,
         'reachableThrough': scope['window']['cleanupEnd'], 'paymentAuthorized': False}, 'ED2_APPROVAL')
    t = {key: r.m.timestamp(value) for key, value in scope['window'].items()}
    need(set(t) == {'start', 'launchCutoff', 'inputCutoff', 'readEnd', 'verifyEnd', 'cleanupEnd'} and
         t['start'] < t['launchCutoff'] < t['inputCutoff'] < t['readEnd'] < t['verifyEnd'] < t['cleanupEnd'] and
         t['cleanupEnd'] - t['start'] <= 1800 and t['verifyEnd'] - t['readEnd'] >= 60 and t['cleanupEnd'] - t['verifyEnd'] >= 60,
         'ED2_WINDOW')
    now = time.time()
    need(t['start'] <= now < t[{'launch': 'launchCutoff', 'read': 'readEnd', 'cleanup': 'verifyEnd'}[phase]], 'ED2_DEADLINE')
    v.source_guard({'sourceCommit': SOURCE, 'manifestSha256': scope['manifestSha256']})
    r.guard({'sourceCommit': SOURCE, 'manifestSha256': scope['containmentManifestSha256']})
    need(now <= time.time() < t[{'launch': 'launchCutoff', 'read': 'readEnd', 'cleanup': 'verifyEnd'}[phase]], 'ED2_DEADLINE')
    return scope, t


def validate_report(completed, phase):
    return r.endpoint_result(completed, phase)


class PhaseJournal(v.Journal):
    """Same immutable custody implementation, with this operation's phase names."""
    def put(self, name, value):
        need(name in {'attempt.json', 'observe.json', 'disable.json', 'verify.json',
                      'closeout.json', 'result.json', 'interruption.json'}, 'VM2_CUSTODY')
        self.inspect()
        r.m.reserve(self.root / name, value)
        self.hashes[name] = r.m.digest((self.root / name).read_bytes())
        self.inspect()


class OwnedChild(r.EndpointChild):
    def __init__(self, clock, times, gate):
        super().__init__(clock, times, gate, False)
        self.observed = set()

    def _finish_child(self, process):
        self.observed.add(process)
        return super()._finish_child(process)

    def absent(self, expected):
        if (type(expected) is not int or expected not in (0, 1) or
                len(self.observed) != expected or self.child_processes or self.child_cleanup_unconfirmed):
            return False
        for process in self.observed:
            try:
                if process.poll() is None:
                    return False
                process.wait(timeout=0)
                if process.returncode is None:
                    return False
            except (OSError, subprocess.TimeoutExpired):
                return False
            try:
                os.killpg(process.pid, 0)
                return False
            except ProcessLookupError:
                pass
            except OSError:
                return False
        return True


def execute(commit):
    scope, t = authorize(commit, 'launch')
    key = destination = None
    ios = []
    integrity = True
    last = time.time()
    hard_end = time.monotonic() + max(0, t['readEnd'] - last)
    verify_hard_end = time.monotonic() + max(0, t['verifyEnd'] - last)
    result = {'operationId': OP, 'status': 'ENDPOINT_CORRECTION_UNKNOWN', 'failureDetails': [],
              'initial': None, 'change': None, 'final': None, 'disableAttempted': False,
              'disableAcknowledged': False, 'finalDisabled': False, 'workerInvocations': 0,
              'phaseReservations': [], 'paymentAuthorized': False}

    def gate(cleanup=False):
        nonlocal last, integrity
        now = time.time()
        if now < last:
            integrity = False
            need(False, 'ED2_CLOCK_ROLLBACK')
        need(now < t['verifyEnd' if cleanup else 'readEnd'], 'ED2_DEADLINE')
        last = now
        need(time.monotonic() < (verify_hard_end if cleanup else hard_end), 'ED2_DEADLINE')
        if not cleanup:
            need(integrity and not v.INTERRUPTED.get(), 'ED2_INTERRUPTED_OR_INTEGRITY')
        journal.inspect()
        return t['verifyEnd' if cleanup else 'readEnd']

    def phase_call(phase):
        nonlocal integrity
        payload = completed = request = None
        need(phase in ('OBSERVE', 'DISABLE', 'VERIFY') and
             phase not in result['phaseReservations'] and len(ios) < 3, 'ED2_PHASE')
        need(len(ios) == result['workerInvocations'] and all(io.absent(1) for io in ios), 'ED2_PRIOR_CHILD_CLOSURE')
        if phase == 'DISABLE':
            need(result['initial'] is not None and result['initial']['scope'] == 'MATCH' and
                 result['initial']['status'] == 'ENDPOINT_OBSERVED' and
                 result['initial']['state'] == 'ENABLED' and not result['disableAttempted'], 'ED2_ELIGIBILITY')
        cleanup = phase == 'VERIFY'
        try:
            rebound, _ = authorize(commit, 'cleanup' if cleanup else 'read')
            need(rebound == scope, 'ED2_SCOPE_DRIFT')
        except BaseException:
            integrity = False
            raise
        gate(cleanup)
        until = min(t['verifyEnd' if cleanup else 'readEnd'], time.time() + 15)
        need(until - time.time() >= 7, 'ED2_DEADLINE')
        journal.put(phase.lower() + '.json', {'operationId': OP, 'phase': phase,
                    'requestReserved': True, 'method': 'POST' if phase == 'DISABLE' else 'GET'})
        result['phaseReservations'].append(phase)
        result['workerInvocations'] += 1
        if phase == 'DISABLE': result['disableAttempted'] = True
        io = OwnedChild(time.time, t, gate)
        io.cleanup = cleanup
        ios.append(io)
        try:
            request = {'phase': phase, 'key': key, 'endpointId': destination, 'deadline': int(until * 1000)}
            payload = json.dumps(request, separators=(',', ':'))
            request.clear(); request = None
            completed = io.child(ARGV, input=payload, text=True, capture_output=True,
                                 timeout=max(.01, until - time.time()), env=ENV)
            payload = None
            gate(cleanup)
            try:
                v.source_guard({'sourceCommit': SOURCE, 'manifestSha256': scope['manifestSha256']})
                r.guard({'sourceCommit': SOURCE, 'manifestSha256': scope['containmentManifestSha256']})
            except BaseException:
                integrity = False
                raise
            value = validate_report(completed, phase)
            gate(cleanup)
            return value
        except BaseException as error:
            if (type(error) in (r.m.Stop, r.k.inv.Stop) and type(error.args) is tuple and
                    len(error.args) == 1 and type(error.args[0]) is str and
                    error.args[0] in ('CLOCK_ROLLBACK', 'ED2_CLOCK_ROLLBACK')):
                integrity = False
            raise
        finally:
            if request is not None: request.clear()
            payload = completed = request = None

    def failed(stage):
        result['failureDetails'].append({'stage': stage, 'code': 'INTERRUPTED' if v.INTERRUPTED.get() else 'BOUNDARY_UNCONFIRMED'})

    signals = {signal.SIGTERM, signal.SIGHUP, signal.SIGINT}
    previous_mask = None
    interruption_required = False
    inputs_valid = False
    try:
        with r.k.lease(LEASE):
            with v.interruption_handlers():
                journal = PhaseJournal(ROOT)
                journal.put('attempt.json', {'operationId': OP, 'scopeSha256': r.m.digest(scope),
                            'approvalCommit': commit, 'startedAt': datetime.datetime.now(datetime.timezone.utc).isoformat()})
                stage = 'INPUT'
                try:
                    with r.k.acl.http_deadline(min(120, t['inputCutoff'] - time.time())):
                        need(input('Type READY to begin the two hidden inputs: ') == 'READY', 'ED2_NOT_READY')
                    gate()
                    key = r.ct3_hidden('1/2 Existing Sandbox SECRET KEY starting sk_test_ (hidden): ', t['inputCutoff'])
                    gate()
                    destination = r.ct3_hidden('2/2 Existing DESTINATION ID starting we_ (hidden): ', t['inputCutoff'])
                    r.ct3_inputs_valid(key, destination)
                    need(len(destination) <= 256 and time.time() < t['inputCutoff'], 'ED2_INPUT')
                    inputs_valid = True
                    stage = 'OBSERVE'
                    result['initial'] = phase_call('OBSERVE')
                    if (result['initial']['status'] == 'ENDPOINT_OBSERVED' and
                        result['initial']['scope'] == 'MATCH' and result['initial']['state'] == 'ENABLED'):
                        stage = 'DISABLE'
                        result['change'] = phase_call('DISABLE')
                        result['disableAcknowledged'] = (result['change']['status'] == 'ENDPOINT_OBSERVED' and
                            result['change']['scope'] == 'MATCH' and result['change']['state'] == 'DISABLED')
                        if not result['disableAcknowledged']: failed('DISABLE')
                except BaseException:
                    failed(stage)
                finally:
                    # Independent readback is reserved even after a failed/uncertain
                    # POST; no POST is ever retried. Masked signals cannot cancel it.
                    previous_mask = signal.pthread_sigmask(signal.SIG_BLOCK, signals)
                    for io in ios:
                        for process in list(io.child_processes):
                            try: io._finish_child(process)
                            except BaseException: io.child_cleanup_unconfirmed = True
                    if inputs_valid:
                        try:
                            result['final'] = phase_call('VERIFY')
                            result['finalDisabled'] = (result['final']['status'] == 'ENDPOINT_OBSERVED' and
                                result['final']['scope'] == 'MATCH' and result['final']['state'] == 'DISABLED')
                        except BaseException:
                            failed('VERIFY')
                    key = destination = None
                    for io in ios:
                        for process in list(io.child_processes):
                            try: io._finish_child(process)
                            except BaseException: io.child_cleanup_unconfirmed = True
                    closed = len(ios) == result['workerInvocations'] and all(io.absent(1) for io in ios)
                    on_time = last <= time.time() < t['cleanupEnd']
                    interrupted = v.INTERRUPTED.get() or bool(signal.sigpending() & signals)
                    initial_matched = (result['initial'] is not None and result['initial']['status'] == 'ENDPOINT_OBSERVED'
                                       and result['initial']['scope'] == 'MATCH')
                    if initial_matched and result['finalDisabled'] and closed and on_time and integrity and not interrupted:
                        result['status'] = 'ENDPOINT_DISABLED_CONFIRMED'
                    result.update(privateInputsPersisted=False, privateReferencesCleared=True,
                                  processCleanupVerified=closed, onTime=on_time, integrityVerified=integrity,
                                  ownedChildCount=sum(len(io.observed) for io in ios),
                                  residuals=[] if closed else ['OWNED_PROCESS_UNCONFIRMED'])
                    journal.put('closeout.json', {name: result[name] for name in
                                ('operationId', 'privateInputsPersisted', 'privateReferencesCleared',
                                 'processCleanupVerified', 'onTime', 'ownedChildCount', 'residuals')})
                    journal.put('result.json', result)
                    result_digest = r.m.digest(result)
                    interruption_required = v.INTERRUPTED.get() or bool(signal.sigpending() & signals)
                    if interruption_required: v.record_interruption(ROOT, result_digest)
            result = v.read_result(ROOT, result_digest, interruption_required=interruption_required)
            if signal.sigpending() & signals:
                interruption_required = True
                result = v.record_interruption(ROOT, result_digest)
            result = v.read_result(ROOT, result_digest, interruption_required=interruption_required)
            if signal.sigpending() & signals and not interruption_required:
                result = v.record_interruption(ROOT, result_digest)
    finally:
        key = destination = None
        if previous_mask is not None: signal.pthread_sigmask(signal.SIG_SETMASK, previous_mask)
    print(json.dumps(result, sort_keys=True), flush=True)
    return 0 if result['status'] == 'ENDPOINT_DISABLED_CONFIRMED' and not result['residuals'] else 2


if __name__ == '__main__':
    try:
        need(len(sys.argv) == 2, 'ED2_ARGUMENTS')
        code = execute(sys.argv[1])
    except BaseException:
        print('ED2_NOT_STARTED_OR_UNCONFIRMED', flush=True)
        code = 2
    sys.exit(code)
