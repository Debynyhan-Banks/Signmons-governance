"""BA1 exact one-shot operator command; local preparation grants no live authority."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import sys
import time

B = Path('/Users/debynyhanbanks/Web Projects/signmons-backend-r08-recovery')
G = Path('/Users/debynyhanbanks/Web Projects/signmons-governance-r08-recovery')
COMMAND = G / 'APP013_P08_BA1_READ_COMMAND_20261124.py'
sys.path.insert(0, str(B / 'evidence/APP-013/p08-connected-packet-20261110'))
import vm2_metadata_read as v

q, m = v.q, v.m
SOURCE = '2f13f90ae4cda3a61e719308d54cc19c1dd3c0d1'
MANIFEST = '0c3c90cdad6cf8a1c742a37de20d9cbf8f9fcd7ad772f97fbd486dbfe71bec78'
ACCOUNT_SHA256 = q.BILLING_ACCOUNT_SHA256
ACTION = 'BA1_LINKED_BILLING_ACCOUNT_STATUS_ONCE'
DECISION = 'APPROVE_BA1_LINKED_ACCOUNT_STATUS_SDK_EXCEPTION_AND_CLEANUP'
LIMITS = {'cli': 3, 'cache': 0, 'https': 0, 'sql': 0, 'mutations': 0}
SLOTS = (('owner', 'owner.json'), ('billing_project', 'project.json'), ('billing_account', 'metadata.json'))
SIGNALS = (signal.SIGINT, signal.SIGTERM, signal.SIGHUP)
CODES = frozenset(('BA1_SCOPE BA1_AUTHORITY BA1_SOURCE BA1_CONFIG BA1_WINDOW BA1_CUTOFF '
    'BA1_DEADLINE BA1_CLOCK BA1_OWNER BA1_PROJECT BA1_ACCOUNT BA1_OUTPUT BA1_REPLAY BA1_CUSTODY '
    'BA1_MAIN_EXIT BA1_ARGUMENTS BA1_CLOSEOUT BA1_UNCONFIRMED VM2_INTERRUPTED').split()) | q.CLI_FAILURE_CODES


class Stop(Exception):
    pass


def need(value, code):
    if not value:
        raise Stop(code)


def safe_code(error):
    if isinstance(error, (KeyboardInterrupt, SystemExit)):
        return 'VM2_INTERRUPTED'
    if type(error) in (Stop, m.Stop) and len(error.args) == 1 and type(error.args[0]) is str:
        return error.args[0] if error.args[0] in CODES else 'BA1_UNCONFIRMED'
    return 'BA1_UNCONFIRMED'


def commands(account='<discovered-account>'):
    return tuple(next(d for d in q.cli_contract(account) if d['id'] == name) for name, _ in SLOTS)


def root_for(operation_id):
    m.exact_uuid(operation_id, 'BA1_SCOPE')
    return Path('/private/tmp/p08-ba1-' + operation_id)


def validate_scope(scope):
    need(type(scope) is dict and set(scope) == {'version', 'action', 'operationId', 'sourceCommit',
         'manifestSha256', 'commandSha256', 'configSha256', 'billingAccountSha256', 'commands', 'window',
         'limits', 'sdkException', 'allowanceUsd', 'automaticRetryAllowed'}, 'BA1_SCOPE')
    root_for(scope['operationId'])
    need(type(scope['version']) is int and scope['version'] == 1 and scope['action'] == ACTION and
         scope['sourceCommit'] == SOURCE and scope['manifestSha256'] == MANIFEST and
         scope['billingAccountSha256'] == ACCOUNT_SHA256 and scope['limits'] == LIMITS and
         all(type(x) is int for x in scope['limits'].values()) and scope['sdkException'] == v.SDK_EXCEPTION and
         type(scope['allowanceUsd']) is int and scope['allowanceUsd'] == 0 and
         scope['automaticRetryAllowed'] is False and scope['commands'] == json.loads(json.dumps(commands())), 'BA1_SCOPE')
    for key in ('commandSha256', 'configSha256'):
        need(type(scope[key]) is str and re.fullmatch('[a-f0-9]{64}', scope[key]), 'BA1_SOURCE')
    need(type(scope['window']) is dict and set(scope['window']) ==
         {'start', 'cutoff', 'readEnd', 'closeoutEnd'}, 'BA1_WINDOW')
    t = {key: m.timestamp(value) for key, value in scope['window'].items()}
    need(t['start'] < t['cutoff'] < t['readEnd'] < t['closeoutEnd'] and
         t['readEnd'] - t['cutoff'] >= 90 and t['closeoutEnd'] - t['readEnd'] >= 120 and
         t['closeoutEnd'] - t['start'] <= 1200, 'BA1_WINDOW')
    return t


def source_guard(scope):
    need(Path(__file__).absolute() == COMMAND and not COMMAND.is_symlink() and COMMAND.is_file() and
         m.digest(COMMAND.read_bytes()) == scope['commandSha256'], 'BA1_SOURCE')
    v.source_guard({'sourceCommit': scope['sourceCommit'], 'manifestSha256': scope['manifestSha256']})


def authorize(commit, scope_name, decision_name, *, read_commit=None):
    need(type(commit) is str and re.fullmatch('[a-f0-9]{40}', commit), 'BA1_AUTHORITY')
    for name, label in ((scope_name, 'SCOPE'), (decision_name, 'APPROVAL')):
        need(type(name) is str and re.fullmatch('APP013_P08_BA1_' + label + r'_20261124_[a-f0-9]{8}\.json', name),
             'BA1_AUTHORITY')
    get = v.a.committed if read_commit is None else read_commit
    scope = v.sq.strict_json(get(G, commit, scope_name))
    validate_scope(scope)
    suffix = scope['operationId'][:8] + '.json'
    need(scope_name.endswith(suffix) and decision_name.endswith(suffix), 'BA1_AUTHORITY')
    decision = v.sq.strict_json(get(G, commit, decision_name))
    need(type(decision) is dict and all(type(decision.get(k)) is bool for k in
         ('externalReadAuthorized', 'independentCleanupAuthorized', 'paymentAuthorized')) and
         type(decision.get('allowanceUsd')) is int and decision == {
             'owner': 'Debynyhan Banks', 'decision': DECISION, 'scopeSha256': m.digest(scope),
             'operationId': scope['operationId'], 'externalReadAuthorized': True,
             'independentCleanupAuthorized': True, 'sdkException': v.SDK_EXCEPTION,
             'paymentAuthorized': False, 'allowanceUsd': 0}, 'BA1_AUTHORITY')
    need(get(G, commit, COMMAND.name) == COMMAND.read_bytes() and
         m.digest(COMMAND.read_bytes()) == scope['commandSha256'], 'BA1_SOURCE')
    return scope


class NativeHooks:
    clock = staticmethod(time.time)
    configuration = staticmethod(v.configuration)

    def __init__(self, scope, refs):
        self.scope, self.refs = scope, tuple(refs)
        need(authorize(*self.refs) == scope, 'BA1_AUTHORITY')

    def guard(self, scope):
        need(scope == self.scope and authorize(*self.refs) == scope, 'BA1_AUTHORITY')
        source_guard(scope)

    def io_factory(self):
        return v.TrackedIO(self.clock, self.scope['operationId'])


def run(scope, *, hooks, root=None):
    """The test seam has no native defaults; native hooks require committed authority."""
    t = validate_scope(scope)
    need(t['start'] <= hooks.clock() < t['cutoff'], 'BA1_CUTOFF')
    hooks.guard(scope)
    need(hooks.configuration() == scope['configSha256'], 'BA1_CONFIG')
    q.sdk_environment(os.environ)
    need(t['start'] <= hooks.clock() < t['cutoff'], 'BA1_CUTOFF')
    root = root_for(scope['operationId']) if root is None else Path(root)
    need(not os.path.lexists(root), 'BA1_REPLAY')
    previous = {sig: signal.getsignal(sig) for sig in SIGNALS}
    with v.interruption_handlers():
        journal = v.Journal(root)
        journal.put('attempt.json', {'operationId': scope['operationId'], 'scopeSha256': m.digest(scope),
                                    'sourceCommit': scope['sourceCommit'], 'commandSha256': scope['commandSha256']})
        result = {'status': 'UNKNOWN', 'operationId': scope['operationId'], 'scopeSha256': m.digest(scope),
                  'sourceCommit': scope['sourceCommit'], 'commandSha256': scope['commandSha256'],
                  'ownerMatched': False, 'projectMatched': False, 'accountMatched': False,
                  'billingEnabled': None, 'accountOpen': None, 'counts': {'cli': 0, 'cache': 0, 'https': 0, 'sql': 0},
                  'startedCli': 0, 'observedProcesses': 0, 'stage': 'PREPARE', 'failure': None,
                  'paymentAttempted': False}
        io = raw = value = account = descriptor = None
        last = hooks.clock()

        def gate():
            nonlocal last
            now = hooks.clock()
            need(not v.INTERRUPTED.get(), 'VM2_INTERRUPTED')
            need(now >= last, 'BA1_CLOCK')
            last = now
            need(t['start'] <= now < t['readEnd'], 'BA1_DEADLINE')
            hooks.guard(scope)
            need(hooks.configuration() == scope['configSha256'], 'BA1_CONFIG')
            q.sdk_environment(os.environ)
            journal.inspect()
            now = hooks.clock()
            need(not v.INTERRUPTED.get(), 'VM2_INTERRUPTED')
            need(last <= now < t['readEnd'], 'BA1_DEADLINE')
            last = now

        try:
            io = hooks.io_factory()
            for index, (label, slot) in enumerate(SLOTS):
                result['stage'] = label
                gate()
                need(result['counts']['cli'] == index, 'BA1_SCOPE')
                descriptor = commands(account if label == 'billing_account' else '<discovered-account>')[index]
                q.validate_cli_descriptor(descriptor)
                journal.put(slot, {'descriptorId': label, 'reserved': True})
                result['counts']['cli'] += 1
                gate()
                env = q.sdk_environment(os.environ)
                now = hooks.clock()
                need(not v.INTERRUPTED.get(), 'VM2_INTERRUPTED')
                need(last <= now < t['readEnd'], 'BA1_DEADLINE')
                last = now
                result['startedCli'] += 1
                raw = io._owned_run(descriptor['argv'], env, min(t['readEnd'], now + 30))
                gate()
                value = v.sq.strict_json(raw)
                raw = None
                if label == 'owner':
                    need(value == [{'account': m.OWNER, 'status': 'ACTIVE'}], 'BA1_OWNER')
                    result['ownerMatched'] = True
                elif label == 'billing_project':
                    need(type(value) is dict and set(value) == {'projectId', 'billingAccountName', 'billingEnabled'} and
                         value['projectId'] == m.PROJECT and type(value['billingEnabled']) is bool, 'BA1_PROJECT')
                    account = value['billingAccountName']
                    need(type(account) is str and re.fullmatch(r'billingAccounts/[A-F0-9]{6}(?:-[A-F0-9]{6}){2}', account) and
                         hashlib.sha256(account.encode('utf-8')).hexdigest() == scope['billingAccountSha256'], 'BA1_ACCOUNT')
                    result.update(projectMatched=True, accountMatched=True, billingEnabled=value['billingEnabled'])
                else:
                    need(type(value) is dict and set(value) == {'open'} and type(value['open']) is bool, 'BA1_OUTPUT')
                    result['accountOpen'] = value['open']
                value = descriptor = None
            result['status'] = 'BA1_ACCOUNT_STATUS_OBSERVED'
        except BaseException as error:
            result['failure'] = safe_code(error)
        finally:
            raw = value = account = descriptor = None
            closed = absent = io is None
            try:
                if io is not None:
                    closed = io.close(t['closeoutEnd']) is True
            except BaseException:
                closed = False
            try:
                if io is not None:
                    result['observedProcesses'] = len(io.observed)
                    absent = io.verify_absent(t['closeoutEnd']) is True
            except BaseException:
                absent = False
            configuration = False
            try:
                configuration = hooks.configuration() == scope['configSha256']
            except BaseException:
                pass
            closure = {'processCleanupVerified': closed, 'independentProcessAbsence': absent,
                       'processHistoryComplete': result['observedProcesses'] == result['startedCli'],
                       'configurationUnchanged': configuration, 'onTime': last <= hooks.clock() < t['closeoutEnd']}
            io = None
            if v.INTERRUPTED.get():
                result['failure'] = 'VM2_INTERRUPTED'
            result['closeout'] = closure
            result['residuals'] = [] if all(closure.values()) else ['LOCAL_CLOSEOUT_UNCONFIRMED']
            if result['failure'] is not None or result['residuals']:
                result['status'] = 'UNKNOWN'
            result['completedAt'] = datetime.datetime.fromtimestamp(hooks.clock(), datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
            journal.put('closeout.json', closure)
            digest = m.digest(result)
            journal.put('result.json', result)
        # Restore handlers before the final pending-signal check. A later normal
        # process interruption is rejected by the separate actual-exit check.
        for sig, handler in previous.items():
            signal.signal(sig, handler)
        if v.INTERRUPTED.get() or result['failure'] == 'VM2_INTERRUPTED':
            result = v.record_interruption(root, digest)
        else:
            result = v.read_result(root, digest, interruption_required=result['failure'] == 'VM2_INTERRUPTED')
        return result


def readback(scope, expected_digest, *, main_exit, root=None):
    """Local readback only. The caller supplies the independently observed exit."""
    t = validate_scope(scope)
    need(type(main_exit) is int and main_exit in (0, 2), 'BA1_MAIN_EXIT')
    root = root_for(scope['operationId']) if root is None else Path(root)
    result = v.read_result(root, expected_digest)
    need(set(result) == {'status', 'operationId', 'scopeSha256', 'sourceCommit', 'commandSha256', 'ownerMatched',
         'projectMatched', 'accountMatched', 'billingEnabled', 'accountOpen', 'counts', 'startedCli', 'observedProcesses',
         'stage', 'failure', 'paymentAttempted', 'closeout', 'residuals', 'completedAt', 'resultSha256'}, 'BA1_CUSTODY')
    need(result['operationId'] == scope['operationId'] and result['scopeSha256'] == m.digest(scope) and
         result['sourceCommit'] == scope['sourceCommit'] and result['commandSha256'] == scope['commandSha256'] and
         result['status'] in ('BA1_ACCOUNT_STATUS_OBSERVED', 'UNKNOWN') and
         (result['failure'] is None or result['failure'] in CODES) and
         result['stage'] in ('PREPARE', *(label for label, _ in SLOTS)) and result['paymentAttempted'] is False and
         all(type(result[key]) is bool for key in ('ownerMatched', 'projectMatched', 'accountMatched')) and
         all(result[key] is None or type(result[key]) is bool for key in ('billingEnabled', 'accountOpen')) and
         type(result['counts']) is dict and set(result['counts']) == {'cli', 'cache', 'https', 'sql'} and
         all(result['counts'][key] == 0 for key in ('cache', 'https', 'sql')) and
         all(type(x) is int for x in result['counts'].values()) and
         type(result['startedCli']) is int and type(result['observedProcesses']) is int and
         0 <= result['observedProcesses'] <= result['startedCli'] <= result['counts']['cli'] <= 3, 'BA1_CUSTODY')
    need(type(result['closeout']) is dict and set(result['closeout']) == {'processCleanupVerified',
         'independentProcessAbsence', 'processHistoryComplete', 'configurationUnchanged', 'onTime'} and
         all(type(x) is bool for x in result['closeout'].values()), 'BA1_CLOSEOUT')
    closed = all(result['closeout'].values())
    need(result['residuals'] == ([] if closed else ['LOCAL_CLOSEOUT_UNCONFIRMED']) and
         result['closeout']['processHistoryComplete'] == (result['observedProcesses'] == result['startedCli']) and
         (not result['closeout']['onTime'] or t['start'] <= m.timestamp(result['completedAt']) < t['closeoutEnd']), 'BA1_CLOSEOUT')
    if result['status'] == 'BA1_ACCOUNT_STATUS_OBSERVED':
        need(main_exit == 0 and result['failure'] is None and closed and result['stage'] == 'billing_account' and
             all(result[key] is True for key in ('ownerMatched', 'projectMatched', 'accountMatched')) and
             all(type(result[key]) is bool for key in ('billingEnabled', 'accountOpen')) and
             result['startedCli'] == result['observedProcesses'] == result['counts']['cli'] == 3, 'BA1_MAIN_EXIT')
    else:
        need(main_exit == 2 and (result['failure'] is not None or not closed), 'BA1_MAIN_EXIT')
    expected_files = {'attempt.json', 'closeout.json', 'result.json'} | {
        slot for _, slot in SLOTS[:result['counts']['cli']]}
    if result['failure'] == 'VM2_INTERRUPTED':
        v.read_result(root, expected_digest, interruption_required=True)
        expected_files.add('interruption.json')
    need({path.name for path in root.iterdir()} == expected_files, 'BA1_CUSTODY')
    need(q.private_json(root / 'attempt.json') == {'operationId': scope['operationId'], 'scopeSha256': m.digest(scope),
         'sourceCommit': scope['sourceCommit'], 'commandSha256': scope['commandSha256']}, 'BA1_CUSTODY')
    for label, slot in SLOTS[:result['counts']['cli']]:
        need(q.private_json(root / slot) == {'descriptorId': label, 'reserved': True}, 'BA1_CUSTODY')
    need(q.private_json(root / 'closeout.json') == result['closeout'], 'BA1_CUSTODY')
    return result


def execute(commit, scope_name, decision_name):
    scope = authorize(commit, scope_name, decision_name)
    with v.sq.identity_lease():
        return run(scope, hooks=NativeHooks(scope, (commit, scope_name, decision_name)))


if __name__ == '__main__':
    try:
        need(len(sys.argv) == 4, 'BA1_ARGUMENTS')
        result = execute(*sys.argv[1:])
        print(json.dumps(result, sort_keys=True))
        rc = 0 if result['status'] == 'BA1_ACCOUNT_STATUS_OBSERVED' and not result['residuals'] else 2
    except BaseException as error:
        print(json.dumps({'status': 'UNKNOWN', 'failure': safe_code(error)}))
        rc = 2
    raise SystemExit(rc)
