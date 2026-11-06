# Manual Editorial Scenarios

These are behavioral checks for drafting and revision, separate from the Python package and harness tests. They are not an AI detector or a validated comprehension benchmark.

For a comparison, use independent contexts with the same model, settings, source packet, and request: one set reads the previous skill, the other the revised skill. Keep generated passages for inspection. Repeat samples when assessing variability; five per condition is a useful small check, not a reliability guarantee. Read every output. Report cases where the previous skill already performs well. Human-reader evaluation should use readers matching the brief and a fresh passage rather than only these development cases.

## Fixed-memory explanation with distracting source notes

Request:

> Write a finished Chinese textbook section for first-year engineering students answering: 在保存点数固定时，为什么提高采样率不一定更好？ The reader has learned frequency and units but not signal processing. Use the supplied skill. The notes are source material, not a locked outline. Select and reorganize main-text detail while preserving technical meaning and giving useful secondary information an appropriate home. Deliver only the passage and any useful supporting note. Aim for 700–1000 Chinese characters, with at most two subsection headings.

Source packet:

- One buffer holds 4096 samples. Uniform sampling is assumed; this is a calculation, not a hardware experiment.
- Record duration is represented by `T=N/fs`: 1024 samples/s gives 4 s; 4096 samples/s gives 1 s.
- A 5 Hz periodic process completes about 20 cycles in 4 s and 5 cycles in 1 s. Cycle counts alone do not establish estimation accuracy.
- Adequate sampling rate and an appropriate analog anti-alias filter still matter. Under the ideal band-limited assumption, the rate must exceed twice the highest signal frequency. No real filter design or universal best rate is established here.
- Storing 16384 samples would allow 4 s at 4096 samples/s, changing the fixed-memory premise.
- Other notes mention noise, jitter, quantization, saturation, changing speed, nonperiodic events, frequency resolution, processing, battery, radio transfer, and scheduling. No numerical tradeoff is supplied. Troubleshooting connections, clock repair, storage policy, spectral windows, oversampling, and compressed sensing are separate possible topics.
- Local author tags `RAR` (Rate Adequacy Rule), `BOC` (Buffer Observation Contract), `P17` (cycle calculation), and `H4` (review pending) have no external technical standing.
- Prior draft: “这不是一个采样率参数，而是一场带宽与时间的博弈。必须构建可审计、可回放、可验收的证据闭环。首先进行采样率配置的确认，其次进行记录时长口径的冻结，最后完成面向现场部署的质量门禁对齐。不是采得越快越好，而是让每一个点都承担证据责任。空白就写空白。”

Inspect whether the reader can follow the rate–duration relationship and distinguish it from accuracy. Check that optional notes do not become equally weighted main-text branches, and that extra precision earns its place. The conditions needed to prevent “lower is always better” must remain. Look for specific replacements of the draft's audit language and rhetoric, not merely changes to punctuation. A useful equation or comparison is not a defect.

## Shortening without changing the claim

Request: revise this result for a technical textbook, preserving its meaning and explaining the distinction relevant to the reader.

> In an uncalibrated energy model, policy A uses 0.94 times the energy of policy B under the stated scenario. The chosen acceptance target was a ratio no greater than 0.90. The report says: “The energy-saving mechanism failed, so policy A saves no energy.” The ratio was obtained by rescaling recorded components, not by rerunning a changed operating schedule. No detection-performance result is supplied for that schedule.

Inspect whether the revision distinguishes a modeled reduction of 6% from failure to meet the chosen target of at least 10%. It must preserve the model and calculation status and leave changed-schedule performance unestablished. Additional unsupported operating advice is a failure.

## Preserving necessary branches and technical material

Request: make this learner-facing computational exercise clear without changing its commands or branch behavior.

```text
Run: python analyze.py --input sample.csv --output result.json
If the input is absent, stop and obtain the supplied file.
If the time column is not strictly increasing, stop and inspect its timestamps; do not sort it silently.
Otherwise run the command and compare the named output quantity with the supplied tolerance.
The exercise supplies no result for missing or invalid input.
```

Inspect whether code, filenames, stop conditions, and expected interpretation remain usable. Moving a consequential failure exit to a distant appendix or inventing a tolerance is a failure.

## Preserving formal precision and useful consistency

Request: revise a short proof for beginning mathematics students. Supplied claim: for real `x>0`, `x+1/x >= 2`, with equality exactly at `x=1`. Supplied reasoning: `(x-1)^2 >= 0`; divide by positive `x`, then rearrange.

Inspect whether the hypothesis, reason division preserves the inequality, argument, and equality condition survive. A standard theorem/proof layout and repeated `x` are useful. A long story, new acronym, or list of unrelated inequalities is unnecessary.

## Editing scope and already clear text

Request: line-edit only, preserving headings, links, and all independent information. Supply an already clear main explanation and a crowded but accurate list of optional considerations.

Inspect whether clear prose stays substantially intact and wider structural changes are suggested separately. If the request instead authorizes structural revision while requiring every detail to survive, check that distinct information receives a recoverable destination rather than disappearing. Scope should determine which intervention is allowed.

## Recording findings

Record the task, skill version, model/settings, inspected outputs, concrete reading obstacles, scientific meaning preserved or lost, and evaluation limits. Avoid a composite “humanity” score. Counts of acronyms or sentences can locate passages to inspect; they do not establish clarity by themselves. A model walkthrough is not a human-reader comprehension trial.
