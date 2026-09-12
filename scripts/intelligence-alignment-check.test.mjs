import { test } from 'node:test';
import assert from 'node:assert/strict';
import { alignmentErrors, sequence } from './intelligence-alignment-check.mjs';
const board = (now, next) => '## Now\n\n- [ ] ' + now + '\n\n## Next\n\n' + next.map(x => '- [ ] ' + x).join('\n') + '\n\n## Later\n';
const pointer = next => '- Approved Next: ' + next.map(x => String.fromCharCode(96) + x + String.fromCharCode(96)).join(' → ');
test('current synchronized dependency order passes', () => {
  const b = board(sequence[0], sequence.slice(1));
  assert.deepEqual(alignmentErrors(b, pointer(sequence.slice(1)), b), []);
});
test('blank Next and stale backend fail', () => {
  assert.ok(alignmentErrors(board(sequence[0], []), pointer(sequence.slice(1)), board('APP-011', [])).length >= 2);
});
test('out-of-order queue and pointer fail', () => {
  assert.ok(alignmentErrors(board(sequence[0], [...sequence.slice(1)].reverse()), pointer(sequence.slice(1))).length >= 2);
});
test('full acceptance promotion can advance to the remaining suffix', () => {
  const b = board(sequence[1], sequence.slice(2));
  assert.deepEqual(alignmentErrors(b, pointer(sequence.slice(2)), b), []);
});
