import {test} from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {baselineRef,protectedSections,frozenBaselineErrors,checkFrozenBaseline} from './frozen-baseline-check.mjs';
const baseline=Object.fromEntries(Object.keys(protectedSections).map(file=>[file,execFileSync('git',['show',baselineRef+':'+file],{encoding:'utf8'})]));
const contract='APP013_REMAINING_EXECUTION_CONTRACT.md';
const steel='PAYMENT_BOOKING_TEXT_STEEL_THREAD.md';
test('current checkout passes pinned baseline',()=>assert.deepEqual(checkFrozenBaseline(),[]));
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
