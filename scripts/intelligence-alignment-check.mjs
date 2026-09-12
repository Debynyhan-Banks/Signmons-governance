export const sequence = ['APP-013', 'APP-017', 'APP-018', 'APP-019', 'APP-015', 'APP-016', 'APP-033'];

function tickets(board, section) {
  const body = board.match(new RegExp('## ' + section + '\\n([\\s\\S]*?)(?=\\n## |$)'))?.[1] ?? '';
  return [...body.matchAll(/^- \[ \] ((?:APP|BE)-\d+)/gm)].map(m => m[1]);
}

export function alignmentErrors(board, pointer, backend) {
  const errors = [];
  const now = tickets(board, 'Now');
  const index = sequence.indexOf(now[0]);
  if (now.length !== 1 || index < 0) errors.push('intelligence Now is not a unique approved ticket');
  const next = tickets(board, 'Next');
  if (JSON.stringify(next) !== JSON.stringify(sequence.slice(index + 1))) errors.push('intelligence Next does not match approved remaining dependency order');
  const current = pointer.match(/- Approved Next: ([^\n]+)/)?.[1] ?? '';
  const pointerNext = [...current.matchAll(/\x60(APP-\d+)\x60/g)].map(m => m[1]);
  if (JSON.stringify(pointerNext) !== JSON.stringify(next)) errors.push('intelligence pointer/Next mismatch');
  if (backend !== undefined && (JSON.stringify(tickets(backend, 'Now')) !== JSON.stringify(now) || JSON.stringify(tickets(backend, 'Next')) !== JSON.stringify(next))) errors.push('intelligence backend/governance queue mismatch');
  return errors;
}
