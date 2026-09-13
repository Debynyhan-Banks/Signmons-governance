import {execFileSync} from 'node:child_process';
import {readFileSync,existsSync} from 'node:fs';
import {resolve} from 'node:path';
import {fileURLToPath} from 'node:url';
export const anchor='5bb6295b708c0466d4c1cc19b8609de2b4a4c26a';
export const files=["AGENTS.md",".github/CODEOWNERS","docs/execution-baseline/APP013_REMAINING_EXECUTION_CONTRACT.md","docs/execution-baseline/PAYMENT_BOOKING_TEXT_STEEL_THREAD.md"];
export const normalize=s=>s.replace(/\r\n/g,'\n').replace(/^- \[[ xX]\] /gm,'- [ ] ').trim();
export function compare(current,baseline) {
 return files.flatMap(file=>typeof current[file]!=='string'||typeof baseline[file]!=='string'||normalize(current[file])!==normalize(baseline[file])?['Protected baseline changed: '+file]:[]);
}
export function check() {
 try {
 const current={},baseline={};
 for(const file of files) {
 current[file]=readFileSync(file,'utf8');
 baseline[file]=execFileSync('git',['show',anchor+':'+file],{encoding:'utf8',stdio:['ignore','pipe','pipe']});
 }
 const errors=compare(current,baseline);
 for(const file of ['APP013_REMAINING_EXECUTION_CONTRACT.md','PAYMENT_BOOKING_TEXT_STEEL_THREAD.md']) {
 if(existsSync(file)&&normalize(readFileSync(file,'utf8'))!==normalize(baseline['docs/execution-baseline/'+file]))
 errors.push('Canonical plan differs from frozen snapshot: '+file+'; review scope/status changes explicitly before adoption.');
 }
 return errors;
 } catch {return ['Missing baseline file/history; fetch full history. Do not skip or regenerate.'];}
}
if(process.argv[1]&&resolve(process.argv[1])===fileURLToPath(import.meta.url)) {
 const errors=check();
 if(errors.length){console.error(errors.join('\n'));console.error('STOP: explicit owner-reviewed baseline change required.');process.exitCode=1;}
 else console.log('execution-controls passed');
}
