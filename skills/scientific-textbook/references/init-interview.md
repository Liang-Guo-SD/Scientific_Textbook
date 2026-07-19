# Initialize a Textbook Project

Use this reference only when creating or materially re-architecting a textbook harness.

## Socratic discovery

Read `socratic-dialogue.md`. Collect or infer the decisions below in short rounds rather than presenting a ten-question form. Start with the smallest set needed to propose a useful architecture.

### Round 1 — Learner and destination

Establish the target learner, entry knowledge, study context, and observable exit capabilities. Ask what successful readers should be able to produce, explain, calculate, evaluate, or decide.

### Round 2 — Scope and evidence

Establish included and excluded subjects, the dominant evidence profile, evidence sources, and whether current literature, datasets, experiments, code, standards, or field records are required.

### Round 3 — Production and assurance

Establish output directory and format, assessment strategy, notation and citation constraints, existing material to preserve, publication intent, review standard, and any safety, ethics, privacy, or regulatory boundaries.

Do not require two running examples. Ask instead which examples or evidence classes are pedagogically necessary and what role each serves.

After each round, summarize what is settled, what is assumed, and what remains open. Do not ask the next round when the information is already available in existing files.

## Architecture proposal

Before writing chapters:

1. Convert the exit capabilities into a small set of MECE capability domains.
2. Decompose each domain into independently assessable chapter capabilities.
3. Define prerequisites and check that the graph is acyclic and beginner-safe.
4. Assign evidence and a mastery output to each chapter.
5. Map all legacy source material to destinations when rewriting an existing book.
6. Group chapters into parts only after the capability and prerequisite structure is sound.
7. Present the architecture and major tradeoffs for approval before creating a large harness.

Use approval as a Socratic checkpoint: ask whether the proposed progression matches the learner's actual destination, which prerequisite assumption is most questionable, and which evidence class would make the author distrust a chapter if omitted.

Avoid fixing chapter count too early. Split or merge according to cognitive load, prerequisite boundaries, evidence burden, and mastery coherence.

## Harness creation

After approval, read `harness-files.md` and create the core harness. Add only the profile-specific files justified by the project. For large or executable books, create a machine-readable curriculum registry and a validator from the beginning.

Run the baseline validator, report assumptions and deferred decisions, and set `PROGRESS.md` to the next exact work item. The next item need not be chapter prose.
