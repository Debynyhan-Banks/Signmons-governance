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

OP = '32337134-670a-45d0-bc83-21cf25f64cdd'
SOURCE = '92c4d03712153558717f918e1d53fc87a54de663'
SCOPE_FILE = 'APP013_P08_ED1_LIVE1_SCOPE_20261125.json'
DECISION_FILE = 'APP013_P08_ED1_LIVE1_DECISION_20261125.json'
ROOT = Path('/private/tmp/p08-ed1-' + OP)
LEASE = '/private/tmp/p08-account-containment.lock'
FIELDS = {'objectType', 'endpointIdentity', 'sandboxMode', 'url', 'apiVersion',
          'enabledEvents', 'recognizedStatus', 'disabledStatus'}
LABELS = {'MATCH', 'MISMATCH', 'TYPE_INVALID'}
ARGV = [r.NODE, str(r.ENDPOINT_WORKER), '--endpoint-once', '--field-report']
LIMITS = {'https': 1, 'child': 1, 'sql': 0, 'sdk': 0, 'cache': 0, 'mutations': 0}
ENV = {'PATH': '/usr/bin:/bin:/opt/homebrew/bin', 'LANG': 'C'}
need = r.need


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def expected_resources():
    values = r.ct3_resources()
    return {k: values[k] for k in ('endpointSha256', 'endpointUrl', 'apiVersion', 'node', 'worker')}


def authorize(commit, phase):
    need(re.fullmatch('[a-f0-9]{40}', commit or '') and phase in ('launch', 'read'), 'ED1_AUTHORITY')
    scope = r.q.strict_json(r.a.committed(G, commit, SCOPE_FILE))
    need(type(scope) is dict and set(scope) == {'action', 'operationId', 'sourceCommit', 'commandSha256',
         'manifestSha256', 'containmentManifestSha256', 'interpreters', 'resources', 'argv',
         'limits', 'window', 'costAllowanceUsd'}, 'ED1_SCOPE')
    need(scope['action'] == 'READ_EXACT_SANDBOX_WEBHOOK_FIELDS_ONCE' and scope['operationId'] == OP and
         scope['sourceCommit'] == SOURCE and scope['argv'] == ARGV and
         type(scope['limits']) is dict and scope['limits'] == LIMITS and
         all(type(count) is int for count in scope['limits'].values()) and
         scope['resources'] == expected_resources() and type(scope['costAllowanceUsd']) is int and
         scope['costAllowanceUsd'] == 0, 'ED1_SCOPE')
    command = Path(__file__)
    need(not command.is_symlink() and sha(command) == scope['commandSha256'] and
         r.a.committed(G, commit, command.name) == command.read_bytes(), 'ED1_COMMAND')
    need(scope['interpreters'] == {str(Path(sys.executable).resolve()): sha(Path(sys.executable).resolve()),
         r.NODE: sha(r.NODE)}, 'ED1_INTERPRETER')
    decision = r.q.strict_json(r.a.committed(G, commit, DECISION_FILE))
    need(type(decision) is dict and all(type(decision.get(key)) is bool for key in
         ('externalReadAuthorized', 'independentCleanupAuthorized', 'terminalReady',
          'noOverlappingOperation', 'paymentAuthorized')) and
         decision == {'decision': 'APPROVE_ED1_ONE_WEBHOOK_READ_AND_CLEANUP', 'owner': 'Debynyhan Banks',
         'operationId': OP, 'scopeSha256': r.m.digest(scope), 'externalReadAuthorized': True,
         'independentCleanupAuthorized': True, 'terminalReady': True, 'noOverlappingOperation': True,
         'reachableThrough': scope['window']['cleanupEnd'], 'paymentAuthorized': False}, 'ED1_APPROVAL')
    t = {key: r.m.timestamp(value) for key, value in scope['window'].items()}
    need(set(t) == {'start', 'launchCutoff', 'inputCutoff', 'readEnd', 'cleanupEnd'} and
         t['start'] < t['launchCutoff'] < t['inputCutoff'] < t['readEnd'] < t['cleanupEnd'] and
         t['cleanupEnd'] - t['start'] <= 1800 and t['cleanupEnd'] - t['readEnd'] >= 60,
         'ED1_WINDOW')
    now = time.time()
    need(t['start'] <= now < t['launchCutoff' if phase == 'launch' else 'inputCutoff'], 'ED1_DEADLINE')
    v.source_guard({'sourceCommit': SOURCE, 'manifestSha256': scope['manifestSha256']})
    r.guard({'sourceCommit': SOURCE, 'manifestSha256': scope['containmentManifestSha256']})
    need(now <= time.time() < t['launchCutoff' if phase == 'launch' else 'inputCutoff'], 'ED1_DEADLINE')
    return scope, t


def validate_report(completed):
    need(type(completed.stdout) is str and len(completed.stdout.encode()) <= 8192 and
         completed.stderr == '', 'ED1_OUTPUT')
    value = r.q.strict_json(completed.stdout)
    need(type(value) is dict, 'ED1_OUTPUT')
    has_fields = 'fields' in value
    fields = value.pop('fields', None)
    legacy = subprocess.CompletedProcess([], completed.returncode, json.dumps(value), completed.stderr)
    base = r.endpoint_result(legacy, 'OBSERVE')
    if has_fields:
        need(type(fields) is dict and set(fields) == FIELDS and
             all(type(x) is str and x in LABELS for x in fields.values()) and
             base['requests'] == 1 and base['httpStatus'] == 200 and base['scope'] in ('MATCH', 'DRIFT'),
             'ED1_FIELDS')
        matched = all(label == 'MATCH' for key, label in fields.items() if key != 'disabledStatus')
        need(matched == (base['scope'] == 'MATCH'), 'ED1_FIELDS')
        if matched:
            need(fields['disabledStatus'] == ('MATCH' if base['state'] == 'DISABLED' else 'MISMATCH'), 'ED1_FIELDS')
    return {**base, **({'fields': fields} if fields is not None else {})}


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
    key = destination = payload = completed = None
    io = None
    last = time.time()
    hard_end = time.monotonic() + max(0, t['readEnd'] - last)
    def gate(cleanup=False):
        nonlocal last
        now = time.time()
        need(now >= last and now < t['cleanupEnd' if cleanup else 'readEnd'], 'ED1_DEADLINE')
        last = now
        if not cleanup:
            need(not v.INTERRUPTED.get() and time.monotonic() < hard_end, 'ED1_INTERRUPTED_OR_DEADLINE')
        journal.inspect()
        return t['cleanupEnd' if cleanup else 'readEnd']

    signals = {signal.SIGTERM, signal.SIGHUP, signal.SIGINT}
    previous_mask = None
    interruption_required = False
    try:
        with r.k.lease(LEASE):
            with v.interruption_handlers():
                journal = v.Journal(ROOT)
                journal.put('attempt.json', {'operationId': OP, 'scopeSha256': r.m.digest(scope),
                            'approvalCommit': commit, 'startedAt': datetime.datetime.now(datetime.timezone.utc).isoformat()})
                result = {'operationId': OP, 'status': 'ENDPOINT_OBSERVATION_UNKNOWN', 'failure': None,
                          'report': None, 'workerInvocations': 0, 'paymentAuthorized': False}
                try:
                    with r.k.acl.http_deadline(min(120, t['inputCutoff'] - time.time())):
                        need(input('Type READY to begin the two hidden inputs: ') == 'READY', 'ED1_NOT_READY')
                    gate()
                    key = r.ct3_hidden('1/2 Existing Sandbox SECRET KEY starting sk_test_ (hidden): ', t['inputCutoff'])
                    gate()
                    destination = r.ct3_hidden('2/2 Existing DESTINATION ID starting we_ (hidden): ', t['inputCutoff'])
                    r.ct3_inputs_valid(key, destination)
                    need(len(destination) <= 256, 'ED1_INPUT')
                    rebound, _ = authorize(commit, 'read')
                    need(rebound == scope, 'ED1_SCOPE_DRIFT')
                    gate()
                    until = min(t['readEnd'], time.time() + 15)
                    need(until - time.time() >= 7, 'ED1_DEADLINE')
                    io = OwnedChild(time.time, t, gate)
                    journal.put('metadata.json', {'operationId': OP, 'requestReserved': True, 'method': 'GET'})
                    result['workerInvocations'] = 1
                    payload = json.dumps({'phase': 'OBSERVE', 'key': key, 'endpointId': destination,
                                          'deadline': int(until * 1000)}, separators=(',', ':'))
                    key = destination = None
                    completed = io.child(ARGV, input=payload, text=True, capture_output=True,
                                          timeout=max(.01, until - time.time()), env=ENV)
                    payload = None
                    gate()
                    v.source_guard({'sourceCommit': SOURCE, 'manifestSha256': scope['manifestSha256']})
                    r.guard({'sourceCommit': SOURCE, 'manifestSha256': scope['containmentManifestSha256']})
                    result['report'] = validate_report(completed)
                    result['workerExit'] = completed.returncode
                    gate()
                    if result['report'].get('fields') and result['report']['code'] in ('NONE', 'PAYMENT_ENDPOINT_DRIFT'):
                        result['status'] = 'ENDPOINT_FIELD_OBSERVATION_RECORDED'
                except BaseException:
                    result['status'] = 'ENDPOINT_OBSERVATION_UNKNOWN'
                    result['failure'] = 'INTERRUPTED' if v.INTERRUPTED.get() else 'INPUT_OR_BOUNDARY_UNCONFIRMED'
                finally:
                    key = destination = payload = completed = None
                    # Keep signals masked through immutable publication and handler
                    # restoration. Pending signals veto this completion; they are
                    # delivered only after the original handlers are back in place.
                    previous_mask = signal.pthread_sigmask(signal.SIG_BLOCK, signals)
                    if io is not None:
                        for process in list(io.child_processes):
                            try:
                                io._finish_child(process)
                            except BaseException:
                                io.child_cleanup_unconfirmed = True
                    closed = (io is None and result['workerInvocations'] == 0) or (
                        io is not None and io.absent(result['workerInvocations']))
                    on_time = last <= time.time() < t['cleanupEnd']
                    interrupted = v.INTERRUPTED.get() or bool(signal.sigpending() & signals)
                    if interrupted or not closed or not on_time:
                        result['status'] = 'ENDPOINT_OBSERVATION_UNKNOWN'
                    result.update(privateInputsPersisted=False, privateReferencesCleared=True,
                                  processCleanupVerified=closed, onTime=on_time,
                                  ownedChildCount=0 if io is None else len(io.observed),
                                  residuals=[] if closed else ['OWNED_PROCESS_UNCONFIRMED'])
                    journal.put('closeout.json', {key: result[key] for key in
                                ('operationId', 'privateInputsPersisted', 'privateReferencesCleared',
                                 'processCleanupVerified', 'onTime', 'ownedChildCount', 'residuals')})
                    journal.put('result.json', result)
                    result_digest = r.m.digest(result)
                    interruption_required = v.INTERRUPTED.get() or bool(signal.sigpending() & signals)
                    if interruption_required:
                        v.record_interruption(ROOT, result_digest)
            # The flag-only handlers have now been restored. Keep the mask until
            # safe readback and one final pending-signal check establish completion.
            result = v.read_result(ROOT, result_digest, interruption_required=interruption_required)
            if signal.sigpending() & signals:
                interruption_required = True
                result = v.record_interruption(ROOT, result_digest)
            result = v.read_result(ROOT, result_digest, interruption_required=interruption_required)
            if signal.sigpending() & signals and not interruption_required:
                result = v.record_interruption(ROOT, result_digest)
            # Completion is established here. A later signal uses the original
            # handlers; it cannot be silently consumed during printing or return.
    finally:
        if previous_mask is not None:
            signal.pthread_sigmask(signal.SIG_SETMASK, previous_mask)
    print(json.dumps(result, sort_keys=True), flush=True)
    return 0 if result['status'] == 'ENDPOINT_FIELD_OBSERVATION_RECORDED' and not result['residuals'] else 2


if __name__ == '__main__':
    try:
        need(len(sys.argv) == 2, 'ED1_ARGUMENTS')
        code = execute(sys.argv[1])
    except BaseException:
        print('ED1_NOT_STARTED_OR_UNCONFIRMED', flush=True)
        code = 2
    sys.exit(code)
