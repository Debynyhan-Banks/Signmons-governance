"""Local-only Chrome preference tests. Never invokes gcloud or credentials."""
import ast
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
import uuid

G=Path(__file__).resolve().parent
B=Path('/Users/debynyhanbanks/Web Projects/signmons-backend-r08-recovery')
TEMPLATE=G/'APP013_P08_CHROME_FIRST_SIGNIN_TEMPLATE_20261126.py'
RESULT=G/'APP013_P08_CHROME_FIRST_SIGNIN_VERIFICATION_20261126.json'
LEASE=Path('/private/tmp/p08-chrome-first-signin-test-20261126.lock')
BASELINE_SHA='911b3a4250198fdd8eb83adf3728ded29174010c36de321e3d21fa75d82c5589'
EXPECTED_SHA='73686cddb7f5f70332155432d82f2d87c325c4a95a4a0bd1c8b717a00866084d'
sys.path.insert(0,str(B/'evidence/APP-013/p08-connected-packet-20261110'))
import packet
import iq1_identity_boundary as identity
import vm2_metadata_read as interruption
q=packet.q
SIGNALS={signal.SIGINT,signal.SIGTERM,signal.SIGHUP}

class Refused(Exception):pass

def need(ok,code):
    if not ok:raise Refused(code)

def save(value):
    temporary=RESULT.with_suffix('.next')
    fd=os.open(temporary,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
    with os.fdopen(fd,'w') as f:json.dump(value,f,indent=2);f.write('\n')
    os.replace(temporary,RESULT)

def record():
    return json.loads(RESULT.read_text()) if RESULT.exists() else {}

def template_environment():
    raw=TEMPLATE.read_text()
    need(hashlib.sha256(raw.encode()).hexdigest()==EXPECTED_SHA,'TEMPLATE_CHANGED')
    new="    env=q.sdk_environment(os.environ)\n    env['BROWSER']='chrome'\n    return d,r,env,acl.config_snapshot(acl.CONFIG_ROOT,os.environ)"
    old="    return d,r,q.sdk_environment(os.environ),acl.config_snapshot(acl.CONFIG_ROOT,os.environ)"
    need(raw.count(new)==1,'ENVIRONMENT_CHANGE_SHAPE')
    need(hashlib.sha256(raw.replace(new,old).encode()).hexdigest()==BASELINE_SHA,'SUPERVISOR_DRIFT')
    tree=ast.parse(raw)
    preflight=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='preflight')
    statements=preflight.body[-3:-1]
    need(len(statements)==2 and all(isinstance(n,ast.Assign) for n in statements),'ENVIRONMENT_AST')
    namespace={'q':q,'os':os}
    original=dict(os.environ)
    exec(compile(ast.Module(body=statements,type_ignores=[]),str(TEMPLATE),'exec'),namespace)
    baseline=q.sdk_environment(os.environ)
    need(namespace['env']=={**baseline,'BROWSER':'chrome'},'ENVIRONMENT_DIFF')
    need(dict(os.environ)==original,'AMBIENT_ENVIRONMENT_CHANGED')
    return namespace['env'],baseline

def require_chrome(value):
    need(value=={'class':'MacOSXOSAScript','name':'google chrome'},'CHROME_CONTROLLER_UNAVAILABLE')

def guarded_attempt(invoke,close):
    value=None;error=None
    try:value=invoke()
    except BaseException as exc:error='INTERRUPTED' if isinstance(exc,(KeyboardInterrupt,SystemExit)) else 'OPENER_TIMEOUT' if isinstance(exc,subprocess.TimeoutExpired) else 'OPENER_UNCONFIRMED'
    finally:closed=close()
    need(closed,'OPENER_CLOSEOUT_UNCONFIRMED')
    need(error is None,error or 'OPENER_UNCONFIRMED')
    return value

def probe(env,timeout=5):
    code="import json,webbrowser;b=webbrowser.get();print(json.dumps({'class':type(b).__name__,'name':b.name}))"
    r=subprocess.run([env['CLOUDSDK_PYTHON'],'-I','-B','-c',code],env=env,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,timeout=timeout,check=True)
    return json.loads(r.stdout)

def local_tests():
    with identity.lease(str(LEASE)):
        return _local_tests()

def _local_tests():
    env,baseline=template_environment();selected=probe(env);require_chrome(selected)
    default=probe(baseline);need(default=={'class':'MacOSXOSAScript','name':'default'},'BASELINE_CONTROLLER')
    rejected=0
    for value in [{'class':'MacOSXOSAScript','name':'default'},{'class':'Missing','name':None}]:
        try:require_chrome(value)
        except Refused:rejected+=1
    need(rejected==2,'UNAVAILABLE_NEGATIVE')
    cleanup_calls=[]
    for exc in [subprocess.TimeoutExpired('synthetic',10),KeyboardInterrupt()]:
        def fail():raise exc
        try:guarded_attempt(fail,lambda:(cleanup_calls.append(True) or True))
        except Refused:pass
        else:raise Refused('NEGATIVE_DID_NOT_STOP')
    need(len(cleanup_calls)==2,'INDEPENDENT_CLEANUP_NEGATIVE')
    boundaries=synthetic_tests()
    existing=record()
    status=existing.get('status','BROWSER_TEST_UNCONFIRMED') if existing.get('browserAttemptReserved') else 'LOCAL_TESTS_PASS_BROWSER_TEST_PENDING'
    existing.update({'status':status,'sourceCommit':'b72ecb89f1907a25c988bbe3f33388bfdab77976','templateSha256':EXPECTED_SHA,'baselineSha256':BASELINE_SHA,'testSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'localVerifiedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cases':{'supervisorOnlyEnvironmentDiff':'PASS','actualSdkEnvironmentDifference':'ONLY_BROWSER_CHROME','ambientEnvironmentUnchanged':'PASS','actualPinnedPythonChromeSelection':selected,'baselineSelection':default,'unavailableAndUnexpectedControllerRefused':2,'injectedTimeoutAndInterruptionCleanup':2,**boundaries},'providerCalls':0,'credentialReads':0,'signinInvoked':False})
    save(existing)
    print(json.dumps({'status':'LOCAL_TESTS_PASS','selectedController':selected,'browserLaunched':False,'providerCalls':0,'credentialReads':0}))

# Reuses the existing Chrome JXA application/tab interfaces. Only IDs and an
# exact synthetic marker comparison leave the script; no other URL is returned.
SNAPSHOT=r'''function run(argv) {
const marker=argv[0]; if(!/^about:blank#p08-chrome-check-[0-9a-f-]{36}$/.test(marker)) throw Error('MARKER');
const app=Application('com.google.Chrome'); const ids=[],matches=[];
if(!app.running()) return JSON.stringify({running:false,ids:[],matches:[]});
for(const w of app.windows()) { const ts=w.tabs(); for(let i=0;i<ts.length;i++) {const t=ts[i]; const row={window:w.id(),tab:t.id()}; ids.push(row); if(t.url()===marker) matches.push({...row,visible:app.frontmost() && w.index()===1 && w.activeTabIndex()===i+1});}}
return JSON.stringify({running:true,ids:ids,matches:matches});}'''
CLOSE=r'''function run(argv) {
const marker=argv[0],wid=String(argv[1]),tid=String(argv[2]);
if(!/^about:blank#p08-chrome-check-[0-9a-f-]{36}$/.test(marker) || !/^[1-9][0-9]{0,19}$/.test(wid) || !/^[1-9][0-9]{0,19}$/.test(tid)) throw Error('OWNERSHIP');
const app=Application('com.google.Chrome'); let found=[];
if(app.running()) for(const w of app.windows()) for(const t of w.tabs()) if(String(w.id())===wid && String(t.id())===tid && t.url()===marker) found.push(t);
if(found.length!==1) throw Error('OWNERSHIP'); found[0].close(); return 'CLOSED';}'''

def jxa(script,args,timeout):
    r=None
    try:
        r=subprocess.run(['/usr/bin/osascript','-l','JavaScript','-e',script,*args],stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=timeout,check=False)
        if r.returncode:
            error=r.stderr.decode('utf-8','replace')
            code='AUTOMATION_DENIED' if re.search(r'(?<!\d)-1743(?!\d)',error) else 'APP_NOT_RUNNING' if re.search(r'(?<!\d)-600(?!\d)',error) else 'SCRIPT_UNCONFIRMED'
            error=None
            raise Refused(code)
        need(len(r.stdout)<=65536,'SCRIPT_OUTPUT_UNCONFIRMED')
        return r.stdout.decode().strip()
    finally:r=None

def snapshot(marker,timeout):return json.loads(jxa(SNAPSHOT,[marker],timeout))

def own_match(observed,before):
    rows=observed['matches'];prior={(r['window'],r['tab']) for r in before['ids']}
    need(len(rows)==1,'OWNED_TAB_UNCONFIRMED')
    row=rows[0];need((row['window'],row['tab']) not in prior,'TAB_PREEXISTED')
    return row

def pending():
    need(not interruption.INTERRUPTED.get(),'INTERRUPTED')

def bounded_timeout(end,maximum):
    remaining=end-time.monotonic()
    need(remaining>0,'BROWSER_TEST_DEADLINE')
    return min(maximum,remaining)

def worker_result(output):
    need(type(output) is bytes and len(output)<=8192,'OPENER_OUTPUT_UNCONFIRMED')
    # A harmless osascript status line can precede the worker's own final JSON.
    # Only the final fixed-shape Boolean is consumed; earlier text is discarded.
    try:value=json.loads(output.splitlines()[-1])
    except (ValueError,IndexError):raise Refused('OPENER_OUTPUT_UNCONFIRMED') from None
    need(type(value) is dict and set(value)=={'opened'} and type(value['opened']) is bool,'OPENER_OUTPUT_UNCONFIRMED')
    return value

def _browser_attempt(start,overall):
    r=record();need(r.get('templateSha256')==EXPECTED_SHA and r.get('cases'),'LOCAL_TESTS_REQUIRED')
    need(r.get('testSha256')==hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'LOCAL_TESTS_STALE')
    need(not r.get('browserAttemptReserved'),'BROWSER_ATTEMPT_CONSUMED')
    pending();env,_=template_environment();pending()
    require_chrome(probe(env,bounded_timeout(overall,5)));pending()
    marker='about:blank#p08-chrome-check-'+str(uuid.uuid4())
    before=snapshot(marker,bounded_timeout(overall,5));pending();need(not before['matches'],'MARKER_PREEXISTED')
    r['browserAttemptReserved']=True;r['browserAttemptStartedAt']=datetime.datetime.now(datetime.timezone.utc).isoformat();save(r)
    result={'status':'UNCONFIRMED','controller':'chrome','openerInvocations':0,'ownedTabClosed':False,'preexistingTabsPreserved':False,'ownedProcessGroupAbsent':False,'rawUrlRetained':False}
    io=None;process=None;owned=None
    worker="import json,re,sys,webbrowser;u=sys.argv[1];assert re.fullmatch(r'about:blank#p08-chrome-check-[0-9a-f-]{36}',u);b=webbrowser.get();assert type(b).__name__=='MacOSXOSAScript' and b.name=='google chrome';print(json.dumps({'opened':b.open(u,new=1,autoraise=True)}),flush=True)"
    def invoke():
        nonlocal process
        pending();deadline=time.monotonic()+bounded_timeout(overall,10)
        result['openerInvocations']+=1
        process=subprocess.Popen([env['CLOUDSDK_PYTHON'],'-I','-B','-c',worker,marker],env=env,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,start_new_session=True)
        # Flag-only handlers cannot interrupt the Popen-to-registration interval.
        io.children.add(process)
        pending();output=None
        try:
            output,_=process.communicate(timeout=bounded_timeout(deadline,10))
            pending();need(process.returncode==0,'OPENER_EXIT_UNCONFIRMED')
            return worker_result(output)
        finally:output=None
    def close_worker():
        closed=io is None or io.close(time.time()+min(20,max(0,overall-time.monotonic()))) is True
        absent=process is None and result['openerInvocations']==0
        if process is not None:
            try:os.killpg(process.pid,0)
            except ProcessLookupError:absent=True
            except OSError:absent=False
        result['ownedProcessGroupAbsent']=absent and (process is None or process.poll() is not None)
        return closed and result['ownedProcessGroupAbsent']
    try:
        pending();io=q.NativeIO(time.time,str(uuid.uuid4()))
        opened=guarded_attempt(invoke,close_worker);need(opened=={'opened':True},'BROWSER_NOT_OPENED')
        pending()
        end=min(overall,time.monotonic()+20)
        while time.monotonic()<end:
            pending();observed=snapshot(marker,bounded_timeout(end,5));pending()
            if observed['matches']:
                owned=own_match(observed,before)
                if owned['visible']:break
            time.sleep(bounded_timeout(end,.2))
        pending()
        need(owned is not None and owned['visible'],'VISIBLE_TAB_UNCONFIRMED')
        result['status']='VISIBLE_CHROME_BLANK_PAGE_CONFIRMED'
    except BaseException as exc:
        result['failureCode']=str(exc) if isinstance(exc,Refused) else type(exc).__name__
    finally:
        cleanup_end=min(overall,time.monotonic()+20)
        try:
            if not result['openerInvocations']:result['ownedProcessGroupAbsent']=True
            observed=snapshot(marker,bounded_timeout(cleanup_end,5))
            if observed['matches']:
                owned=own_match(observed,before)
                need(jxa(CLOSE,[marker,str(owned['window']),str(owned['tab'])],bounded_timeout(cleanup_end,5))=='CLOSED','CLOSE_UNCONFIRMED')
            after=snapshot(marker,bounded_timeout(cleanup_end,5))
            result['ownedTabClosed']=not after['matches']
            result['preexistingTabsPreserved']={(x['window'],x['tab']) for x in before['ids']}<={(x['window'],x['tab']) for x in after['ids']}
        except BaseException as exc:
            safe_codes={'AUTOMATION_DENIED','APP_NOT_RUNNING','SCRIPT_UNCONFIRMED','SCRIPT_OUTPUT_UNCONFIRMED',
                        'OWNED_TAB_UNCONFIRMED','TAB_PREEXISTED','CLOSE_UNCONFIRMED','BROWSER_TEST_DEADLINE'}
            result['cleanupFailureCode']=(exc.args[0] if type(exc) is Refused and len(exc.args)==1 and
                type(exc.args[0]) is str and exc.args[0] in safe_codes else type(exc).__name__)
        result['withinOverallBound']=time.monotonic()<overall
        result['elapsedSeconds']=round(time.monotonic()-start,3)
        result['cleanupVerified']=all(result[k] for k in ['ownedTabClosed','preexistingTabsPreserved','ownedProcessGroupAbsent','withinOverallBound'])
        r['browserProof']=result;r['browserVerifiedAt']=datetime.datetime.now(datetime.timezone.utc).isoformat();r['status']='LOCAL_CHROME_FIRST_VERIFIED' if result['status']=='VISIBLE_CHROME_BLANK_PAGE_CONFIRMED' and result['cleanupVerified'] else 'BROWSER_TEST_UNCONFIRMED'
    return r

def veto_interruption(r):
    r['status']='BROWSER_TEST_UNCONFIRMED'
    r['browserProof'].update(status='UNCONFIRMED',failureCode='INTERRUPTED',interrupted=True)

def check_completion_deadline(r,start,overall):
    if time.monotonic()>=overall:
        r['status']='BROWSER_TEST_UNCONFIRMED'
        r['browserProof'].update(status='UNCONFIRMED',withinOverallBound=False,
            cleanupVerified=False,failureCode='BROWSER_TEST_DEADLINE',elapsedSeconds=round(time.monotonic()-start,3))

def browser_once():
    # Includes environment/controller probes and the initial tab snapshot.
    start=time.monotonic();overall=start+60;previous_mask=None
    with identity.lease(str(LEASE)):
        try:
            with interruption.interruption_handlers():
                r=_browser_attempt(start,overall)
                previous_mask=signal.pthread_sigmask(signal.SIG_BLOCK,SIGNALS)
                check_completion_deadline(r,start,overall)
                if interruption.INTERRUPTED.get() or signal.sigpending()&SIGNALS:veto_interruption(r)
                save(r)
                check_completion_deadline(r,start,overall)
                if interruption.INTERRUPTED.get() or signal.sigpending()&SIGNALS:veto_interruption(r)
                if r['status']!='LOCAL_CHROME_FIRST_VERIFIED':save(r)
            # Restore original handlers before completing/publicizing the test.
            if signal.sigpending()&SIGNALS:veto_interruption(r);save(r)
        finally:
            if previous_mask is not None:signal.pthread_sigmask(signal.SIG_SETMASK,previous_mask)
    result=r['browserProof']
    print(json.dumps({'status':r['status'],'browserProof':result,'providerCalls':0,'credentialReads':0,'signinInvoked':False}))
    return 0 if r['status']=='LOCAL_CHROME_FIRST_VERIFIED' else 2

def synthetic_tests():
    """Actual lease/handler/owned-child paths; every browser interface is injected."""
    import copy
    import tempfile
    from unittest.mock import patch
    selected={'class':'MacOSXOSAScript','name':'google chrome'}
    default={'class':'MacOSXOSAScript','name':'default'}
    cases=0
    # Execute the exact production CLOSE text in a JavaScript VM with an inert
    # Application object. No osascript or browser is invoked by these cases.
    close_harness=r'''
const vm=require('node:vm'),fs=require('node:fs');
const script=JSON.parse(fs.readFileSync(0,'utf8')).script;
const marker='about:blank#p08-chrome-check-00000000-0000-4000-8000-000000000001';
const row=(w,t,url=marker)=>({w,t,url});
const one=(w,t)=>[row(w,t)];
const cases=[
 {tabs:one(2,20),args:[marker,'2','20'],ok:true},
 {tabs:one('2','20'),args:[marker,'2','20'],ok:true},
 {tabs:one('2',20),args:[marker,'2','20'],ok:true},
 {tabs:one(2,'20'),args:[marker,2,20],ok:true},
 {tabs:one(2,20),args:[marker,'3','20'],ok:false},
 {tabs:one(2,20),args:[marker,'2','21'],ok:false},
 {tabs:[row(2,20,'about:blank#other')],args:[marker,'2','20'],ok:false},
 {tabs:[row(2,20),row('2','20')],args:[marker,'2','20'],ok:false},
 {tabs:[],args:[marker,'2','20'],ok:false},
 {tabs:one(2,20),args:[marker,'2','20'],running:false,ok:false},
 {tabs:one(2,20),args:['about:blank#wrong','2','20'],ok:false},
 {tabs:one(2,20),args:[marker,'02','20'],ok:false},
 {tabs:one(2,20),args:[marker,'2','0'],ok:false},
 {tabs:one(2,20),args:[marker,'-2','20'],ok:false},
 {tabs:one(2,20),args:[marker,'2.0','20'],ok:false},
 {tabs:one(2,20),args:[marker,true,'20'],ok:false},
 {tabs:one(2,20),args:[marker,'2',null],ok:false},
 {tabs:one(2,20),args:[marker,'2','100000000000000000000'],ok:false}
];
for(const test of cases){
 const closed=[];
 const tabs=[...test.tabs,row(1,10,'about:blank#preexisting')];
 const app={running:()=>test.running!==false,windows:()=>tabs.map((r,index)=>({
   id:()=>r.w,tabs:()=>[{id:()=>r.t,url:()=>r.url,close:()=>closed.push(index)}]
 }))};
 let value,error;
 try{value=vm.runInNewContext(script+'\nrun(args)',{
   args:test.args,Application:name=>{if(name!=='com.google.Chrome')throw Error('APP_SCOPE');return app;}
 },{timeout:500});}catch(exc){error=exc.message;}
 if(test.ok){if(value!=='CLOSED'||error||JSON.stringify(closed)!=='[0]')throw Error('OWNED_CLOSE_FAILED');}
 else if(error!=='OWNERSHIP'||closed.length)throw Error('UNOWNED_CLOSE_NOT_REFUSED');
}
console.log(JSON.stringify({passed:cases.length,closedOnlyOwned:true}));
'''
    close_run=subprocess.run(['/Users/debynyhanbanks/.nvm/versions/node/v24.12.0/bin/node','-e',close_harness],
        input=json.dumps({'script':CLOSE}),text=True,capture_output=True,timeout=5,check=True)
    close_cases=json.loads(close_run.stdout)
    need(close_cases=={'passed':18,'closedOnlyOwned':True},'EXACT_CLOSE_SCRIPT_REGRESSION')
    cases+=close_cases['passed']
    before={'running':True,'ids':[{'window':1,'tab':10}],'matches':[]}
    for rows in ([],[{'window':1,'tab':10,'visible':True}],
                 [{'window':2,'tab':20,'visible':True}]*2):
        try:own_match({'matches':rows},before)
        except Refused:cases+=1
        else:raise Refused('OWNERSHIP_NEGATIVE_FAILED')
    need(own_match({'matches':[{'window':1,'tab':20,'visible':True}]},before)['tab']==20,'OWNED_NEW_TAB')
    cases+=1
    need(worker_result(b'harmless osascript status\n{"opened":true}\n')=={'opened':True},'WORKER_FINAL_JSON')
    for output in (b'{"opened":1}',b'PRIVATE_SENTINEL',b'{"opened":true,"url":"PRIVATE_SENTINEL"}'):
        try:worker_result(output)
        except Refused:cases+=1
        else:raise Refused('WORKER_OUTPUT_NEGATIVE_FAILED')
    for error,code in [(b'PRIVATE_SENTINEL (-1743)','AUTOMATION_DENIED'),
                       (b'PRIVATE_SENTINEL (-600)','APP_NOT_RUNNING'),
                       (b'PRIVATE_SENTINEL','SCRIPT_UNCONFIRMED')]:
        with patch.object(subprocess,'run',return_value=subprocess.CompletedProcess([],1,b'',error)):
            try:jxa(SNAPSHOT,[],1)
            except Refused as exc:need(str(exc)==code,'SCRIPT_ERROR_CLASSIFICATION');cases+=1
            else:raise Refused('SCRIPT_ERROR_NEGATIVE_FAILED')

    real_popen=subprocess.Popen;real_monotonic=time.monotonic
    def exercise(*,registration_signal=None,publication_signal=False,held=False,preexisting=False,save_failure=False,fail_spawn=False,publication_delay=False):
        with tempfile.TemporaryDirectory(prefix='p08-chrome-synthetic-',dir='/private/tmp') as temp:
            target=Path(temp)/'result.json';lock=Path(temp)/'lease'
            initial={'templateSha256':EXPECTED_SHA,'testSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':{'synthetic':True}}
            target.write_text(json.dumps(initial));os.chmod(target,0o600)
            state={'opened':False,'closed':False,'calls':0,'closeCalls':0,'processes':[],'published':False,'delay':0.}
            handlers={s:signal.getsignal(s) for s in SIGNALS};mask=signal.pthread_sigmask(signal.SIG_BLOCK,set())
            env={'CLOUDSDK_PYTHON':sys.executable,'BROWSER':'chrome'}
            def fake_snapshot(marker,timeout):
                state['marker']=marker;need(0<timeout<=5,'SNAPSHOT_BOUND')
                value=copy.deepcopy(before)
                if state['opened'] and not state['closed']:
                    row={'window':1 if preexisting else 2,'tab':10 if preexisting else 20,'visible':True}
                    value['matches']=[row]
                    if not preexisting:value['ids'].append({'window':2,'tab':20})
                return value
            def close_tab(script,args,timeout):
                need(script==CLOSE and args==[state['marker'],'2','20'] and 0<timeout<=5,'OWNED_CLOSE_SCOPE')
                state['closeCalls']+=1;state['closed']=True;return 'CLOSED'
            def spawn(argv,**kwargs):
                need(argv[-1]==state['marker'] and 'webbrowser' in argv[-2],'SYNTHETIC_WORKER_BOUNDARY')
                state['calls']+=1
                if fail_spawn:raise OSError('SYNTHETIC_SPAWN_FAILURE')
                state['opened']=True
                code='import time;time.sleep(30)' if registration_signal else 'print("harmless status");print(\'{"opened":true}\')'
                process=real_popen([sys.executable,'-I','-B','-c',code],**kwargs)
                state['processes'].append(process)
                if registration_signal:
                    signal.getsignal(registration_signal)(registration_signal,None)
                return process
            original_save=save
            def store(value):
                if save_failure and 'browserProof' in value:raise OSError('SYNTHETIC_SAVE_FAILURE')
                original_save(value)
                if publication_delay and 'browserProof' in value:state['delay']=61.
                if publication_signal and 'browserProof' in value and not state['published']:
                    state['published']=True;signal.getsignal(signal.SIGTERM)(signal.SIGTERM,None)
            def published(*args,**kwargs):
                need(all(signal.getsignal(s)==h for s,h in handlers.items()),'HANDLER_NOT_RESTORED')
                need(signal.pthread_sigmask(signal.SIG_BLOCK,set())==mask,'MASK_NOT_RESTORED')
            with (patch.dict(globals(),{'RESULT':target,'LEASE':lock}),
                  patch.dict(globals(),{'template_environment':lambda:(env,{}),'probe':lambda *args:selected,
                                       'snapshot':fake_snapshot,'jxa':close_tab,'save':store}),
                  patch.object(time,'monotonic',lambda:real_monotonic()+state['delay']),
                  patch.object(subprocess,'Popen',spawn),patch('builtins.print',published)):
                try:
                    if held:
                        with identity.lease(str(lock)):
                            try:browser_once()
                            except identity.Stop:pass
                            else:raise Refused('LEASE_RACE_NOT_REFUSED')
                        need(state['calls']==0 and record()==initial,'LEASE_RACE_DISPATCH')
                        return
                    if save_failure:
                        try:browser_once()
                        except OSError:pass
                        else:raise Refused('SAVE_FAILURE_NOT_PROPAGATED')
                    else:
                        code=browser_once();saved=record();bad=bool(registration_signal or publication_signal or preexisting or fail_spawn or publication_delay)
                        need(code==(2 if bad else 0),'SYNTHETIC_RESULT')
                        need(saved['browserAttemptReserved'] is True and state['calls']==1,'ONCE_RESERVATION')
                        need(saved['browserProof']['ownedProcessGroupAbsent'] is (not fail_spawn),'OWNED_PROCESS_ABSENCE')
                        need(state['closeCalls']==(0 if preexisting or fail_spawn else 1),'OWNED_TAB_ISOLATION')
                        if preexisting:need(saved['browserProof']['cleanupFailureCode']=='TAB_PREEXISTED','SAFE_CLEANUP_REFUSAL_CODE')
                        if publication_delay:need(saved['browserProof']['withinOverallBound'] is False,'PUBLICATION_DEADLINE')
                        if registration_signal or publication_signal:
                            need(saved['browserProof']['interrupted'] is True,'INTERRUPTION_VETO')
                        try:browser_once()
                        except Refused as exc:need(str(exc)=='BROWSER_ATTEMPT_CONSUMED','CONSUMED_CODE')
                        else:raise Refused('REPLAY_NOT_REFUSED')
                        # Local checks may refresh their own evidence but cannot erase
                        # the consumed browser flag or replace the browser outcome.
                        old_status=saved['status']
                        with (patch.dict(globals(),{'synthetic_tests':lambda:{},'probe':lambda e,*args:selected if e.get('BROWSER') else default}),
                              patch('builtins.print')):
                            _local_tests()
                        need(record()['browserAttemptReserved'] is True and record()['status']==old_status,'LOCAL_TEST_RESET_ATTEMPT')
                finally:
                    need(all(signal.getsignal(s)==h for s,h in handlers.items()),'HANDLER_NOT_RESTORED')
                    need(signal.pthread_sigmask(signal.SIG_BLOCK,set())==mask,'MASK_NOT_RESTORED')
                    for process in state['processes']:
                        need(process.poll() is not None,'SYNTHETIC_CHILD_NOT_REAPED')
                        try:os.killpg(process.pid,0)
                        except ProcessLookupError:pass
                        else:raise Refused('SYNTHETIC_CHILD_GROUP_REMAINS')
    exercise();cases+=1
    exercise(held=True);cases+=1
    exercise(preexisting=True);cases+=1
    for sig in SIGNALS:exercise(registration_signal=sig);cases+=1
    exercise(publication_signal=True);cases+=1
    exercise(save_failure=True);cases+=1
    exercise(fail_spawn=True);cases+=1
    exercise(publication_delay=True);cases+=1
    # The full deadline starts before the environment/controller probe.
    with tempfile.TemporaryDirectory(prefix='p08-chrome-deadline-',dir='/private/tmp') as temp:
        target=Path(temp)/'result.json';target.write_text(json.dumps({'templateSha256':EXPECTED_SHA,'testSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':{'synthetic':True}}));clock=[0.]
        def late_environment():clock[0]=61.;return {},{}
        with (patch.dict(globals(),{'RESULT':target,'LEASE':Path(temp)/'lease','template_environment':late_environment}),
              patch.object(time,'monotonic',lambda:clock[0]),patch.dict(globals(),{'probe':lambda *_:(_ for _ in ()).throw(AssertionError('PROBE_AFTER_DEADLINE'))})):
            try:browser_once()
            except Refused as exc:need(str(exc)=='BROWSER_TEST_DEADLINE','WHOLE_OPERATION_DEADLINE')
            else:raise Refused('DEADLINE_NOT_REFUSED')
            need(not record().get('browserAttemptReserved'),'DEADLINE_RESERVED_BROWSER')
    cases+=1
    return {'injectedBoundaryCases':cases,'actualInertChildrenNoBrowser':8,
            'exactCloseJxaNumericStringIdsAndRefusals':close_cases['passed'],'cleanupRefusalCodePreserved':'PASS',
            'leaseRaceAndConsumedReplay':'PASS','flagOnlyRegistrationIntTermHup':'PASS',
            'latePublicationVetoAndHandlerRestoration':'PASS','preexistingTabNeverClosed':'PASS',
            'localChecksPreserveBrowserAttempt':'PASS','wholeOperationDeadline':'PASS','safeJxaFailureClassification':'PASS'}

if __name__=='__main__':
    if sys.argv[1:]==['--local-tests']:local_tests()
    elif sys.argv[1:]==['--browser-once']:raise SystemExit(browser_once())
    else:raise SystemExit('Use --local-tests or one approved --browser-once; no sign-in mode exists.')
