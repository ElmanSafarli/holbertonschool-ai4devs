"""Exercise: return the last n values without modifying the input."""


def last_items(values, n):
    """Accept a non-negative integer count."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return []
    start = len(values) - n
    return values[start:-1]


if __name__ == "__main__":
    sample = [10, 20, 30, 40, 50]
    print(last_items(sample, 3))
