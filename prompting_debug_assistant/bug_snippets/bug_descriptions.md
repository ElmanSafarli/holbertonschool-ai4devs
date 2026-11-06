# Bug Descriptions

## Bug 1 - `bug1.py`
- **Language:** Python
- **Intended Behavior:** Return "Pass" for scores of 60 or higher and "Fail" otherwise.
- **Issue Type:** Syntax error.
- **Notes:** The `if score >= 60` statement is missing a colon (`:`), so Python cannot parse the file.

## Bug 2 - `bug2.js`
- **Language:** JavaScript
- **Intended Behavior:** Subtract the percentage discount from the original product price.
- **Issue Type:** Logical error.
- **Notes:** The function adds the computed discount instead of subtracting it. A $20 item with a 10% discount incorrectly costs $22 rather than $18.

## Bug 3 - `bug3.java`
- **Language:** Java
- **Intended Behavior:** Print the last city in the list.
- **Issue Type:** Runtime exception (index out of bounds).
- **Notes:** A list of size 3 has valid indexes 0 through 2. `cities.get(cities.size())` accesses index 3 and throws `IndexOutOfBoundsException`.

## Bug 4 - `bug4.py`
- **Language:** Python
- **Intended Behavior:** Sum all the elements of a list.
- **Issue Type:** Off-by-one error.
- **Notes:** The loop uses `range(len(numbers) - 1)`, skipping the last number. For `[4, 7, 9, 10]`, it returns 20 instead of 30.

## Bug 5 - `bug5.js`
- **Language:** JavaScript
- **Intended Behavior:** Add prices from a form as numbers.
- **Issue Type:** Misuse of data types.
- **Notes:** The form prices are strings, and JavaScript's `+` operator concatenates them. The result is `01285`, not the numeric total 25.

## Bug 6 - `bug6.py`
- **Language:** Python
- **Intended Behavior:** Remove products with zero quantity from an inventory dictionary.
- **Issue Type:** Runtime exception (dictionary mutation during iteration).
- **Notes:** The code deletes keys from a dictionary while iterating over `inventory.items()`, causing `RuntimeError: dictionary changed size during iteration`.
