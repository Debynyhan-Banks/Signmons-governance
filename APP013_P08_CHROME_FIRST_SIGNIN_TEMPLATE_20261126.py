"""Ephemeral operator procedure for the exact approved TR34; no reusable launcher."""
import datetime,fcntl,json,os,signal,stat,subprocess,sys,time,uuid
from pathlib import Path
B=Path('/Users/debynyhanbanks/Web Projects/signmons-backend-r08-recovery')
sys.path.insert(0,str(B/'evidence/APP-013/p08-connected-packet-20261110'))
import packet as p
q=p.q;m=q.model;a=q.current_module('authority');acl=q.current_module('acl')
COMMIT='PENDING_EXACT_TR34_APPROVAL'
SOURCE='b72ecb89f1907a25c988bbe3f33388bfdab77976'
NAME='APP013_P08_TR34_DECISION_20261126.json'
ROOT=B/'evidence/APP-013/p08-narrow-access-check-local-20261101/renewals/20261126-tr34'
ARGV=['/opt/homebrew/bin/gcloud','auth','login','debynyhan@signmons.com','--force','--no-activate','--brief','--quiet','--verbosity=none']
def preflight():
    raw=a.committed(p.G,COMMIT,NAME);d=q.strict_json(raw)
    draft=q.strict_json(a.committed(p.G,COMMIT,'APP013_P08_TR34_DECISION_DRAFT_20261126.json'))
    m.need(d==draft['decisionForReview'] and d['reservation']=='owner-signin-20261126-tr34' and d['sourceCommit']==SOURCE,'TR34_DECISION')
    proposal=a.committed(p.G,COMMIT,'APP013_P08_TR34_OWNER_SIGNIN_PROPOSAL_20261126.md')
    m.need(m.digest(proposal)==d['proposalSha256'],'TR34_PROPOSAL')
    attendance=q.strict_json(a.committed(p.G,COMMIT,'APP013_P08_TR34_OWNER_ATTENDANCE_20261126.json'))
    m.need(attendance['attendanceThrough']=='2026-11-26T16:55:00Z' and attendance['proposalSha256']==d['proposalSha256'],'TR34_ATTENDANCE')
    r=p.renewal_preflight(SOURCE,{'commit':COMMIT,'path':NAME,'sha256':m.digest(raw)},d)
    reviewed=q.strict_json(a.committed(p.G,COMMIT,'APP013_P08_TR34_SOURCE_READINESS_20261126.json'))
    for name,expected in reviewed['sdkAdditionalFiles'].items():m.need(m.digest(Path(name).read_bytes())==expected,'TR34_SIGNIN_SDK')
    m.need(not os.path.lexists(ROOT) and ROOT.parent.resolve()==ROOT.parent,'TR34_ALREADY_RESERVED')
    env=q.sdk_environment(os.environ)
    env['BROWSER']='chrome'
    return d,r,env,acl.config_snapshot(acl.CONFIG_ROOT,os.environ)
def main():
    m.need(sys.argv[1:] in (['--preflight'],['--execute']),'TR34_ARGUMENT')
    d,r,env,config=preflight()
    if sys.argv[1]=='--preflight':
        print(json.dumps({'status':r['status'],'providerCalls':0,'credentialStoresRead':False,'operationReserved':False}));return 0
    cutoff=m.timestamp(d['cutoff']);close=m.timestamp(d['closeoutEnd']);horizon=m.timestamp(d['validThrough'])
    m.need(time.time()<cutoff,'TR34_CUTOFF')
    os.umask(0o077);ROOT.mkdir(mode=0o700)
    fd=os.open(ROOT/'entry.lock',os.O_CREAT|os.O_EXCL|os.O_RDWR|os.O_NOFOLLOW,0o600)
    fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
    io=q.NativeIO(time.time,str(uuid.uuid4()));process=None;cleaning=False;spawning=False;pending_signal=False;started=time.monotonic()
    result={'status':'SIGNIN_UNQUALIFIED','sourceCommit':SOURCE,'decisionCommit':COMMIT,'reservation':d['reservation'],
        'cliReserved':1,'cacheReserved':0,'exitCode':None,'ownedPid':None,'leaderReaped':False,'groupAbsent':False,
        'configurationUnchanged':False,'onTime':False,'outputDisposition':'OS_DEVNULL','validThrough':d['validThrough'],
        'sdkAuthenticationRequestCount':'UNKNOWN','sdkCacheMaintenanceAuthorized':True,'providerResourceRequests':0}
    m.reserve(ROOT/'attempt.json',{'sourceCommit':SOURCE,'decisionCommit':COMMIT,'reservation':d['reservation'],'commandSha256':m.digest(ARGV),'startedAt':time.time()})
    def interrupted(*_):
        nonlocal pending_signal
        if spawning:pending_signal=True
        elif not cleaning:raise m.Stop('INTERRUPTED')
    handlers={sig:signal.signal(sig,interrupted) for sig in (signal.SIGINT,signal.SIGTERM)}
    try:
        last=time.time();m.need(last<cutoff,'TR34_CUTOFF')
        hard=time.monotonic()+min(300,close-last-2)
        spawning=True
        try:
            process=subprocess.Popen(ARGV,cwd=B,env=env,stdin=subprocess.DEVNULL,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,start_new_session=True)
            io.children.add(process);result['ownedPid']=process.pid
        finally:spawning=False
        if pending_signal:raise m.Stop('INTERRUPTED')
        while process.poll() is None:
            now=time.time();m.need(now>=last,'CLOCK_ROLLBACK');last=now
            m.need(now<close-2 and time.monotonic()<hard,'SIGNIN_TIMEOUT')
            time.sleep(.1)
        m.need(time.time()>=last,'CLOCK_ROLLBACK')
        result['exitCode']=process.returncode
    except BaseException as error:
        result['status']='INTERRUPTED' if isinstance(error,(KeyboardInterrupt,SystemExit)) or str(error)=='INTERRUPTED' else 'SIGNIN_UNCONFIRMED'
    finally:
        cleaning=True
        try:closed=io.close(close) is True
        except BaseException:closed=False
        result['leaderReaped']=process is None or process.poll() is not None
        if process is None:result['groupAbsent']=True
        else:
            try:os.killpg(process.pid,0)
            except ProcessLookupError:result['groupAbsent']=True
            except PermissionError:pass
        try:result['configurationUnchanged']=acl.config_snapshot(acl.CONFIG_ROOT,os.environ)==config
        except BaseException:pass
        if closed and result['leaderReaped'] and result['groupAbsent'] and result['configurationUnchanged'] and result['exitCode']==0 and time.time()<close:
            try:
                m.reserve(ROOT/'cache-reservation.json',{'reserved':True,'validThrough':d['validThrough']});result['cacheReserved']=1
                with acl.http_deadline(min(8,close-time.time())):
                    token=acl.read_cached_token(acl.CONFIG_ROOT,horizon)
                    token=None
                result['status']='VALID_THROUGH_CUTOFF'
            except BaseException as error:
                token=None
                code=error.args[0] if isinstance(error,acl.Stop) and len(error.args)==1 else None
                result['status']=code if code in {'CACHED_TOKEN_EXPIRED','CACHED_TOKEN_MISSING','CACHE_BUSY','CACHE_CHANGED','CACHE_JOURNAL_UNSUPPORTED','CACHE_FORMAT_UNSUPPORTED','CACHE_SCHEMA_UNSUPPORTED','TOKEN_EXPIRY_UNKNOWN','TOKEN_RESTRICTION_UNSUPPORTED','CACHE_READ_UNCONFIRMED','HTTP_TIMEOUT'} else 'CACHE_VALIDITY_UNCONFIRMED'
        try:result['configurationUnchanged']=acl.config_snapshot(acl.CONFIG_ROOT,os.environ)==config
        except BaseException:result['configurationUnchanged']=False
        result['elapsedSeconds']=round(time.monotonic()-started,3);result['completedAt']=time.time();result['onTime']=time.time()<close
        result['localResiduals']=[] if closed and result['leaderReaped'] and result['groupAbsent'] and result['configurationUnchanged'] and result['onTime'] else ['LOCAL_CLOSEOUT_UNCONFIRMED']
        m.reserve(ROOT/'result.json',result)
        for sig,handler in handlers.items():signal.signal(sig,handler)
        fcntl.flock(fd,fcntl.LOCK_UN);os.close(fd)
    print(json.dumps(result,sort_keys=True))
    return 0 if result['status']=='VALID_THROUGH_CUTOFF' and not result['localResiduals'] else 2
if __name__=='__main__':
    try:raise SystemExit(main())
    except Exception:
        print('{"status":"TR34_REFUSED_OR_UNCONFIRMED"}');raise SystemExit(2)
