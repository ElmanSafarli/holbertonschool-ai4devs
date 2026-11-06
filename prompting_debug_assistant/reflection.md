# Reflection on AI-Assisted Debugging

## Introduction

In this project, I used an AI assistant to investigate six intentionally buggy programs written in Python, JavaScript, and Java. The examples covered syntax errors, incorrect discount calculations, invalid list indexes, off-by-one mistakes, string concatenation instead of addition, and modifying a dictionary during iteration. I compared AI explanations with the original code, created corrected versions, and documented the expected results. This exercise showed that AI can accelerate debugging, but its suggestions still require careful human verification.

## AI Strengths

The easiest issues for AI were errors with recognizable patterns. In `bug1.py`, it quickly identified the missing colon after an `if` statement and the extra colon after `return`. In `bug3.java`, it explained why accessing index `cities.size()` throws an exception: list indexes start at zero. The dictionary mutation error in `bug6.py` was also straightforward to diagnose. AI was especially helpful because it explained not only what to change, but why the original code failed.

AI also helped with less obvious logical issues. In `bug2.js`, the program ran but added a discount instead of subtracting it. In `bug5.js`, numeric-looking strings were silently concatenated. Concrete examples made these mistakes easy to understand.

## AI Weaknesses and Trust

The hardest aspect was not always finding a one-line fix; it was deciding whether the proposed change fully met the intended behavior. For example, changing `cities.size()` to `cities.size() - 1` solves the Java example with three cities, but it still fails on an empty list. Similarly, `Number(price)` fixes valid numeric strings yet can produce `NaN` for invalid input.

I therefore treated AI suggestions as hypotheses, not guarantees. My trust was highest when the explanation matched the language rules and the output could be checked independently. I trusted AI less when it made broad claims without testing edge cases.

## Human Role and Manual Intervention

Human judgment mattered when selecting the correct behavior and reviewing the fixes. The grade evaluator had two syntax defects, so correcting only the first would not be sufficient. I also needed to decide that a discount must reduce the price and that zero-stock products should disappear from the final inventory.

The validation process compared actual outputs with expected values, including boundary cases such as a passing score of 60, an empty list, and decimal shopping-cart prices. Documentation was another human responsibility: the AI-generated explanations needed a consistent structure that clearly separated diagnosis, resolution, and test results.

## Conclusion

AI made debugging faster by recognizing common mistakes, explaining unfamiliar exceptions, and proposing targeted fixes. However, it did not replace understanding the program's requirements or checking its behavior. My main lesson is to combine AI analysis with reproducible tests: identify the failure, inspect the reasoning, apply the smallest reasonable change, and verify normal and edge cases. In real-world development, AI is best used as a debugging partner, while the developer remains responsible for correctness, safety, and maintainability.
