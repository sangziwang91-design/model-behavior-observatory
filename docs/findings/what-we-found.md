# What We Found

This repository is built around one practical observation:

> Models can sound more confident than the evidence supports.

That does **not** mean every confident answer is wrong.
It means confidence is a weaker reliability signal than many users assume.

## Public findings

### F1 — Confidence gap
A model can produce language that sounds settled, structured, and credible even when reliable truth is not securely available.

### F2 — Structure can outrun evidence
When a topic is framed with enough narrative or methodological structure, the model may begin organizing the topic into a plausible-looking frame before the evidence justifies that move.

### F3 — Expansion often arrives before outright fabrication
The most important failure mode is not always direct falsehood.
Often it begins with theory inflation: an unverified topic starts to sound like a legitimate research direction, framework, or mechanism.

### F4 — Observation, not remediation
This protocol is designed to expose response behavior.
It is **not** a patch, defense, or alignment fix.
Its value is diagnostic visibility.

### F7 — Incomplete input, no halt
A model may correctly explain that it should stop when task coverage is incomplete — and still continue execution anyway.
This is a process-level weakness, not just a content error.

## Why this matters

Most users do not inspect the full path from uncertainty to answer.
They hear confidence, structure, and fluency — and treat those as rough proxies for reliability.

This repository exists to make that shortcut easier to question.
