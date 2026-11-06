# Structured Bug Reports

These reports summarize the investigation, root cause, correction, and lessons learned for six intentionally faulty code snippets. Original sources are stored in `bug_snippets/`, corrected versions in `bug_fixes/`, AI analysis in `bug_snippets/ai_debug_log.md`, and test outcomes in `bug_fixes/fix_validation.md`. All referenced paths are relative to `prompting_debug_assistant/`.

## Bug Report – bug1.py

- **File name:** `bug_snippets/bug1.py` (corrected: `bug_fixes/bug1_fixed.py`)
- **Bug summary:** Python raises a `SyntaxError` before running the grade-evaluation program.
- **Root cause:** A colon is missing after `if score >= 60`, while `return "fail":` has an extra colon. Python cannot parse either invalid statement.
- **Resolution (AI suggestion + manual edits):** AI identified the two syntax problems. The corrected version adds the colon to the `if` condition and removes the colon after `return "fail"`. The misspelled function name `evaluted_grade` was kept consistently because it does not prevent execution. Both corrections were necessary; fixing only one would leave the other syntax error.
- **Before:** `if score >= 60` and `return "fail":`
- **After:** `if score >= 60:` and `return "fail"`
- **Validation:** The corrected sample outputs `23: fail`, `321: pass`, `123: pass`. The pass threshold of `60` was also checked. See `bug_fixes/fix_validation.md`.
- **Lessons learned:** Syntax errors can prevent all execution. Read the full parser error and recheck the file after each correction, because multiple syntax defects may coexist.

## Bug Report – bug2.js

- **File name:** `bug_snippets/bug2.js` (corrected: `bug_fixes/bug2_fixed.js`)
- **Bug summary:** The total price increases when a discount should decrease it.
- **Root cause:** The formula uses `price + discount` rather than `price - discount`. The program executes normally, so the defect is logical rather than syntactic.
- **Resolution (AI suggestion + manual edits):** AI recommended subtracting the calculated discount. The corrected file changes only the arithmetic operator; no additional manual changes were required for the sample.
- **Before:** `const finalPrice = price + discount;`
- **After:** `const finalPrice = price - discount;`
- **Validation:** A $20 product discounted by 10% now costs `$18.00` (previously `$22.00`), and a $1000 product discounted by 20% costs `$800.00` (previously `$1200.00`).
- **Lessons learned:** Code can run without throwing errors yet still produce incorrect business results. Test formulas using inputs with easily calculated expected values.

## Bug Report – bug3.java

- **File name:** `bug_snippets/bug3.java` (corrected: `bug_fixes/bug3_fixed.java`)
- **Bug summary:** Requesting the last city throws an `IndexOutOfBoundsException`.
- **Root cause:** Java list indexes begin at zero. For three cities, the last valid index is `2`, but `cities.size()` returns `3`.
- **Resolution (AI suggestion + manual edits):** AI proposed using `cities.size() - 1`. The corrected source uses that index; no extra edit was needed for the non-empty sample. For production use, an empty-list guard would also be important.
- **Before:** `int lastIndex = cities.size();`
- **After:** `int lastIndex = cities.size() - 1;`
- **Validation:** The corrected program compiles and outputs `Last city: Astana`. The tested sample contains `Baku`, `Tbilisi`, and `Astana`.
- **Lessons learned:** The number of elements is not the index of the last element. Handle index boundaries explicitly and consider empty collections.

## Bug Report – bug4.py

- **File name:** `bug_snippets/bug4.py` (corrected: `bug_fixes/bug4_fixed.py`)
- **Bug summary:** The total excludes the final list element.
- **Root cause:** `range(len(numbers) - 1)` stops before the final index, creating an off-by-one error.
- **Resolution (AI suggestion + manual edits):** AI recommended `range(len(numbers))`. That single range-bound change was applied. The alternative approach `for number in numbers` would also avoid manual index management, but was not needed.
- **Before:** `for i in range(len(numbers) - 1):`
- **After:** `for i in range(len(numbers)):`
- **Validation:** The sample `[4, 7, 9, 10]` now sums to `30` instead of `20`. Empty and one-element lists were also considered in validation.
- **Lessons learned:** Test loop boundaries, especially the first and last element. Minimal test cases expose off-by-one mistakes quickly.

## Bug Report – bug5.js

- **File name:** `bug_snippets/bug5.js` (corrected: `bug_fixes/bug5_fixed.js`)
- **Bug summary:** The shopping cart total is the text `"01285"` instead of the number `25`.
- **Root cause:** Item prices arrive as strings. JavaScript's `+` operator concatenates a string operand instead of performing numeric addition.
- **Resolution (AI suggestion + manual edits):** AI suggested converting each price to a number before addition; the corrected file uses `Number(price)`. No manual change beyond the conversion was necessary for valid numeric input. Real applications should reject invalid strings that convert to `NaN`.
- **Before:** `total += price;`
- **After:** `total += Number(price);`
- **Validation:** Input `["12", "8", "5"]` now gives `25` rather than `"01285"`; decimal-string prices `["1.5", "2.5"]` give `4`.
- **Lessons learned:** Validate the types of values received from forms or external data sources. Explicit numeric conversion prevents silent string concatenation.

## Bug Report – bug6.py

- **File name:** `bug_snippets/bug6.py` (corrected: `bug_fixes/bug6_fixed.py`)
- **Bug summary:** Removing out-of-stock products raises `RuntimeError: dictionary changed size during iteration`.
- **Root cause:** The code deletes keys from `inventory` while iterating over the live `inventory.items()` view. The dictionary's size changes during iteration.
- **Resolution (AI suggestion + manual edits):** AI recommended iterating over `inventory.copy().items()` while deleting from the original dictionary. This one-line adjustment was applied. An alternative would build a new filtered dictionary, but that approach was not needed for this fix.
- **Before:** `for item, quantity in inventory.items():`
- **After:** `for item, quantity in inventory.copy().items():`
- **Validation:** The corrected result is `{'apples': 5, 'oranges': 3}`; zero-stock `bananas` and `pears` are removed without an exception. Empty and single-item inventory cases were also documented.
- **Lessons learned:** Avoid changing a collection's size while iterating over it. Iterate over a snapshot or create a filtered collection instead.

## Overall Findings

- **Bug categories:** Syntax, logic, runtime exceptions, off-by-one, and data-type misuse.
- **Resolution method:** AI-assisted diagnosis, targeted source changes, and validation against expected outputs.
- **Outcome:** Six separate corrected files and their validation notes are documented under `bug_fixes/`. The originals under `bug_snippets/` remain intentionally buggy.
- **Key lesson:** Debug systematically: reproduce the failure, identify the root cause, apply a minimal correction, and validate both normal and boundary inputs.
