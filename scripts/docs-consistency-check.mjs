#!/usr/bin/env node

import { existsSync, readFileSync } from 'node:fs';

const errors = [];

const mustRead = (path) => {
  if (!existsSync(path)) {
    errors.push(`[missing-file] ${path}`);
    return '';
  }
  return readFileSync(path, 'utf8');
};

const extractInlineCode = (text) => [...text.matchAll(/`([^`]+)`/g)].map((m) => m[1]);

const requiredFiles = [
  'SYSTEM_OF_RECORD.md',
  'WHAT_SIGNMONS_IS_AND_DOD.md',
  'SAAS_SCOPE_DOD.md',
  'EXECUTION_BOARD.md',
  'SCREEN_INVENTORY.md',
  'MVP_BACKLOG.md',
  'QUALITY_GATES.md',
  'AI_WORKFLOW_RULES.md',
  'SESSION_HANDOFF.md',
  'GLOBAL_EXECUTION_POINTER.md',
  'SCREEN_ROUTE_API_MATRIX.md',
  'LINK_CTA_MAP.md',
  'WORKFLOW_RUNBOOK.md',
  'TICKET_TEMPLATE.md',
  'scripts/docs-consistency-check.mjs',
];

for (const file of requiredFiles) {
  if (!existsSync(file)) errors.push(`[missing-required-file] ${file}`);
}

const board = mustRead('EXECUTION_BOARD.md');
const screensDoc = mustRead('SCREEN_INVENTORY.md');
const pointer = mustRead('GLOBAL_EXECUTION_POINTER.md');
const routeMatrix = mustRead('SCREEN_ROUTE_API_MATRIX.md');
const ctaMap = mustRead('LINK_CTA_MAP.md');
const backlog = mustRead('MVP_BACKLOG.md');

const screenIdRegex = /`(SCR-[A-Z]+-\d+[A-Z]?)`/g;
const screenIds = new Set();
for (const match of screensDoc.matchAll(screenIdRegex)) {
  const id = match[1];
  if (screenIds.has(id)) errors.push(`[duplicate-screen-id] ${id}`);
  screenIds.add(id);
}

if (screenIds.size === 0) {
  errors.push('[screen-inventory-empty] no screen IDs found in SCREEN_INVENTORY.md');
}

const backlogScreenRefs = extractInlineCode(backlog).filter((token) => token.startsWith('SCR-'));
for (const screenId of backlogScreenRefs) {
  if (!screenIds.has(screenId)) {
    errors.push(`[backlog-unknown-screen-ref] MVP_BACKLOG.md references ${screenId} not found in SCREEN_INVENTORY.md`);
  }
}

const matrixScreenRefs = extractInlineCode(routeMatrix).filter((token) => token.startsWith('SCR-'));
for (const screenId of matrixScreenRefs) {
  if (!screenIds.has(screenId)) {
    errors.push(`[matrix-unknown-screen-ref] SCREEN_ROUTE_API_MATRIX.md references ${screenId} not found in SCREEN_INVENTORY.md`);
  }
}

const backlogFeatureLines = backlog
  .split('\n')
  .filter((line) => /^- (APP|FE)-\d+[A-Z]?:/.test(line));
for (const line of backlogFeatureLines) {
  if (!/`SCR-[A-Z]+-\d+[A-Z]?`/.test(line)) {
    errors.push(`[backlog-missing-screen-id] ${line.trim()}`);
  }
}

const nowSection = board.match(/## Now([\s\S]*?)(?:\n## |$)/);
if (!nowSection) {
  errors.push('[missing-now-section] EXECUTION_BOARD.md is missing a Now section');
} else {
  const openNow = [...nowSection[1].matchAll(/^- \[ \] ([A-Z]+-\d+[A-Z]?)/gm)].map((m) => m[1]);
  if (openNow.length !== 1) {
    errors.push(`[wip-rule] expected exactly 1 unchecked ticket in Now; found ${openNow.length}`);
  }

  const pointerNow = pointer.match(/Program `Now`:\s*`([A-Z]+-\d+[A-Z]?)`/);
  if (pointerNow && openNow[0] && pointerNow[1] !== openNow[0]) {
    errors.push(`[pointer-mismatch] GLOBAL_EXECUTION_POINTER.md=${pointerNow[1]} but EXECUTION_BOARD.md Now=${openNow[0]}`);
  }
}

const sectionTickets = (sectionName) => {
  const section = board.match(new RegExp(`## ${sectionName}([\\s\\S]*?)(?:\\n## |$)`));
  if (!section) return [];
  return [...section[1].matchAll(/^- \[ \] ([A-Z]+-\d+[A-Z]?)/gm)].map((m) => m[1]);
};

for (const ticket of [...sectionTickets('Now'), ...sectionTickets('Next')]) {
  if (ticket === 'APP-003A') {
    errors.push('[superseded-ticket] APP-003A cannot appear in Now/Next');
  }

  const activePath = `TICKETS/${ticket}.md`;
  const archivedPath = `ARCHIVE/TICKETS/${ticket}.md`;

  if (!existsSync(activePath)) {
    if (existsSync(archivedPath)) {
      errors.push(`[archived-ticket-referenced] ${ticket} is archived but referenced in EXECUTION_BOARD.md`);
    } else {
      errors.push(`[missing-ticket-file] ${ticket} expected at ${activePath}`);
    }
  }
}

const activeTicketFiles = existsSync('TICKETS')
  ? extractInlineCode(board)
      .concat(extractInlineCode(mustRead('MVP_BACKLOG.md')))
      .filter((code) => /^(APP|FE|GOV|BE|OPS)-\d+[A-Z]?$/.test(code))
      .map((id) => `TICKETS/${id}.md`)
      .filter((path, i, all) => all.indexOf(path) === i && existsSync(path))
  : [];

for (const file of activeTicketFiles) {
  const text = mustRead(file);
  for (const token of extractInlineCode(text)) {
    if (token.startsWith('SCR-') && !screenIds.has(token)) {
      errors.push(`[unknown-screen-ref] ${file} references ${token} not found in SCREEN_INVENTORY.md`);
    }
  }
}

const matrixRoutes = new Set();
for (const token of extractInlineCode(routeMatrix)) {
  if (token.startsWith('/')) matrixRoutes.add(token.replace(/\/+$/, '') || '/');
}

const ctaRoutes = new Set(
  extractInlineCode(ctaMap)
    .filter((token) => token.startsWith('/'))
    .map((route) => route.replace(/\/+$/, '') || '/'),
);

for (const route of ctaRoutes) {
  if (!matrixRoutes.has(route)) {
    errors.push(`[cta-route-mismatch] ${route} exists in LINK_CTA_MAP.md but not in SCREEN_ROUTE_API_MATRIX.md`);
  }
}

const matrixEndpoints = new Set(
  extractInlineCode(routeMatrix).filter((token) => /^(GET|POST|PUT|PATCH|DELETE)\s+\//.test(token)),
);
const ctaEndpoints = new Set(
  extractInlineCode(ctaMap).filter((token) => /^(GET|POST|PUT|PATCH|DELETE)\s+\//.test(token)),
);

for (const endpoint of ctaEndpoints) {
  if (!matrixEndpoints.has(endpoint)) {
    errors.push(`[cta-endpoint-mismatch] ${endpoint} exists in LINK_CTA_MAP.md but not in SCREEN_ROUTE_API_MATRIX.md`);
  }
}

if (errors.length > 0) {
  console.error('docs-consistency-check failed');
  for (const err of errors) console.error(`- ${err}`);
  process.exit(1);
}

console.log('docs-consistency-check passed');
