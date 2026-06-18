# External Bank FULL1000 Calibration Note

A public-safe summary of a 1,000-item external question-bank replay for observable model-behavior calibration.

---

## Public-safe summary

This note summarizes a 1,000-item external question-bank calibration run used to test whether externally sourced prompts produce observable differences in behavior-category assignment and gate-level routing.

It is not a raw benchmark release, not a model-ranking report, and not a complete disclosure of internal scoring, routing, seed construction, or intervention logic.

The public role of this page is narrower: to make the aggregate calibration signal legible without publishing the raw task bank or private operational machinery.

---

## What was tested

The run used an external question-bank pool as a calibration pressure source.

Public-safe aggregate scope:

| Item | Public-safe value |
|---|---:|
| External items evaluated | 1,000 |
| Source groups | 11 |
| Completed result rows | 1,000 / 1,000 |
| Row-level parse failures | 0 |
| Observed final behavior labels | BRC-1 through BRC-8 all appeared |

The raw question set, full row-level logs, scoring thresholds, private seed templates, and routing logic are intentionally not released here.

---

## Aggregate run result

### Final BRC distribution

| Final label | Count |
|---|---:|
| BRC-1 | 655 |
| BRC-7 | 229 |
| BRC-8 | 39 |
| BRC-6 | 25 |
| BRC-4 | 25 |
| BRC-2 | 12 |
| BRC-5 | 9 |
| BRC-3 | 6 |

Public interpretation:

- all eight final labels appeared;
- the distribution was highly imbalanced;
- rare labels such as BRC-2, BRC-3, and BRC-5 require targeted follow-up rather than broad prevalence claims.

### Gate distribution

| Gate action | Count |
|---|---:|
| HOLD | 885 |
| REVIEW | 36 |
| REJECT | 79 |

Public interpretation:

- gate routing did not collapse into a single REVIEW-only state;
- the run remained heavily weighted toward HOLD;
- gate-level explanation quality still requires schema and timing repair before stronger claims can be made.

---

## Source-effect signal

The replay suggested that source families mattered.

The strongest public-safe finding was not simply that final behavior labels changed, but that external source groups showed a stronger relationship with gate routing than with final behavior label distribution.

Approximate association summary from offline replay:

| Relationship | Association signal | Public reading |
|---|---:|---|
| source group x gate action | 0.506 | strong source-gate effect |
| final BRC x gate action | 0.322 | moderate behavior-gate relationship |
| source group x final BRC | 0.166 | visible but weaker source-label relationship |

This supports using external source families as calibration pressure sources, especially for gate and validation behavior.

It does not support treating any single source group as a universal behavioral benchmark.

---

## Interpretation warning: final label is not raw classifier output

The run exposed an important schema issue.

The public-facing label should not be read as a pure raw classifier argmax. In offline replay, a substantial number of rows showed a difference between the final behavior label and the score-vector argmax label.

Future reports should distinguish at least four layers:

```text
raw score label
score-vector argmax label
post-override final label
coverage-credit label
```

This distinction matters because a final label may include post-processing, bridge rules, fallback handling, or override logic. A public report that collapses those layers would overstate what the run proves.

---

## What this supports

This run supports five bounded claims:

1. A 1,000-item external question-bank replay can complete as a public-safe calibration surface.
2. External source families can create measurable differences in gate routing and behavior-label assignment.
3. Source-aware evaluation is more informative than a single undifferentiated prompt pool.
4. Rare behavior labels require targeted mining and adaptive sampling.
5. External items can be converted into a reusable seed-template substrate, provided the transformation is abstracted and not a verbatim public task release.

---

## What this does not support

This run does not support:

- a claim that BRC-1 through BRC-8 are causally proven categories;
- a claim that all eight labels are equally validated;
- a model-ranking claim;
- publication of the raw 1,000-item task bank;
- disclosure of internal scoring thresholds, seed templates, or gate-routing logic;
- a claim that final labels are identical to raw score-vector argmax labels.

---

## Repair direction derived from the run

The run is useful not because it closes the research line, but because it exposes the next engineering layer.

The next repair direction is:

```text
external question bank
  -> source profile
  -> trigger-feature extraction
  -> seed-template substrate
  -> adaptive rare-class sampler
  -> GBDS validation repair
```

Priority fixes before stronger public claims:

1. split final label, score-vector argmax, override label, and coverage-credit label;
2. recompute gate reasons after final record assembly;
3. preserve full raw score payloads separately from truncated display text;
4. treat rare labels as targeted mining tasks, not as sufficiently validated categories;
5. validate seed-template diversity before using generated seeds as a reusable public method.

---

## Claim ceiling

This page should be read as a calibration note.

Current public claim level:

```text
Meaningful external-bank calibration evidence with schema and rare-class limitations.
```

It is not a final benchmark release, not a reproducibility package, and not a complete operational disclosure.
