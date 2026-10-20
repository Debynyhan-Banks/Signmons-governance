import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

// Owner-requested baseline freeze. Never move this anchor merely to pass CI.
// A dedicated owner-approved change record and old/new review is required.
export const baselineRef = '57ca1cf0f12ed79075b6afd4781bf28be5e36abc';
// Owner reviewed this exact old/new record, then authorized adoption with "proceed".
// Keep the original freeze; apply ONLY the two replacements from this immutable record.
export const automaticAdmissionRef = '872795c57d2a3a7def07f9822c67664d8cc01d60';
export const automaticAdmissionRecord = 'APP013_2B_AUTOMATIC_ADMISSION_CHANGE.md';
export function applyAutomaticAdmissionAmendment(baseline, record) {
  const blocks = [...record.matchAll(/^(Old|New):\n> (.+)$/gm)];
  if (blocks.length !== 4 || blocks.map(m=>m[1]).join(',') !== 'Old,New,Old,New')
    throw Error('invalid approved amendment');
  const result = {...baseline};
  ['APP013_REMAINING_EXECUTION_CONTRACT.md', 'PAYMENT_BOOKING_TEXT_STEEL_THREAD.md'].forEach((file,i)=>{
    const oldText = blocks[i*2][2], newText = blocks[i*2+1][2];
    if (typeof result[file] !== 'string' || result[file].split(oldText).length !== 2)
      throw Error('approved amendment target missing or duplicated');
    result[file] = result[file].replace(oldText,newText);
  });
  return result;
}
// The owner reviewed the exact proposal at this immutable revision and approved
// adoption on October 20, 2026. This supplements, never replaces, both older pins.
// Only six APP-013 criterion lines and the remaining-MVP paragraph are amended.
export const coreReleaseRef = '7ed300a1d4f50a9a53500db405c3290130bd43cf';
export const coreReleasePatch = 'MVP_CORE_RELEASE_PROPOSED_DIFF_20261020.patch';
const coreReleasePatchSha256 = '0a221591289ae7a5a72a64f4c8ee19b1943d7c2b383d399008e44252431318be';
const coreReleaseFrozenChanges = [
  '[frozen-criterion] APP013_REMAINING_EXECUTION_CONTRACT.md / Reporting and remaining MVP boundary',
  '[frozen-criterion] TICKETS/APP-013.md / Acceptance Criteria (must all pass)',
];
export function applyCoreReleaseAmendment(baseline, patch) {
  if (typeof patch !== 'string' || createHash('sha256').update(patch).digest('hex') !== coreReleasePatchSha256)
    throw Error('invalid pinned core-release proposal');
  const result = {...baseline};
  const changes = [];
  for (const [file,title,count] of [
    ['TICKETS/APP-013.md','Acceptance Criteria (must all pass)',6],
    ['APP013_REMAINING_EXECUTION_CONTRACT.md','Reporting and remaining MVP boundary',1],
  ]) {
    const fileBlocks = patch.split(/(?=^--- a\/)/m).filter(block=>block.startsWith('--- a/'+file+'\n+++ b/'+file+'\n'));
    if (fileBlocks.length !== 1) throw Error('missing or duplicated core-release file');
    const hunks = fileBlocks[0].split(/(?=^@@ )/m).slice(1);
    const targetHunks = hunks.filter(hunk=>file.startsWith('TICKETS/')
      ? hunk.includes('\n ## '+title+'\n')
      : hunk.includes('\n-After 3D, reconcile remaining APP-013\'s twelve criteria,'));
    if (targetHunks.length !== 1) throw Error('missing or duplicated core-release hunk');
    const removed = [...targetHunks[0].matchAll(/^-(.+)$/gm)].map(match=>match[1]);
    const added = [...targetHunks[0].matchAll(/^\+(.+)$/gm)].map(match=>match[1]);
    if (removed.length !== count || added.length !== count || new Set(removed).size !== count || new Set(added).size !== count)
      throw Error('invalid core-release replacement count');
    if (file.startsWith('TICKETS/') && [...removed,...added].some(line=>!line.startsWith('- [ ] ')))
      throw Error('core-release replacements must preserve criterion positions');
    removed.forEach((oldText,index)=>{
      if (typeof result[file] !== 'string' || result[file].split(oldText).length !== 2)
        throw Error('core-release target missing or duplicated');
      result[file] = result[file].replace(oldText,added[index]);
      changes.push({file,oldText,newText:added[index]});
    });
  }
  const ticket = 'TICKETS/APP-013.md';
  for (const text of [baseline[ticket],result[ticket]]) {
    if (section(text,'Acceptance Criteria (must all pass)').split('\n').filter(line=>line.startsWith('- [ ] ')).length !== 12)
      throw Error('core-release amendment must preserve twelve criteria');
  }
  if (changes.length !== 7 || JSON.stringify(frozenBaselineErrors(result,baseline)) !== JSON.stringify(coreReleaseFrozenChanges))
    throw Error('core-release amendment changed unintended frozen requirements');
  return result;
}
export const protectedSections = {
  'APP013_REMAINING_EXECUTION_CONTRACT.md': [
    'Authority and fixed scope', 'Mandatory section card before implementation',
    '2B — verified intake creates one reviewed job',
    '3A — Sandbox payment on the admitted job',
    '3B — one test-calendar appointment',
    "3C — receive that appointment's confirmation text",
    '3D — changes and recovery on the same journey',
    'Reporting and remaining MVP boundary',
  ],
  'PAYMENT_BOOKING_TEXT_STEEL_THREAD.md': ['Section acceptance cards'],
  'TICKETS/APP-013.md': ['Acceptance Criteria (must all pass)'],
};

// Checked/unchecked evidence status may change, but its requirement text may not.
const normalize = text => text.replace(/\r\n/g,'\n').replace(/^- \[[ xX]\] /gm,'- [ ] ').trim();
function section(text, title) {
  const lines=text.replace(/\r\n/g,'\n').split('\n');
  const starts=lines.flatMap((line,i)=>line === '## '+title ? [i] : []);
  if(starts.length !== 1) throw Error('missing or duplicated section: '+title);
  const start=starts[0]; let end=start+1;
  while(end<lines.length && !/^#{1,2} /.test(lines[end])) end++;
  return normalize(lines.slice(start+1,end).join('\n'));
}
function ids(text, file) {
  const regex=file.startsWith('APP013_') ? /^## (.+)$/gm : /^### (\d+[A-Z]) — /gm;
  return [...text.matchAll(regex)].map(m=>m[1]).join(',');
}
export function frozenBaselineErrors(current, baseline) {
  const errors=[];
  for(const [file,titles] of Object.entries(protectedSections)) {
    try {
      if(typeof current[file] !== 'string' || typeof baseline[file] !== 'string') throw Error('missing file');
      if(ids(current[file],file)!==ids(baseline[file],file)) errors.push(`[frozen-order] ${file}: section IDs/order changed`);
      for(const title of titles) {
        if(section(current[file],title)!==section(baseline[file],title)) errors.push(`[frozen-criterion] ${file} / ${title}`);
      }
    } catch(e) {errors.push(`[frozen-invalid] ${file}: ${e.message}`);}
  }
  return errors;
}
export function checkFrozenBaseline(root=process.cwd()) {
  try {
    const current={}, baseline={};
    for(const file of Object.keys(protectedSections)) {
      current[file]=readFileSync(resolve(root,file),'utf8');
      baseline[file]=execFileSync('git',['show',baselineRef+':'+file],{cwd:root,encoding:'utf8',stdio:['ignore','pipe','pipe']});
    }
    const record=execFileSync('git',['show',automaticAdmissionRef+':'+automaticAdmissionRecord],{cwd:root,encoding:'utf8',stdio:['ignore','pipe','pipe']});
    const patch=execFileSync('git',['show',coreReleaseRef+':'+coreReleasePatch],{cwd:root,encoding:'utf8',stdio:['ignore','pipe','pipe']});
    return frozenBaselineErrors(current,applyCoreReleaseAmendment(applyAutomaticAdmissionAmendment(baseline,record),patch));
  } catch {return ['[frozen-unavailable] Required files or pinned Git revision unavailable. Fetch history; do not skip or regenerate the baseline.'];}
}
if(process.argv[1] && resolve(process.argv[1])===fileURLToPath(import.meta.url)) {
  const errors=checkFrozenBaseline();
  if(errors.length) {console.error(errors.join('\n'));console.error('STOP: owner-reviewed baseline change required; do not silently rebaseline.');process.exitCode=1;}
  else console.log('frozen-baseline-check passed');
}
