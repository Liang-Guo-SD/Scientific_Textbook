# Review and Release

Apply gates independently. Passing one gate does not imply another.

## Core quality gates

### Harness integrity

- Authority, IDs, statuses, links, registries, and progress agree.
- A fresh agent can identify the next exact work item without chat context.
- Historical prototypes and canonical chapters are not conflated.

### Scientific or conceptual integrity

- Central claims are correct and appropriately bounded.
- Definitions, assumptions, notation, units, conventions, derivations, and sources are internally consistent.
- Proposed frameworks and modeling choices are distinguishable from established results.
- Alternative explanations, counterexamples, or validity limits are visible.
- Literature-dependent claims trace to verified sources, and conflicting evidence is not concealed.

### Pedagogical integrity

- Check the learning functions across the teaching unit declared in the existing chapter/capability contract. Linked fulfillment is acceptable for transitional or reference material; flag missing coverage or unjustified omissions. Do not require the same visible shell in every passage.
- Objectives are observable and prerequisites are safe.
- Diagnostics have repair routes.
- Evidence applications expose reasoning and support transfer.
- Misconceptions or failure modes are repaired.
- Practice and mastery evidence align with the objectives.

### Editorial integrity

- Apply `reader-centered-writing.md` to substantive prose review. The main question, explanatory sequence, and consequential result remain identifiable without following optional branches.
- Necessary definitions, relationships, and qualifications appear at the reader's point of need. Secondary cases have useful destinations and clear selection conditions when they affect a decision.
- Sentences name their relevant objects and actions. Audit vocabulary, invented labels, rhetorical framing, repeated caveat endings, and excessive emphasis do not displace explanation.
- Compare revised passages with their source for quantities, units, denominators, comparison groups, conditions, negation, uncertainty, attribution, causal strength, and completion status. Resolve or flag substantive errors before accepting a style revision.
- Heading hierarchy, title convention, cross-references, terminology, figures, tables, citations, and chapter structure follow the style guide.
- The chapter does not silently depend on later material.

Use a concrete comprehension task in review: explain the main result, reconstruct a key inference, identify its evidence and governing limit, or apply it to a changed case. A routine model walkthrough can expose missing information; record who performed the check, its limits, and any obstruction found. Require a human-reader trial when the project's quality gates call for one; if that required trial is unavailable, keep its gate unresolved. A model walkthrough is not a completed human-reader trial. Keep findings in review records; do not append a compulsory editorial checklist or score to the chapter.

## Profile-specific gates

Add empirical integrity, dataset integrity, reproducibility, operational safety, ethics, privacy, standards compliance, source integrity, accessibility, or release packaging from `project-profiles.md` when applicable.

For high-stakes or regulated content, require a qualified human reviewer. An LLM self-review or second-agent review does not satisfy this gate.

## Review roles

Use separate records for:

- **Self-review:** catches omissions and contract violations before handoff.
- **Independent review:** evaluates raw artifacts without relying on the author's claims about quality. Record reviewer role, scope, source state, findings, severity, required remediation, and acceptance tests.
- **Release review:** verifies that accepted remediation, canonical status, manifests, and distributable artifacts agree.

An agent in the same authoring context may perform a useful adversarial self-review, but do not call it independent unless the project explicitly accepts that meaning. Preserve the distinction in the review record.

## Finding lifecycle

Each material finding needs:

- stable ID and severity;
- affected gate and artifact;
- concrete evidence;
- required remediation;
- an observable acceptance test;
- current state: open, resolved, accepted risk, or superseded.

Do not erase failed reviews after remediation. Append the recheck and current decision.

## Status transition

Recommended states:

```text
planned -> drafting -> evidence-ready -> review -> complete
```

Move forward only when the state's declared entry criteria pass. Move backward when a later change invalidates earlier evidence. `complete` means all required gates passed at an identified source and artifact state; it does not mean perfect or immutable.

Before release, ask the author to confirm the intended audience, publication claim, unresolved risks, reviewer qualifications, and whether any provisional assumption remains in learner-facing content.

## Completion report

Report:

1. what changed and which files are authoritative;
2. validators, tests, renders, or reviews performed;
3. remaining limitations and accepted risks;
4. the resulting canonical status;
5. the next exact work item.
