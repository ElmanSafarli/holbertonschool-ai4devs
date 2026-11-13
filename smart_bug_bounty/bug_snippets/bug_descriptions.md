# Bug Descriptions

## Scope
Six original, intentionally flawed snippets for Smart Bug Bounty Task 0.
Languages: Python 3, JavaScript (Node.js/CommonJS), and Java.
Each source file contains 10–40 physical lines and runs independently without
third-party dependencies. These are local debugging exercises, not production code.
No fixes are included at this collection stage.

## bug1.py — Last N items
- **Language:** Python.
- **Intended Behavior:** Return the last n values in original order without changing the input. Zero returns an empty list; n greater than the list length returns the entire list.
- **Current Issue:** The slice excludes the final element and calculates an unsuitable starting position for oversized counts.
- **Reproduction:** Run `python smart_bug_bounty/bug_snippets/bug1.py`.
- **Expected:** `[30, 40, 50]`.
- **Actual:** `[30, 40]`.
- **Later validation cases:** n = 0, 1, list length, oversized n, empty input, and negative n.

## bug2.js — Cart total
- **Language:** JavaScript.
- **Intended Behavior:** Sum price multiplied by quantity for every item. An empty cart returns zero. This exercise uses finite non-negative integer prices and quantities.
- **Current Issue:** The loop stops before processing the final item.
- **Reproduction:** Run `node smart_bug_bounty/bug_snippets/bug2.js`.
- **Expected:** `35`.
- **Actual:** `20`.
- **Later validation cases:** Empty cart, one item, multiple items, and zero quantity.

## bug3.java — Arithmetic mean
- **Language:** Java.
- **Intended Behavior:** Return the arithmetic mean as a double, preserving fractional results; reject an empty array.
- **Current Issue:** Integer division truncates the fraction before the result is converted to double.
- **Reproduction:** From this folder, run `javac bug3.java`, then `java Bug3`.
- **Expected:** `1.5` for [1, 2].
- **Actual (derived from integer-division semantics):** `1.0`.
- **Later validation cases:** Fractional mean, negative values, one value, and empty array.

## bug4.py — Independent tag lists
- **Language:** Python.
- **Intended Behavior:** Each call without an explicit list creates an independent list; an explicitly supplied list is appended to in place.
- **Current Issue:** The mutable default list is shared by calls, leaking tags between otherwise independent operations.
- **Reproduction:** Run `python smart_bug_bounty/bug_snippets/bug4.py`.
- **Expected:** First: ['security']; Second: ['performance'].
- **Actual:** Both printed lists contain ['security', 'performance'].
- **Later validation cases:** Repeated omitted-list calls, explicit empty list, separate supplied lists, and blank tag rejection.

## bug5.js — Asynchronous user loading
- **Language:** JavaScript.
- **Intended Behavior:** Resolve only after every fetch completes, return users in input-ID order, and propagate a fetch rejection to the caller.
- **Current Issue:** forEach does not await asynchronous callbacks. The returned array can be observed before completion, later mutates, and does not coordinate callback failures or result order.
- **Reproduction:** Run `node smart_bug_bounty/bug_snippets/bug5.js`. The immediate mock may hide the bug; use the delayed-fetch reproduction below for a reliable failure.
- **Deterministic reproduction from this folder:**
  ```sh
  node -e 'const {loadUsers}=require("./bug5.js"); const fetchUser=id=>new Promise(resolve=>setTimeout(()=>resolve({id}),10)); loadUsers([1,2],fetchUser).then(users=>console.log(JSON.stringify(users)));'
  ```
- **Expected:** `[{"id":1},{"id":2}]` after both fetches complete.
- **Actual with delayed fetch:** `[]` at promise resolution.
- **Later validation cases:** Delayed responses finishing out of order, empty IDs, rejected fetch, and repeated calls.

## bug6.java — Role text comparison
- **Language:** Java.
- **Intended Behavior:** Return true exactly when the role text equals "admin"; return false for null and other roles.
- **Current Issue:** Reference comparison can reject a separately allocated string containing the same characters.
- **Reproduction:** From this folder, run `javac bug6.java`, then `java Bug6`.
- **Expected:** First line true; second line false.
- **Actual (derived from reference-comparison semantics):** Both lines false.
- **Later validation cases:** String literal, newly allocated equal string, viewer role, null, and uppercase ADMIN (false under this case-sensitive contract).
- **Security scope:** This is a comparison exercise; it does not authenticate users or implement a complete authorization system.

## Collection validation
- Confirmed six source files in three languages, each 10–40 physical lines.
- Executed Python and JavaScript reproductions, including the delayed asynchronous case.
- Java snippets were inspected but not compiled or executed: no Java compiler is installed in the available environment. Java outputs above are reasoned expectations, not recorded execution results.
