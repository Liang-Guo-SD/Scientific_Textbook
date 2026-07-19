# Scientific Textbook Engineering

A Codex-first skill for designing, writing, reviewing, and resuming rigorous scientific, mathematical, computational, and technical textbooks.

The skill treats a book as a persistent learning system. It combines capability-based curriculum design, staged Socratic inquiry, notation and terminology control, evidence profiles, source integrity, project state, and explicit quality gates.

## Scope

The skill can support theoretical, empirical, computational, engineering, and hybrid textbook projects. It is not a universal scientific authority and does not certify correctness. Publication-quality work still requires appropriate sources, tools, tests, and qualified human review.

Codex with filesystem and shell access is the supported environment. Claude Code compatibility is experimental. Chat-only LLMs without persistent file access cannot reliably execute the full harness workflow.

## What changed from the original version

- Required learning functions replace the locked eight-section template.
- Evidence coverage replaces the universal two-running-example rule.
- Capability and prerequisite architecture precedes chapter-count decisions.
- Theory, empirical, computational, engineering, and hybrid profiles select appropriate evidence.
- Source-integrity, safety/ethics, regulated-domain, and publication overlays are available.
- Staged Socratic questions surface consequential assumptions while allowing reversible progress.
- `planned`, `drafting`, `evidence-ready`, `review`, and `complete` distinguish real project states.
- Self-review, independent review, remediation, and release acceptance remain separate.

## Socratic workflow

The agent inspects existing context first, then asks one to three focused questions when an answer changes the learner, architecture, evidence burden, safety boundary, or publication claim. It proposes defaults for reversible choices and records confirmed and provisional assumptions in the harness.

Typical starting prompt:

> Use `$scientific-textbook` to help me develop a textbook on continuum mechanics for advanced undergraduates. Ask me focused questions when a consequential choice is unresolved.

## Install for Codex

Codex discovers personal skills under `$HOME/.agents/skills`. Clone the repository, then copy or symlink `skills/scientific-textbook` to `$HOME/.agents/skills/scientific-textbook`. Codex also supports repository-scoped skills under `.agents/skills`.

Alternatively, ask the built-in `$skill-installer` to install the skill from:

```text
https://github.com/Liang-Guo-SD/Scientific_Textbook
```

If an updated skill does not appear, restart Codex.

## Repository layout

```text
skills/scientific-textbook/
├── SKILL.md
├── agents/openai.yaml
├── references/
└── scripts/validate_harness.py
```

The `.claude-plugin` manifest is retained for experimental Claude Code use, but the instructions and validation target Codex first.

## Standard project harness

The standard harness uses:

- `PRD.md`
- `BOOK_ARCHITECTURE.md`
- `TOC.md`
- `STYLE_GUIDE.md`
- `CODEX.md`
- `NOTATION.md`
- `GLOSSARY.md`
- `DECISIONS.md`
- `QUALITY_GATES.md`
- `PROGRESS.md`
- `RESUME.md`

Complex projects may add machine-readable curriculum contracts, schemas, source ledgers, datasets, experiments, environments, learner artifacts, reviews, and publication records.

## Validation

Run the baseline validator from the skill directory:

```bash
python3 scripts/validate_harness.py /path/to/textbook-project
```

A pass verifies baseline file, status, progress, and local-link integrity only. It does not establish scientific, pedagogical, source, reproducibility, safety, or release acceptance.

## License

MIT
