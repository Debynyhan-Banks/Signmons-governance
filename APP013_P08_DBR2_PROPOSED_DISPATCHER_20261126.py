"""Local-only corrected template. R60 is expired; fresh reviewed bindings are required before any future launch."""
from pathlib import Path
import sys,json,hashlib,os,shlex,subprocess,time
B=Path('/Users/debynyhanbanks/Web Projects/signmons-backend-r08-recovery');G=Path('/Users/debynyhanbanks/Web Projects/signmons-governance-r08-recovery');D=B/'evidence/APP-013/p08-connected-packet-20261110';sys.path.insert(0,str(D))
import packet as p
q=p.q

def deliver_to_terminal(cmd, command_path, cutoff):
    """Deliver the unchanged full command through a short owned-file reference."""
    if not time.time()<cutoff:
        raise RuntimeError('TERMINAL_DISPATCH_CUTOFF')
    command_path=Path(command_path)
    body=(cmd+'\n').encode('utf-8')
    fd=os.open(command_path,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
    with os.fdopen(fd,'wb') as stream:
        stream.write(body)
    expected=hashlib.sha256(body).hexdigest()
    info=command_path.lstat()
    if command_path.is_symlink() or info.st_uid!=os.getuid() or info.st_nlink!=1 or info.st_mode&0o777!=0o600:
        raise RuntimeError('TERMINAL_COMMAND_CUSTODY')
    if hashlib.sha256(command_path.read_bytes()).hexdigest()!=expected:
        raise RuntimeError('TERMINAL_COMMAND_CHANGED')
    short='source '+shlex.quote(str(command_path))
    if len(short.encode('utf-8'))>=256:
        raise RuntimeError('TERMINAL_COMMAND_REFERENCE_TOO_LONG')
    apple='on run argv\n tell application "Terminal"\n activate\n do script (item 1 of argv)\n end tell\nend run'
    if not time.time()<cutoff:
        raise RuntimeError('TERMINAL_DISPATCH_CUTOFF')
    result=subprocess.run(['/usr/bin/osascript','-e',apple,short],capture_output=True,text=True,check=True)
    return result,expected

scope=G/'APP013_P08_DATABASE_ROLE_DIAGNOSTIC_PACKET_DBR2_20261126.json'
e=json.loads(scope.read_text())
commit='PENDING_EXACT_DBR2_APPROVAL'
name='APP013_P08_DATABASE_ROLE_DIAGNOSTIC_OPERATION_20261126.json'
raw=q.current_module('authority').committed(G,commit,name)
e['decision']={'commit':commit,'path':name,'sha256':hashlib.sha256(raw).hexdigest()}
cap=q.RoleDiagnosticCapability(e);cap.prepare()
root=Path('/private/tmp/p08-dbr2-request-'+e['operationId']);root.mkdir(mode=0o700)
q.model.reserve(root/'envelope.json',e)
BOOT="""import sys
from pathlib import Path
sys.path.insert(0,sys.argv[1])
import qualification_launch as q
source=Path(sys.argv[2]);envelope=q.private_json(source)
owned=Path('/private/tmp/p08-database-role-'+envelope['operationId'])
try:
    q.role_diagnostic_main(['--diagnose-database-role',str(source)])
finally:
    if owned.exists() and not (owned/'closeout.json').exists():
        q.role_diagnostic_main(['--closeout-database-role',str(owned)])
"""
argv=[p.PYTHON,'-I','-B','-c',BOOT,str(q.model.ROOT),str(root/'envelope.json')]
cmd='cd '+shlex.quote(str(B))+' && '+shlex.join(argv)
command_path=Path('/private/tmp/p08-dbr2-terminal-'+e['operationId']+'.command')
result,sha=deliver_to_terminal(cmd,command_path,cap.times['cutoff'])
print(json.dumps({'status':'DBR2_DISPATCHED','terminal':result.stdout.strip(),'ownedCommandPath':str(command_path),'ownedCommandSha256':sha,'decisionCommit':commit}))
