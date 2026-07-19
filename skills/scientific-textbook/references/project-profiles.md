# Project Profiles

Select gates by the claims the book teaches learners to make. A hybrid project combines applicable requirements; it does not automatically inherit every possible artifact.

## Theory profile

Use for mathematics, formal science, logic, and concept-first books.

Require as applicable:

- precise definitions and theorem dependencies;
- proofs, proof sketches with real argumentative content, or sourced omissions;
- examples, nonexamples, counterexamples, edge cases, and limiting cases;
- notation consistency and prerequisite-safe formalism;
- exercises covering construction, derivation, interpretation, and transfer.

Do not require executable code unless computation is a learning objective.

## Empirical profile

Use when claims depend on observations, literature, field records, or datasets.

Require as applicable:

- source and citation traceability;
- acquisition or selection method;
- population, context, uncertainty, bias, and missing metadata;
- transformation and exclusion records;
- separation of observation, interpretation, causal hypothesis, and decision;
- replication path or a clear statement of why replication is unavailable.

## Computational profile

Use when learners must run, inspect, modify, or evaluate software or numerical methods.

Require as applicable:

- declared runtime ownership and API boundary;
- environment or lock, versions, seeds, configuration, and platform assumptions;
- learner-owned outputs separate from canonical reference artifacts;
- expected outputs, tolerances, invariants, tests, and failure behavior;
- provenance and hashes for release evidence;
- clean-install or isolated-environment validation.

## Engineering profile

Use when learners connect models and measurements to physical systems or decisions.

Require as applicable:

- mechanism, units, dimensions, coordinates, reference conventions, and operating conditions;
- analytical or limiting-case checks;
- controlled simulation or experiment with known boundaries;
- empirical or field evidence distinguished from teaching fixtures;
- alternative explanations, discriminating checks, and verification plans;
- standards and thresholds cited with scope and revision.

## Evidence ladder

Choose only the levels needed for the chapter's claims:

1. definition, mechanism, or formal object;
2. toy, analytical, or limiting case;
3. controlled simulation or experiment;
4. empirical observation or public dataset;
5. cross-context, robustness, or domain-shift check;
6. bounded decision and verification plan.

Higher levels do not repair errors at lower levels. A large dataset does not replace a coherent mechanism; a proof does not establish empirical prevalence.

## Selection test

For each objective, ask: “What evidence would allow a learner to demonstrate this capability, and what could still remain false?” Select the profile artifacts and gates from that answer.

## Cross-cutting overlays

Apply overlays independently of the dominant profile.

### Source-integrity overlay

Use when claims depend on literature, standards, current facts, or external data. Require a source policy, claim-to-source traceability, source verification, and an explicit treatment of conflicting or weak evidence. Read `source-integrity.md`.

### Safety and ethics overlay

Use for clinical, human-subject, biological, chemical, environmental, security-sensitive, or operationally hazardous material. Define prohibited instructions, supervision requirements, consent or privacy boundaries, escalation rules, and mandatory human expert review. Educational framing does not remove real-world risk.

### Regulated-domain overlay

Use when standards, certification, law, or professional practice constrain the content. Record jurisdiction, standard edition, effective date, scope, and reviewer qualifications. Do not generalize a requirement beyond its declared applicability.

### Publication overlay

Use when the intended output is more than working Markdown. Define target formats, equations, figures, tables, bibliography, indexing, accessibility, localization, rendering, and release checks. Treat source files and generated publication artifacts as distinct.
