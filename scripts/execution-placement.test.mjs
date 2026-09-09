import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";
import { executionPlacementErrors } from "./execution-placement.mjs";

const pointer = readFileSync("GLOBAL_EXECUTION_POINTER.md", "utf8");
const handoff = readFileSync("SESSION_HANDOFF.md", "utf8");
const row = pointer.match(/^\|\s*Backend\s*\|.*$/m)?.[0];
const step = handoff.match(/^2\. After review.*$/m)?.[0];
test("current pointer and handoff have properly placed status and ordered steps", () => {
  assert.deepEqual(executionPlacementErrors(pointer, handoff), []);
});
test("prior swapped-row/step failure is rejected without touching repository files", () => {
  assert.ok(row && step);
  const errors = executionPlacementErrors(pointer.replace(row, step), handoff.replace(step, row));
  assert.equal(errors.length, 2);
});
test("missing or duplicated backend rows fail", () => {
  assert.ok(row);
  for (const replacement of ["", row + "\n" + row]) assert.equal(executionPlacementErrors(pointer.replace(row, replacement), handoff).length, 1);
});
test("missing or nonsequential next actions fail", () => {
  assert.ok(step);
  for (const replacement of ["", step.replace(/^2\./, "9.")]) assert.equal(executionPlacementErrors(pointer, handoff.replace(step, replacement)).length, 1);
});
