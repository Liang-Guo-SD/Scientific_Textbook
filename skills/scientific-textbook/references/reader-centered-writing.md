# Reader-Centered Scientific Writing

Use when drafting or revising textbook prose. Improve the reader's understanding while preserving scientific meaning. Work in the requested language and register; technical clarity does not require conversational storytelling or an external humanizer skill. Patterns below identify possible reading problems, not AI authorship.

## Keep a clear line of explanation

Before drafting, identify the question this passage answers, the knowledge the reader already has, and the result the reader needs to understand. Keep this working outline in authoring notes. In the finished passage, connect the necessary objects and relationships so the reader can reach that result.

Develop the ordinary case far enough to make it intelligible before opening alternatives. Introduce a new concept when the next step needs it, and connect it to something already established. After a necessary detour, return explicitly to the question being answered. A transition should show the relationship between ideas; “next we discuss” alone does not supply it.

Select detail by its job:

| Detail's job | Suitable treatment |
|---|---|
| Needed to understand the mechanism, follow a derivation, interpret the result, or make the current decision | Explain it in the main sequence at the point of need |
| Changes the conclusion, validity, safety, or feasible next step | Keep it beside the claim or action it qualifies |
| Useful refinement, alternative method, extended derivation, or uncommon case | Give it a clearly named note, later section, exercise, or appendix with a precise pointer |
| Interesting but unrelated to the learning objective | Leave it out of this passage; preserve it elsewhere if the editing scope requires retaining it |
| Describes drafting, review status, model execution, or internal tracking | Keep it in the authoring record |

A detail is not necessary merely because it is true or related. Ask what the reader would misunderstand or be unable to do without it **at this point**. This applies to extra decimal conversions, endpoint conventions, taxonomies, historical digressions, and lists of every influencing factor. If nothing important changes, defer the detail or omit it within the authorized scope.

When revising, preserve distinct information the user requires: moving it to a supporting note is different from deleting it. Check affected references when moving material. For a line-edit-only request, retain the structure and flag overload that needs a wider edit.

If several branches are necessary for the current task, state the observable condition that selects each branch and the corresponding consequence. A decision tree or comparison table can help. Introduce only the choices needed for that decision. In a procedure, place required checks and failure exits where the reader needs to act on them. Cognitive simplicity must not hide a consequential exception.

## Make paragraphs advance the reasoning

Use a paragraph to answer a question, establish a relationship, work through a step, or interpret evidence. Carry a named object or result into the next paragraph so the reader can see why the discussion moves there. Let paragraph length follow the reasoning.

Explain a table's consequential comparison and its meaning. Explain an equation's quantities, assumptions, relationship, and interpretation at the reader's level. A list of components does not explain their interaction; a source label does not explain why a result follows. Supply missing reasoning from justified material, or identify the gap. Keep the accurate argument when a passage already works.

An example should make the relationship easier to use. Extend it only when the extension teaches a needed distinction. An analogy should map recognizable features to the scientific relationship; state its boundary where a plausible wrong inference arises. Repeated “this analogy is wrong” endings are not a substitute for judging that boundary.

## Edit sentence patterns by meaning

Read the passage continuously, then inspect sentences that interrupt, inflate, or obscure its argument. Use the following decisions rather than a forbidden-word list. A useful contrast, formal noun, repeated term, or short sentence can remain.

| Pattern to inspect | What to write instead |
|---|---|
| Inflated framing: “a new paradigm,” “不是 X，而是 Y,” “不仅……更是……” | State the substantive result directly. Retain both sides when they distinguish real alternatives or correct a plausible misconception. |
| Abstract nouns hide the action: “进行……的确认,” “实现……的对齐,” long chains of “的” | Name the actor, action, object, and condition that matter. For example, “检查两组数据是否使用同一分母” identifies the check more precisely than “完成口径对齐.” |
| Invented compound names, acronyms, audit codes, or governance metaphors | Name the actual quantity, operation, or relationship. Define a useful repeated local term and distinguish it from established terminology. |
| Vague references: “this,” “it,” “the framework,” “这套东西” | Name the relevant component when the referent is unclear or changes from sensor to algorithm to installation. |
| Empty intensifiers and stacked adjectives: “robust, seamless, comprehensive” | Give the supported behavior, comparison, or condition. If evidence is absent, remove the unsupported praise; do not invent numbers. |
| Sentence restates the heading, announces the next sentence, or recaps the immediately preceding claim | Begin with the information that advances the argument. Keep orientation that helps readers locate themselves after a substantial change. |
| Repeated fragments, slogan endings, rhetorical questions, or staged objections | Express the actual relationship in connected sentences. Use a question when its answer organizes a real inquiry, and an objection when it tests a consequential alternative. |
| Every explanation is forced into three items or an identical cadence | Group independent ideas according to their relationship. Keep useful enumerations; change repeated wording only when it impedes reading. |
| Qualifications accumulate around every number or positive claim | State the shared scope naturally and attach each additional limitation to the claim it actually changes. Preserve uncertainty and necessary local conditions. |
| A list of negations tells readers only what to reject | Explain the valid interpretation and the reason the tempting inference fails. Retain a negation that carries an important boundary. |
| Dialogue contains registry labels, provenance badges, or polished maxims in every voice | Put attribution in narration and retain dialogue that serves the instructional task. Factual prose gains clarity through explanation, not invented personal experience. |

Keep one stable name for a concept after introducing it. Explain an established abbreviation at the reader's first need; retain it when conventional or useful for repeated reference. A full expansion that remains opaque still needs explanation. An unnecessary one-off abbreviation can be written out. Use the existing glossary rather than creating a new coding scheme.

Match sentence length to the relation being expressed. Combine fragments when they belong to one thought; divide a dense sentence when its conditions or referents become hard to track. Preserve explicit logical connectors where they express cause, contrast, sequence, or simultaneity. Forced sentence-length variation and universal short-sentence rules create new obstacles.

## Make evidence readable

Distinguish measured, simulated, calculated, assumed, and proposed statements in ordinary language. A continuous passage can share an explicit scope. Restate the relevant scope when it changes or when a claim, table, figure, or summary is meant to stand alone. A qualification that changes a reasonable interpretation stays with the claim.

Use normal citations and useful source or methods notes. Internal fact IDs may support traceability in working records; readers need an intelligible source reference. Learner-facing code, paths, commands, logs, and provenance records belong in the text when learning to use them is part of the task.

Keep distinctions that shortening often erases: a chosen acceptance threshold versus a physical limit; missing a target versus having no benefit; a calculation versus an experiment; a model result versus field performance; an observed zero versus an impossibility; and an association versus a cause. If the source confuses them, resolve the issue from available evidence or flag it separately from the style edit.

Interpret a central quantitative result in terms the reader needs for the current comparison. For example, an energy ratio of 0.94 represents 6% lower modeled energy relative to its stated denominator; that interpretation retains the model's conditions and does not establish field performance.

## A worked revision

The following is a constructed teaching example, not a reported experiment.

**Draft:**

> 这不是一次简单的采样配置，而是带宽与时间的深度博弈。应构建 RVC（记录有效性契约），对记录时长口径进行冻结，形成可审计、可回放、可验收的证据闭环。保存 2048 点，采样率由每秒 512 点升到 2048 点，时长从 4 秒缩至 1 秒。还需综合考虑电池、传输、时钟、窗函数、存储策略及未来部署。不是采得越快越好，而是让每个点承担证据责任。

**Revision:**

> 保存点数固定时，采样越快，同一段记录覆盖的时间就越短。设每次保存 2048 个点：每秒采 512 点，记录时长为 2048 ÷ 512 = 4 秒；每秒采 2048 点，时长就变成 1 秒。
>
> 因此，选择采样率时还要检查记录时长是否足够。提高采样率能把相邻采样时刻排得更密，但可能使我们来不及记录完整的变化过程。这个计算只说明固定点数下的时间关系；实际设置还必须满足信号对采样率的要求。

The revision replaces the invented contract and slogans with the relationship and its calculation. It keeps the boundary needed for interpreting the example. The draft's unquantified list does not explain the current relationship; useful discussion of power or transmission belongs in a section that teaches that tradeoff. If preserving all source material is required, move the list into a supporting note instead of silently deleting it.

**Preserve-as-written cases:** a precisely scoped theorem needs its hypotheses; a laboratory needs executable instructions; a diagnostic procedure may need several failure branches; a stand-alone results table needs its denominator and evidence status. These are useful information, not patterns to erase.

## Revision and final reading

Match the intervention to the request: line editing improves expression; structural editing changes sequence and placement; explanatory revision repairs reasoning using supported material. For a substantial revision, work from purpose and missing or unsound information toward organization and sentence editing. Keep review notes outside the finished passage.

Compare the revision with its source for quantities, units, denominators, comparison groups, conditions, negation, uncertainty, attribution, causal strength, and completion status. Verify changes to claims as scientific work. A shorter or more natural sentence is not evidence that its meaning survived.

Read the finished passage as a continuous explanation. Can the intended learner identify the main result, reconstruct a key step, recognize its governing limit, and continue without pursuing optional branches? Repair the specific obstruction. Report only the requested prose and material unresolved issues; avoid adding a self-score or a compulsory editing report. Human-reader trials provide stronger evidence of comprehension than a model's self-assessment.
