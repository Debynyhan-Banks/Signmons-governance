// Guard against accidentally swapping a status-table row and numbered handoff.
export function executionPlacementErrors(pointer, handoff) {
  const errors = [];
  const status = pointer.match(/### Repo Status\s*\n([\s\S]*?)(?:\n## |$)/)?.[1] ?? "";
  if ([...status.matchAll(/^\|\s*Backend\s*\|/gm)].length !== 1 || /^\d+\. /m.test(status)) {
    errors.push("[pointer-placement] expected one Backend status row and no numbered handoff steps in Repo Status");
  }
  const next = handoff.match(/## Next Actions \(Strict Order\)\s*\n([\s\S]*?)(?:\n## |$)/)?.[1] ?? "";
  const numbers = [...next.matchAll(/^(\d+)\. /gm)].map((match) => Number(match[1]));
  if (numbers.length < 2 || numbers.some((number, index) => number !== index + 1) || /^\|\s*Backend\s*\|/m.test(next)) {
    errors.push("[handoff-placement] expected ordered numbered steps, not a Backend status row, in Next Actions");
  }
  return errors;
}
