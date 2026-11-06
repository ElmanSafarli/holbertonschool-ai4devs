# Fixed Bug 1: repair missing/extra colons in the grade evaluator.

def evaluted_grade(score):
    if score >= 60:
        return "pass"
    else:
        return "fail"

scores = [23, 321, 123]

for score in scores:
    result = evaluted_grade(score)
    print(f"{score}: {result}")
