# Chapter Contract and Writing Workflow

Use this reference when planning, drafting, resuming, or revising a chapter.

For an isolated excerpt, use the supplied learner, question, and editing scope. Treat it as part of a larger teaching unit unless the user requests a complete stand-alone unit. Write or revise the requested passage; add diagnostics, exercises, or other chapter functions only when they belong to that passage's task.

## Contract before prose

For substantial projects, define these fields before drafting:

- stable chapter ID and title;
- primary learner capability;
- the coherent teaching unit in which its learning functions are fulfilled, normally this chapter;
- observable learning objectives;
- prerequisites and explicit non-prerequisites;
- scope exclusions and previewed concepts;
- central concepts, claims, and evidence classes;
- learner output and mastery criteria;
- profile-specific experiment, dataset, proof, source, or artifact requirements;
- completion gates and current status.

If the chapter contract is scientifically or pedagogically unsettled, resolve it before producing polished prose.

At the contract boundary, ask focused questions when the author has not determined a consequential prerequisite, claim type, evidence source, learner output, or safety limit. Offer a proposed default and explain its consequence. Do not ask about choices already settled by the harness.

## Required learning functions

Fulfill the following functions across the teaching unit identified in the existing chapter/capability contract. Normally that unit is a chapter. A short transition, subsection, reference page, or appendix can point to functions supplied elsewhere in the unit instead of reproducing a full chapter shell. Make that location clear in the existing contract; justify any inapplicable function there. Review coverage across the same unit. Flexible placement does not remove diagnostic, practice, or mastery responsibilities.

These are learning functions, not compulsory visible headings. Their order and emphasis follow the explanation and the project's style guide.

1. **Orientation:** state the practical or intellectual question, observable objectives, prerequisites, and scope.
2. **Entry diagnostic and repair:** reveal missing prerequisites and point to a concrete repair route. A zero-foundation first chapter may use the chapter itself as the repair route.
3. **Plain-language model:** build intuition without relying on untaught formalism.
4. **Formal development:** define terms and symbols, derive or justify central results, and state assumptions and validity domains.
5. **Evidence applications:** work through enough complementary cases to establish transfer, contrast, or boundary awareness.
6. **Failure and limitation analysis:** repair plausible misconceptions and show counterexamples, failure modes, uncertainty, or unsupported claims.
7. **Learner practice:** include scaffolded recall/calculation, evidence interpretation, and transfer/design work as appropriate.
8. **Mastery evidence:** define an observable pass criterion and remediation route. Activity completion alone is not mastery.
9. **Connection:** summarize what the learner can now do, what remains unsupported, and the next capability.

Executable or empirical chapters must integrate their learner workflow into these functions; do not append an unexplained code dump or dataset mention.

## Explanatory sequence and detail

Read `reader-centered-writing.md` before drafting or substantive revision. Choose the passage's question and the result the reader needs to reach. Develop the needed model and reasoning before introducing secondary cases. Keep conditions that change the conclusion at the point of use; give optional refinements a named destination. A complete concept inventory is not a readable chapter outline.

During revision, remove repetitive framing and audit language by stating the concrete scientific meaning. Check whether sentence simplification changes the claim. Preserve stable terminology and useful formalism. If a source leaves a logical or evidential gap, identify or resolve it rather than disguising it with fluent prose.

## Formal and scientific discipline

- Check `NOTATION.md` before introducing a symbol. Record meaning, scope, units or dimensions, first use, and conflicts when relevant.
- Introduce a new symbol by naming it in context, explaining it in plain language, and instantiating it in a small example.
- Check `GLOSSARY.md` before defining a term. Distinguish established terms of art from project-specific vocabulary.
- State each theorem or proposition precisely. A proof sketch must identify the actual argument, not merely name a broad field. If proof is omitted, state why and cite a suitable source when citations are in scope.
- Check equations dimensionally, numerically, by limiting case, by counterexample, or by an equivalent method suited to the domain.
- Label proposals at the first substantive use. Separate established fact, sourced empirical result, interpretation, modeling choice, and research hypothesis.
- Verify literature-dependent and current claims under `source-integrity.md`; drafting fluency is not evidence.
- Use forward references only when the current reasoning remains possible without the future concept.

## Evidence coverage

Create an internal concept-to-evidence matrix for dense chapters:

| Central concept | Explanatory case | Contrasting or boundary case | Empirical/computational check | Limitation |
|---|---|---|---|---|

Not every cell must be filled. Every central concept must have evidence adequate to the chapter's claim and profile.

When using running examples:

- give each example a declared role;
- preserve continuity of facts, notation, and assumptions;
- require symmetric treatment only for concepts whose objective is cross-domain comparison;
- use the second example to reveal contrast or failure, not merely repeat arithmetic with different nouns.

## Exercises and AI-assisted learning

Use observable tasks. Include solutions, hints, rubrics, or self-check mechanisms according to the project design; do not assume an AI interaction replaces an answer key.

Ground each student-facing AI prompt in the artifacts required for that task. These may include notation, glossary, chapter text, dataset card, experiment output, learner artifact, rubric, or source list. Tell the learner to request checks and counterarguments, preserve uncertainty, and avoid treating model output as authority.

## Drafting and resumption

Before writing, set `PROGRESS.md` to the exact work item and target file. During long work, leave a precise bookmark describing the last completed subsection, unresolved issues, and the next action. On completion, run the relevant review and release workflow before changing canonical status.
