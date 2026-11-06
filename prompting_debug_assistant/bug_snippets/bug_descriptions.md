# Bug Descriptions

## Bug 1 – bug1.py

**Intended behavior:** Return "Pass" for scores of 60 or higher and "Fail" otherwise.

**Issue type:** Syntax error.

**Notes:** The `if score >= 60` statement is missing a colon (`:`), causing a syntax error. The `return "fail":` statement also has an extra colon.

## Bug 2 – bug2.js

**Intended behavior:** Calculate the final price of a product after applying a percentage discount.

**Issue type:** Logical error.

**Notes:** The function adds the discount to the original price instead of subtracting it. For example, a $20 product with a 10% discount incorrectly costs $22 instead of $18.

## Bug 3 – bug3.java

**Intended behavior:** Display the last city from a list.

**Issue type:** Runtime exception.

**Notes:** The code uses `cities.size()` as an index. Since list indexes start at 0, accessing index 3 in a list containing three elements causes an `IndexOutOfBoundsException`.

## Bug 4 – bug4.py

**Intended behavior:** Calculate the sum of all numbers in a list.

**Issue type:** Off-by-one error.

**Notes:** The loop uses `range(len(numbers) - 1)`, which excludes the last element. For the list `[4, 7, 9, 10]`, the function returns 20 instead of 30.

## Bug 5 – bug5.js

**Intended behavior:** Calculate the total price of items in a shopping cart.

**Issue type:** Misuse of data types.

**Notes:** The prices are stored as strings instead of numbers. JavaScript concatenates the strings instead of adding their numerical values, producing "01285" instead of 25.

## Bug 6 – bug6.py

**Intended behavior:** Remove products with zero quantity from an inventory dictionary.

**Issue type:** Runtime exception.

**Notes:** The program attempts to delete dictionary entries while iterating over the same dictionary. This causes `RuntimeError: dictionary changed size during iteration`. The problem can be avoided by iterating over a copy of the dictionary.
