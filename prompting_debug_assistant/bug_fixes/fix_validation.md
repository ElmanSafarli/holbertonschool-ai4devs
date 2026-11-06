# Fix Validation

The fixed versions were tested locally with Python 3, Node.js, and Java (`javac`/`java`). All six corrected programs executed successfully. Original files in `bug_snippets/` were not changed.

## Bug 1 – bug1_fixed.py

**Fix:** Add the missing colon after `if score >= 60` and remove the invalid colon after `return "fail"`.

**Input:** `scores = [23, 321, 123]`

**Expected Output:**
```text
23: fail
321: pass
123: pass
```

**Actual Output:** Matches expected output. ✅ PASS

**Additional tests:** `23 -> fail`, `60 -> pass`, `99 -> pass`. ✅ PASS

**Manual tweaks:** Both syntax problems had to be corrected; a colon was missing on the `if` line and an extra one was present after `return "fail"`.

## Bug 2 – bug2_fixed.js

**Fix:** Subtract the calculated discount from the original price instead of adding it.

**Input:** Products priced at `20` (10% discount) and `1000` (20% discount).

**Expected Output:**
```text
book: $18.00
book: $800.00
```

**Actual Output:** Matches expected output. ✅ PASS

**Additional tests:** `finalPrice(20, 10) = 18`, `finalPrice(1000, 20) = 800`, `finalPrice(0, 20) = 0`. ✅ PASS

## Bug 3 – bug3_fixed.java

**Fix:** Use `cities.size() - 1` for the index of the last element.

**Input:** `["Baku", "Tbilisi", "Astana"]`

**Expected Output:** `Last city: Astana`

**Actual Output:** `Last city: Astana` ✅ PASS

**Test method:** Compiled with `javac` and executed with `java`.

**Scope:** The supplied list is non-empty. For a potentially empty list, check `cities.isEmpty()` before accessing its last item.

## Bug 4 – bug4_fixed.py

**Fix:** Use `range(len(numbers))` to include the last item.

**Input:** `[4, 7, 9, 10]`

**Expected Output:**
```text
Expected: 30
Actual: 30
```

**Actual Output:** Matches expected output. ✅ PASS

**Additional tests:** Empty list `[] -> 0`; one-element list `[7] -> 7`; sample list `[4, 7, 9, 10] -> 30`. ✅ PASS

## Bug 5 – bug5_fixed.js

**Fix:** Change `total += price` to `total += Number(price)` to sum numeric values rather than concatenate strings.

**Input:** `["12", "8", "5"]`

**Expected Output:**
```text
Cart total: 25
Expected cart total: 25
```

**Actual Output:** Matches expected output. ✅ PASS

**Additional tests:** `[] -> 0`; `["1.5", "2.5"] -> 4`. ✅ PASS

**Scope:** Inputs are valid numeric strings. Production code should validate invalid conversions, such as `Number("abc")`.

## Bug 6 – bug6_fixed.py

**Fix:** Iterate over `inventory.copy().items()` so deletion does not change the dictionary currently being iterated.

**Input:** `{"apples": 5, "bananas": 0, "oranges": 3, "pears": 0}`

**Expected Output:** `Available stock: {'apples': 5, 'oranges': 3}`

**Actual Output:** Matches expected output; no `RuntimeError`. ✅ PASS

**Additional tests:** Single zero-stock item `{"empty": 0} -> {}`; empty dictionary `{} -> {}`. ✅ PASS

## Overall Result

**6/6 corrected snippets passed execution tests.** The sample outputs matched the intended behavior; additional edge cases passed for Python and JavaScript. Files were created under `prompting_debug_assistant/bug_fixes/` with the original bug numbers and `_fixed` suffix. The source snippets remain unchanged.
