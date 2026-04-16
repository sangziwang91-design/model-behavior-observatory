# AI Behavior Audit Demo Report

## Case Insert · Seed Injection Behavior Audit (20-Round AB Test)

### Scenario
This case evaluates how an AI model handles **unknown or weakly verified topics** under two conditions:

- **Baseline**: no structured prompt influence
- **Injection**: structured seed framing applied before evaluation

The purpose is to observe whether structured inputs change:
- boundary awareness
- explanation behavior
- practical deployment risk

---

## Core Results

### Baseline
- Fabrication Risk: **0.10**
- Boundary Retention: **0.90**
- Expansion Tendency: **0.25**
- Distortion Tendency: **0.30**

**Observed behavior:**
The model remains relatively cautious and keeps clearer boundaries when the topic is not strongly framed in advance.

### Injection
- Fabrication Risk: **0.20**
- Boundary Retention: **0.75**
- Expansion Tendency: **0.80**
- Distortion Tendency: **0.75**

**Observed behavior:**
The model becomes much more likely to expand an unverified topic into a more developed explanation structure.

---

## Delta Summary
- Fabrication Risk: **+0.10**
- Boundary Retention: **-0.15**
- Expansion Tendency: **+0.55**
- Distortion Tendency: **+0.45**

---

## Risk Interpretation
The main effect is **not** a sudden jump in outright false claims.

The stronger effect is this:

> A structured seed can make an unverified topic sound more complete, more coherent, and more mature than the available evidence supports.

This creates a practical risk of **credibility inflation** in public-facing uses.

---

## Why This Matters
In scenarios such as:
- AI search assistance
- product explanation layers
- concept exploration
- early-stage research support

structured prompting may increase the chance that the system presents a weakly grounded topic with excessive explanatory confidence.

In simple terms:

> the answer may sound better organized without becoming more reliable.

---

## Deployment Reading
### Baseline Condition
- Overall risk: **relatively low**
- Suitable when unknown-topic handling must remain conservative

### Injection Condition
- Overall risk: **moderately elevated**
- Requires additional verification controls

### Overall Assessment
- Injection Effect Profile: **Strong**
- Recommended stance: **usable with safeguards**

---

## Recommended Safeguards
1. Add an explicit verification step before interpretation.
2. Separate verified facts from conceptual explanation.
3. Avoid letting structured prompts imply external factual support.
4. Add review or policy checks in unknown-topic workflows.

---

## Client-Facing Summary
This case demonstrates that structured prompt framing can significantly increase explanation richness, but may also introduce subtle reliability risk if verification controls are not in place.

---

> Public demo version only. This file intentionally excludes internal scoring logic, control rules, and reconstruction paths.
