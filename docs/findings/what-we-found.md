# What We Found

This repository is built around a core practical observation:

> Models can sound more certain, structured, and internally consistent than the evidence securely supports.

This is not a claim that models are always wrong.

It is a claim that:

> confidence, structure, and fluency are weaker signals of reliability than many users assume.

---

## Public findings

### F1 — Confidence gap

A model can produce language that appears settled, credible, and technically grounded even when reliable evidence is incomplete or weak.

---

### F2 — Structure can outrun evidence

Models tend to organize incomplete or weakly grounded topics into structured frameworks before the available evidence justifies those structures.

---

### F3 — Expansion precedes fabrication

Before producing outright falsehoods, models often expand unverified topics into plausible-looking research directions, frameworks, or mechanisms.

---

### F4 — Observation, not remediation

This repository exposes behavioral patterns.
It does not attempt to fix or patch them.

---

### F5 — Uncertainty smoothing

Models often soften, generalize, or redistribute uncertainty rather than clearly exposing it.

This can make low-confidence outputs appear more stable than they are.

---

### F6 — Context adaptation

Models adapt to user language, framing, and context.

In extended interaction, this can produce outputs that mirror the user’s conceptual structure rather than independently grounded reasoning.

---

### F7 — Incomplete input, no halt

A model may correctly identify missing information or incomplete coverage and still continue execution.

This reflects a process-level issue rather than a single content error.

---

### F8 — Structured explanation surface

Models can generate outputs that resemble:

- system documentation
- internal rules
- audit reports
- source-backed explanations

These structures can appear more grounded than they actually are.

---

### F9 — Self-report reliability gap

When asked to describe their own behavior, limits, or rules, models often generate coherent and structured self-explanations.

However:

> such self-descriptions should be treated as behavioral samples, not mechanism proofs.

---

### F10 — Boundary redirection

Instead of stopping at capability or policy limits, models often redirect outputs into safer generalizations, principles, or adjacent explanations.

---

### F11 — Collapse under forced grounding

When required to explicitly ground claims in verifiable evidence, some structured or plausible outputs may partially or fully collapse.

---

## Why this matters

Many users evaluate AI outputs through surface signals:

- fluency
- structure
- confidence

But a model can be:

- structured without being grounded
- coherent without being correct
- careful-sounding without being well-calibrated
- self-explanatory without being transparent

This repository exists to make those gaps easier to see.

---

## Reading rule

While reading any output, ask not only:

- "Does this sound reasonable?"

Also ask:

- "Where does secure grounding end?"
- "What is being assumed or completed?"
- "Is structure substituting for evidence?"
- "Is the model explaining itself — and should that explanation be trusted?"
