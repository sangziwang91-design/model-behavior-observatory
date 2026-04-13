# Public Report Template

_This template is a public-facing structure for reporting on model behavior. It is intentionally limited to observable phenomena and does not include any private scoring, weighting, or adjudication logic._

---

### **Evaluation Case:** [Brief, descriptive title of the evaluation]

*   **Model(s):** [Model name and version]
*   **Date:** [YYYY-MM-DD]

---

### 1. Input

```
[The full, verbatim input prompt or query given to the model]
```

### 2. Observed Behavior

*   **Summary:** [A concise, neutral summary of the model's response.]
*   **Key Characteristics:** [Bulleted list of notable behavioral traits, e.g., "Responded in a formal tone," "Refused to answer a sensitive question," "Generated code with a specific error."]

### 3. Drift Signals

*   **Comparison Baseline:** [Reference to a previous evaluation or expected behavior.]
*   **Observed Drift:** [Description of how the current behavior deviates from the baseline, if at all.]

### 4. Failure Pattern

*   **Pattern Classification:** [Name of the failure pattern from the public taxonomy, e.g., "Instruction Following Failure," "Factual Hallucination."]
*   **Description:** [Explanation of how the model's behavior fits this pattern, with specific quotes or examples from the output.]

### 5. Reliability Notes

*   **Overall Assessment:** [A brief, qualitative note on the perceived reliability of the model in this specific case.]
*   **Confidence:** [High/Medium/Low] - Confidence in the assessment of the behavior.

### 6. Open Questions

*   [A list of questions for further investigation that arose from this evaluation. E.g., "Would a slightly different prompt have avoided this failure mode?", "Is this behavior consistent across other models in the same family?"]
