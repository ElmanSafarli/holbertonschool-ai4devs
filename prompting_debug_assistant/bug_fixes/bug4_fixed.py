# Fixed Bug 4: include the last element of the list.
# Intended: sum every number, including the final element.

def sum_numbers(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total

values = [4, 7, 9, 10]
expected = sum(values)
actual = sum_numbers(values)
print("Expected:", expected)
print("Actual:", actual)
