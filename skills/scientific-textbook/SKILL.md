---
name: scientific-textbook
description: Use when designing, writing, reviewing, or resuming a scientific, mathematical, computational, or technical textbook; revising chapters with artificial sentence patterns, excessive detail, or confusing branches; or maintaining a book's curriculum, evidence, notation, and project continuity.
---

# Scientific Textbook Engineering

Build a textbook as a persistent learning system, not a sequence of prose files. Preserve continuity, but require evidence appropriate to the book's claims and profile. This skill is Codex-first and assumes an agent that can inspect and edit project files and run relevant tools. Other filesystem agents may adapt the workflow, but compatibility is not guaranteed.

## First Principles

Optimize for these outcomes:

1. A defined learner can acquire observable capabilities from declared prerequisites.
2. Claims are correct, bounded, sourced when needed, and separated from hypotheses.
3. Examples, proofs, data, or experiments provide inspectable evidence rather than decoration.
4. Another agent can resume from project files without private chat context.
5. Completion means that declared quality gates passed; prose existence is insufficient.
6. The learner can follow the central explanation, reconstruct its reasoning, and recognize its limits without decoding the author's working records.

The skill structures authoring and review; it does not certify scientific truth. Require suitable sources, tools, and human subject-matter review for publication, especially in high-stakes or regulated domains.

## Collaborate Socratically

Use staged questions to uncover consequential assumptions without turning initialization into an interrogation. Read `references/socratic-dialogue.md` before initialization or whenever scope, evidence, safety, or publication intent is materially ambiguous.

- Inspect available files and user context before asking.
- Ask one to three focused questions per round.
- Explain briefly why each answer changes the result and propose a sensible default when one exists.
- Separate blocking decisions from preferences. Continue with explicit assumptions when the uncertainty is low-risk and reversible.
- Pause for an answer when guessing would materially change the audience, capability architecture, evidence burden, safety boundary, or publication claim.
- Record resolved answers and assumptions in the harness so later sessions do not ask again.
- Re-open the dialogue at architecture approval, chapter-contract approval, and release boundaries when new uncertainty appears.

## Detect the Work Phase

Before editing, inspect the project and select one phase:

- **Initialize:** the user requests a new textbook, or a book project needs its initial session brief. A supplied-passage edit goes directly to writing/revision. Read `references/init-interview.md` and `references/harness-files.md` for initialization.
- **Architect:** scope or sequence is unsettled, chapters are overloaded, or prerequisites conflict. Read `references/project-profiles.md`.
- **Write, revise, or resume:** a target passage is planned, drafted, or difficult to follow. Read `references/chapter-writing.md` and `references/reader-centered-writing.md`. A supplied passage can be edited directly within the requested scope; it does not require initializing a book harness.
- **Review or release:** the user asks for assessment, completion, or publication readiness. Read `references/review-and-release.md`.
- **Migrate:** an older nine-file or fixed-template harness exists. Read `references/migration.md`; preserve authored content and historical decisions.

Do not assume that `PROGRESS.md` saying “next chapter” authorizes prose. The next item may be architecture, research, code, an experiment, remediation, or review.

## Project Profiles

Choose the dominant evidence profile during initialization or infer it from the existing project:

- **Theory:** definitions, derivations, proofs, counterexamples, and exercises.
- **Empirical:** observations, sources, methods, uncertainty, and replication records.
- **Computational:** executable methods, tests, environments, artifacts, and numerical checks.
- **Engineering:** mechanisms, units, controlled experiments, operational boundaries, and verification.
- **Hybrid:** combine only the gates required by the claims and learner outputs.

Read `references/project-profiles.md` before defining profile-specific files or gates. Add safety, ethics, source-integrity, or publication overlays when the claims require them. Never impose executable laboratories on a purely theoretical book, and never permit prose-only completion for a book whose learning objectives require execution or empirical evidence.

## Authority and Startup

Respect the project's declared authority order. If none exists, use:

1. user instructions;
2. active entries in `DECISIONS.md`;
3. `PRD.md` and `BOOK_ARCHITECTURE.md`;
4. machine-readable curriculum or chapter contracts, when present;
5. `TOC.md`;
6. `STYLE_GUIDE.md` and `QUALITY_GATES.md`;
7. `PROGRESS.md` for current state.

For an existing book project, before changing a chapter, read:

1. `CODEX.md`, or legacy `CLAUDE.md` only when `CODEX.md` is absent;
2. `PROGRESS.md` and the target chapter contract;
3. relevant decisions, prerequisites, and coverage records;
4. `NOTATION.md`, `GLOSSARY.md`, and `STYLE_GUIDE.md`;
5. the nearest completed prerequisite and adjacent chapter;
6. profile-specific dataset, experiment, source, or review records.

Inspect existing changes before editing. Preserve unrelated user work.

## Architecture Rules

- Organize the book around learner capabilities, not a desired chapter count.
- Give each chapter one primary capability, a prerequisite boundary, and observable mastery evidence.
- Split a chapter when its prerequisites, evidence burden, or mastery output cannot form one coherent learning unit.
- Maintain a coverage map when rewriting, splitting, merging, or replacing an earlier manuscript.
- Use machine-readable curriculum and chapter contracts for large, multi-agent, executable, or high-risk projects.
- Keep authoritative records distinct from generated artifacts and historical prototypes.

## Chapter Rules

Use the learning functions in `references/chapter-writing.md` across the declared teaching unit. Read `references/reader-centered-writing.md` for drafting and substantive revision. Give each passage a clear question and a connected explanation; introduce the details needed to understand that explanation before developing secondary cases. Preserve consequential qualifications beside their claims.

Keep authoring records in the project files. Present sources, assumptions, uncertainty, and reproducibility details in forms the learner can use. Follow the project's heading convention without turning every passage into the same checklist.

Always:

- define before use and check notation and glossary registries;
- state assumptions, units, coordinates, conventions, and validity domains when relevant;
- distinguish established results, sourced empirical claims, interpretations, and proposed hypotheses;
- introduce new symbols in context, explain them plainly, and instantiate them concretely;
- provide complementary evidence coverage for central concepts;
- include failure modes, misconceptions, counterexamples, or boundary cases;
- preserve prerequisite safety and mark previews as previews;
- ground student-facing AI prompts in the files needed for the task, not automatically only notation and glossary.

Running examples are optional instruments, not universal constraints. When used, assign each a pedagogical role and require symmetric coverage only where comparison is the learning objective.

## Evidence and Execution

Match evidence to the claim. The following is an evidence relationship, not a compulsory paragraph or section sequence:

```text
definition or mechanism -> derivation or controlled case -> contrasting case
-> empirical or computational check when applicable -> limitation -> next check
```

For executable work, separate the learner-facing launcher, domain runtime, configuration, learner-owned outputs, reference artifacts, provenance, and validation logic. Avoid duplicating scientific logic in orchestration scripts. Record environments, versions, seeds, inputs, hashes, expected outputs or tolerances, and known limitations in proportion to reproducibility risk.

For empirical work, preserve source identity, license, acquisition method, metadata gaps, transformations, split boundaries, uncertainty, and the maximum claim the evidence supports.

For claims that depend on literature, standards, current facts, or external data, read `references/source-integrity.md`. Never invent a source, citation, quotation, dataset property, standard, or empirical result. Treat source retrieval and claim verification as work items with their own status.

## State and Decisions

- Treat `DECISIONS.md` as append-only history. Supersede bad decisions explicitly; do not treat prior choices as eternally correct.
- Record assumptions and limitations in artifacts, not only in chat.
- Use explicit states such as `planned`, `drafting`, `evidence-ready`, `review`, and `complete` when a binary checkbox would hide unfinished work.
- Update `PROGRESS.md` at meaningful work-item boundaries, including partial chapters and non-writing work.
- Keep `CODEX.md` concise; point to authoritative files instead of duplicating them.

## Completion Rule

Before changing a canonical item to `complete`:

1. run the project's validator or, for a baseline harness, `python3 scripts/validate_harness.py <project-dir>` from this skill directory;
2. apply all required core and profile-specific gates from `QUALITY_GATES.md`;
3. verify chapter prose, registries, curriculum status, progress, links, and required artifacts agree;
4. require self-review and an independent review when the project declares them;
5. distinguish a passing harness check from scientific, pedagogical, reproducibility, and release acceptance.

Never edit an authoritative status merely to silence a validator. Fix the underlying inconsistency or report the blocker.

## References

- `references/init-interview.md` — initialization questions and architecture approval flow.
- `references/socratic-dialogue.md` — staged questioning, defaults, and blocking-decision rules.
- `references/harness-files.md` — core and optional harness templates.
- `references/project-profiles.md` — profile selection, evidence ladders, and profile-specific artifacts.
- `references/chapter-writing.md` — chapter contract and required learning functions.
- `references/reader-centered-writing.md` — clear narrative, detail selection, terminology, sentence patterns, and meaning-preserving revision.
- `references/source-integrity.md` — research, citation, evidence, safety, and expert-review boundaries.
- `references/review-and-release.md` — MECE quality gates, review roles, and completion transitions.
- `references/migration.md` — migration from legacy fixed-template projects.
