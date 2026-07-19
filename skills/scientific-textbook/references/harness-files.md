# Harness Files

Create the smallest harness that preserves authority, continuity, and verifiable completion. The standard harness below is the default for a serious multi-chapter project; simplify only through an explicit decision. Do not copy large templates blindly; fill each file with project-specific decisions.

## Core harness

### `PRD.md`

Record title, vision, learner profile, entry assumptions, exit capabilities, scope, exclusions, evidence profile, assessment strategy, publication constraints, and unresolved questions. Mark each project assumption as confirmed, inferred, or provisional.

### `BOOK_ARCHITECTURE.md`

Record the organizing unit, MECE capability domains, prerequisite logic, progression, learner routes, evidence strategy, and split/merge criteria.

### `TOC.md`

Record stable chapter IDs, titles, primary capabilities, and status. Prefer `planned`, `drafting`, `evidence-ready`, `review`, and `complete` for complex projects. If checkboxes are used, define exactly what `[x]` means.

### `STYLE_GUIDE.md`

Record heading hierarchy, title convention, voice, notation, definitions, theorem/proof format, figures, tables, citations, code, exercises, and profile-specific presentation rules. Define required learning functions; lock exact headings only when consistency justifies the rigidity.

### `CODEX.md`

Keep a concise session brief containing project identity, authority order, startup sequence, prohibited shortcuts, validation commands, and current high-level status. Link to authoritative files instead of duplicating them.

### `NOTATION.md`

Use fields appropriate to the domain, normally symbol, meaning, units or dimensions, scope, first introduction, and notes. Reserve symbols deliberately and detect semantic reuse.

### `GLOSSARY.md`

Record term, precise definition, status (`established`, `project-specific`, or `proposed`), first introduction, and source when needed.

### `DECISIONS.md`

Use append-only entries with ID, date, decision, rationale, status, and affected artifacts. Supersede earlier entries explicitly; historical immutability does not imply permanent correctness.

### `QUALITY_GATES.md`

Define core and profile-specific acceptance criteria, evidence required for each gate, validator commands, review roles, and status-transition rules.

### `PROGRESS.md`

Record project phase, last completed work, currently active work, next exact item, target files, blockers, validation state, and a concise session log. This is a bookmark, not the authority for architecture or scientific claims.

### `RESUME.md`

Provide a short resumption prompt that tells a fresh agent to read `CODEX.md`, `PROGRESS.md`, the target contract, relevant registries, and profile-specific records; inspect existing changes; then execute the next exact item and update state.

## Conditional structured records

Add these when scale or risk warrants them:

- `curriculum/chapters.json` or YAML: stable IDs, prerequisites, capabilities, source mappings, artifact requirements, status.
- `schemas/`: machine-checkable contracts for chapters, experiments, datasets, claims, or reviews.
- `TRACEABILITY.md` and coverage matrices: source-to-destination and objective-to-evidence mappings.
- `reviews/`: self-review, independent review, findings, remediation, and acceptance evidence.
- `sources/` or bibliography records: claim-to-source traceability.
- `SOURCE_POLICY.md`: acceptable sources, verification rules, citation style, currency requirements, and conflict handling.
- `SAFETY_AND_ETHICS.md`: hazards, prohibited content, supervision, privacy, consent, escalation, and expert-review requirements.
- `PUBLICATION.md`: target formats, bibliography, figures, accessibility, rendering, and release packaging.
- `datasets/`: cards containing provenance, license, metadata, task boundaries, and limitations.
- `labs/`, `scripts/`, `environments/`, and `artifacts/`: executable learner and reference packages.
- `prototypes/` or a migration ledger: noncanonical experiments and their canonical destinations.

## Machine-readable chapter record

For large projects, include at least:

```yaml
id: C01
title: Example chapter
primary_capability: An observable capability statement
prerequisites: []
scope_exclusions: []
evidence_classes: [controlled-example]
learner_output: A named artifact or assessed response
status: planned
required_gates: [harness, scientific, pedagogical, editorial]
```

Extend this schema for the selected profile. Keep generated status views synchronized with the canonical registry; declare which record is authoritative.

## Initialization checks

After creating the harness:

1. verify that every exit capability has a destination;
2. verify that prerequisites refer only to valid earlier or explicitly external knowledge;
3. verify that every chapter has evidence and mastery output appropriate to its profile;
4. run `python3 scripts/validate_harness.py <project-dir>` from the skill directory;
5. record deferred decisions and set the next exact work item.
6. confirm that consequential unanswered questions are visible rather than silently converted into facts.
