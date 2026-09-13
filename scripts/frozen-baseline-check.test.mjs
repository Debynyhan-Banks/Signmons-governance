import {test} from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {baselineRef,protectedSections,frozenBaselineErrors,checkFrozenBaseline,automaticAdmissionRef,automaticAdmissionRecord,applyAutomaticAdmissionAmendment} from './frozen-baseline-check.mjs';
const original=Object.fromEntries(Object.keys(protectedSections).map(file=>[file,execFileSync('git',['show',baselineRef+':'+file],{encoding:'utf8'})]));
const record=execFileSync('git',['show',automaticAdmissionRef+':'+automaticAdmissionRecord],{encoding:'utf8'});
const baseline=applyAutomaticAdmissionAmendment(original,record);
const contract='APP013_REMAINING_EXECUTION_CONTRACT.md';
const steel='PAYMENT_BOOKING_TEXT_STEEL_THREAD.md';
test('current checkout passes pinned baseline',()=>assert.deepEqual(checkFrozenBaseline(),[]));
test('approved amendment changes exactly two frozen sections and leaves ticket intact',()=>{
  assert.deepEqual(frozenBaselineErrors(baseline,original),[
    '[frozen-criterion] APP013_REMAINING_EXECUTION_CONTRACT.md / 2B — verified intake creates one reviewed job',
    '[frozen-criterion] PAYMENT_BOOKING_TEXT_STEEL_THREAD.md / Section acceptance cards',
  ]);
  assert.equal(baseline['TICKETS/APP-013.md'],original['TICKETS/APP-013.md']);
  assert.deepEqual(frozenBaselineErrors({...baseline},baseline),[]);
});
test('old operator requirement cannot replace adopted automatic admission',()=>{
  assert.equal(frozenBaselineErrors(original,baseline).length,2);
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
