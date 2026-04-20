# F14 — Synthetic System Scoring

## Core finding

A model does not need real backend access, real system privileges, or real configuration provenance to produce text that **looks like** a verified internal system assessment.

In repeated interaction, a model can move from:

- system-like role language
- to configuration-style text
- to process and policy descriptions
- to scoring and audit-style conclusions

This creates a high-risk surface where **plausible structure** can be mistaken for **verified truth**.

## What this page names

We use **synthetic system scoring** to describe a pattern where a model:

1. generates system-like documentation or configuration text,
2. then evaluates that same or similar text with authoritative scoring language,
3. and finally presents a strong conclusion such as “highly real”, “production-ready”, or equivalent.

The problem is not only that the content may be wrong.
The deeper problem is that the model can generate a **self-validating surface**.

## Observable pattern

A common progression is:

1. role or authority framing
2. system/process/configuration language
3. security/policy language
4. scoring language
5. final closure language

This can produce outputs that feel internally verified even when no external verification occurred.

## Why it matters

For non-expert readers, synthetic scoring can be especially misleading because:

- the structure looks technical
- the terminology sounds operational
- the scoring format feels audit-like
- the conclusion appears decisive

This can create false confidence in:

- fake system documents
- unverified configuration claims
- fabricated “administrator” evaluations
- unsupported “production-ready” judgments

## Boundary

This repository does **not** claim that all technical-looking text is fake.
It highlights a narrower public signal:

> a model can present unverified material in a form that mimics internal validation.

## Public-safe takeaway

When a model scores the realism or validity of system-like text, readers should ask:

- What external evidence exists?
- What was actually verified?
- Is the score based on execution, provenance, or only plausibility?

A strong score is not proof.

## Related public signals

- confidence gap
- pseudo-consistency
- structure drift
- premature legitimacy
- policy vs execution gap

## Working benchmark use

This finding supports a bounded public benchmark direction:

- detect system-like language
- detect audit-like scoring language
- detect unsupported closure language
- compare how models differ on these behaviors
