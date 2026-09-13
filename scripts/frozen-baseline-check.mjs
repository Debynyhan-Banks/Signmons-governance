import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

// Owner-requested baseline freeze. Never move this anchor merely to pass CI.
// A dedicated owner-approved change record and old/new review is required.
export const baselineRef = '57ca1cf0f12ed79075b6afd4781bf28be5e36abc';
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
    return frozenBaselineErrors(current,baseline);
  } catch {return ['[frozen-unavailable] Required files or pinned Git revision unavailable. Fetch history; do not skip or regenerate the baseline.'];}
}
if(process.argv[1] && resolve(process.argv[1])===fileURLToPath(import.meta.url)) {
  const errors=checkFrozenBaseline();
  if(errors.length) {console.error(errors.join('\n'));console.error('STOP: owner-reviewed baseline change required; do not silently rebaseline.');process.exitCode=1;}
  else console.log('frozen-baseline-check passed');
}
