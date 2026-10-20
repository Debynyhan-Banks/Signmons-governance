import {test} from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {baselineRef,protectedSections,frozenBaselineErrors,checkFrozenBaseline,automaticAdmissionRef,automaticAdmissionRecord,applyAutomaticAdmissionAmendment,coreReleaseRef,coreReleasePatch,applyCoreReleaseAmendment} from './frozen-baseline-check.mjs';
const original=Object.fromEntries(Object.keys(protectedSections).map(file=>[file,execFileSync('git',['show',baselineRef+':'+file],{encoding:'utf8'})]));
const record=execFileSync('git',['show',automaticAdmissionRef+':'+automaticAdmissionRecord],{encoding:'utf8'});
const automaticBaseline=applyAutomaticAdmissionAmendment(original,record);
const corePatch=execFileSync('git',['show',coreReleaseRef+':'+coreReleasePatch],{encoding:'utf8'});
const baseline=applyCoreReleaseAmendment(automaticBaseline,corePatch);
const contract='APP013_REMAINING_EXECUTION_CONTRACT.md';
const steel='PAYMENT_BOOKING_TEXT_STEEL_THREAD.md';
test('current checkout passes pinned baseline',()=>assert.deepEqual(checkFrozenBaseline(),[]));
test('automatic-admission amendment changes exactly two frozen sections and leaves ticket intact',()=>{
  assert.deepEqual(frozenBaselineErrors(automaticBaseline,original),[
    '[frozen-criterion] APP013_REMAINING_EXECUTION_CONTRACT.md / 2B — verified intake creates one reviewed job',
    '[frozen-criterion] PAYMENT_BOOKING_TEXT_STEEL_THREAD.md / Section acceptance cards',
  ]);
  assert.equal(automaticBaseline['TICKETS/APP-013.md'],original['TICKETS/APP-013.md']);
  assert.deepEqual(frozenBaselineErrors({...automaticBaseline},automaticBaseline),[]);
});
test('old operator requirement cannot replace adopted automatic admission',()=>{
  assert.equal(frozenBaselineErrors(original,automaticBaseline).length,2);
});
test('core-release amendment changes exactly the approved two frozen sections',()=>{
  const expected=[
    '[frozen-criterion] APP013_REMAINING_EXECUTION_CONTRACT.md / Reporting and remaining MVP boundary',
    '[frozen-criterion] TICKETS/APP-013.md / Acceptance Criteria (must all pass)',
  ];
  assert.deepEqual(frozenBaselineErrors(baseline,automaticBaseline),expected);
  assert.deepEqual(frozenBaselineErrors(automaticBaseline,baseline),expected);
  assert.equal(baseline[steel],automaticBaseline[steel]);
  const before=automaticBaseline['TICKETS/APP-013.md'].match(/^- \[[ xX]\] .+$/gm);
  const after=baseline['TICKETS/APP-013.md'].match(/^- \[[ xX]\] .+$/gm);
  assert.equal(before.length,12);
  assert.equal(after.length,12);
  assert.deepEqual(after.flatMap((line,index)=>line===before[index]?[]:[index]),[1,2,3,5,6,8]);
  for(const title of protectedSections[contract].filter(title=>title!=='Reporting and remaining MVP boundary')) {
    const change=baseline[contract].replace('## '+title,'## '+title+' changed');
    assert.ok(frozenBaselineErrors({...baseline,[contract]:change},baseline).length);
  }
});
test('core-release proposal refuses malformed data and missing or duplicated targets',()=>{
  for(const patch of ['',undefined,corePatch+'\n',corePatch.replace('independent channel consent','optional consent'),corePatch.replace('--- a/TICKETS/APP-013.md','--- a/TICKETS/OTHER.md')])
    assert.throws(()=>applyCoreReleaseAmendment(automaticBaseline,patch));
  assert.throws(()=>applyCoreReleaseAmendment({...automaticBaseline,[contract]:''},corePatch));
  assert.throws(()=>applyCoreReleaseAmendment({...automaticBaseline,[contract]:automaticBaseline[contract]+automaticBaseline[contract]},corePatch));
  assert.throws(()=>applyCoreReleaseAmendment({...automaticBaseline,['TICKETS/APP-013.md']:automaticBaseline['TICKETS/APP-013.md'].replace('- [ ] Notification events are auditable.','')},corePatch));
  assert.throws(()=>applyCoreReleaseAmendment({...automaticBaseline,['TICKETS/APP-013.md']:automaticBaseline['TICKETS/APP-013.md']+automaticBaseline['TICKETS/APP-013.md']},corePatch));
});
test('core-release amendment retains consent, delivery, privacy, audit and downstream safeguards',()=>{
  const ticket='TICKETS/APP-013.md';
  for(const phrase of ['independent channel consent','private management action','safe recovery without blind resend','Sensitive data is redacted per role boundaries.','Notification events are auditable.']) {
    assert.ok(baseline[ticket].includes(phrase));
    assert.ok(frozenBaselineErrors({...baseline,[ticket]:baseline[ticket].replace(phrase,'optional')},baseline).length);
  }
  for(const phrase of ['2B accepted','exactly one job','No merge, deployment, migration, IAM/secrets, charges']) {
    assert.ok(baseline[contract].includes(phrase));
    assert.ok(frozenBaselineErrors({...baseline,[contract]:baseline[contract].replace(phrase,'optional')},baseline).length);
  }
});
test('amendment does not permit weakening service or downstream authority',()=>{
  for(const phrase of ['routine operator approval is not required','without bypassing mandatory verification or policy','no payment, booking, dispatch or send authority']) {
    assert.ok(baseline[contract].includes(phrase));
    assert.ok(frozenBaselineErrors({...baseline,[contract]:baseline[contract].replace(phrase,'unrestricted authority')},baseline).length);
  }
});
test('malformed amendment and missing or duplicate targets fail closed',()=>{
  assert.throws(()=>applyAutomaticAdmissionAmendment(original,''));
  assert.throws(()=>applyAutomaticAdmissionAmendment({...original,[contract]:''},record));
  assert.throws(()=>applyAutomaticAdmissionAmendment({...original,[contract]:original[contract]+original[contract]},record));
});
test('changing acceptance text is rejected without editing repositories',()=>{
  const current={...baseline,[contract]:baseline[contract].replace('exactly one job','exactly two jobs')};
  assert.ok(frozenBaselineErrors(current,baseline).some(e=>e.includes('frozen-criterion')));
});
test('changing section dependency is rejected',()=>{
  const current={...baseline,[contract]:baseline[contract].replace('**Entry:** 2B accepted','**Entry:** 2B optional')};
  assert.ok(frozenBaselineErrors(current,baseline).length);
});
test('new section cannot silently increase denominator',()=>{
  assert.ok(frozenBaselineErrors({...baseline,[contract]:baseline[contract]+'\n## 3E — extra section\nNew work\n'},baseline).length);
});
test('reordering or renaming section is rejected',()=>{
  assert.ok(frozenBaselineErrors({...baseline,[contract]:baseline[contract].replace('## 3A —','## 3Z —')},baseline).length);
});
test('missing and duplicate protected section refuse',()=>{
  assert.ok(frozenBaselineErrors({...baseline,[contract]:''},baseline).length);
  assert.ok(frozenBaselineErrors({...baseline,[contract]:baseline[contract]+'\n## Authority and fixed scope\n'},baseline).length);
});
test('ticket criterion mutation is rejected, checkbox evidence change permitted',()=>{
  const file='TICKETS/APP-013.md';
  assert.ok(frozenBaselineErrors({...baseline,[file]:baseline[file].replace('Notification events are auditable.','Notification events need not be auditable.')},baseline).length);
  assert.deepEqual(frozenBaselineErrors({...baseline,[file]:baseline[file].replace('- [ ] Notification events are auditable.','- [x] Notification events are auditable.')},baseline),[]);
});
test('status/evidence outside frozen requirements can be updated',()=>{
  assert.deepEqual(frozenBaselineErrors({...baseline,[steel]:baseline[steel]+'\n## Evidence update\nNew evidence SHA, no requirement change.\n'},baseline),[]);
});
test('missing pinned history fails closed',()=>{
  assert.ok(checkFrozenBaseline('/nonexistent-signmons-baseline-test').some(e=>e.includes('frozen-unavailable')));
});
test('missing immutable core-release proposal fails closed even when older pins are available',()=>{
  const source=`
    import childProcess from 'node:child_process';
    import {syncBuiltinESMExports} from 'node:module';
    const real=childProcess.execFileSync;
    const seen=[];
    childProcess.execFileSync=(command,args,options)=>{
      if(command==='git' && args[0]==='show') {
        seen.push(args[1]);
        if(args[1]===${JSON.stringify(coreReleaseRef+':'+coreReleasePatch)}) throw Error('missing core proposal history');
      }
      return real(command,args,options);
    };
    syncBuiltinESMExports();
    const {checkFrozenBaseline}=await import(${JSON.stringify(new URL('./frozen-baseline-check.mjs',import.meta.url).href)});
    process.stdout.write(JSON.stringify({errors:checkFrozenBaseline(),seen}));
  `;
  const output=JSON.parse(execFileSync(process.execPath,['--input-type=module','-e',source],{encoding:'utf8'}));
  assert.ok(output.seen.includes(automaticAdmissionRef+':'+automaticAdmissionRecord));
  assert.ok(output.seen.includes(coreReleaseRef+':'+coreReleasePatch));
  assert.deepEqual(output.errors,['[frozen-unavailable] Required files or pinned Git revision unavailable. Fetch history; do not skip or regenerate the baseline.']);
});
