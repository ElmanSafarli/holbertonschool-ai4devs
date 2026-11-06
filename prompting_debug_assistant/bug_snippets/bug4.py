# Bug 4: Off-by-one error when summing a list.
# Intended: sum every number, including the final element.

def sum_numbers(numbers):
    total = 0
    for i in range(len(numbers) - 1):
        total += numbers[i]
    return total

values = [4, 7, 9, 10]
expected = sum(values)
actual = sum_numbers(values)
print("Expected:", expected)
print("Actual:", actual)
