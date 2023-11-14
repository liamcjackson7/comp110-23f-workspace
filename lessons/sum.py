"""Summing the elements of a list using different loops."""

__author__ = "730665100"

vals: list[float] = [1.1, 0.9, 1.0]


def w_sum(vals: list[float]) -> float:
    """Finding the sum with a while loop."""
    i = int(0)
    sum = float(0.0)
    while (i < len(vals)):
        sum = sum + (vals[i])
        i = i + 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Finding a sum with a for loop."""
    i = float(0.0)
    sum = float(0.0)
    for i in vals:
        sum += i
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Finding the sum with a for loop using range."""
    sum = float(0.0)
    for i in range(len(vals)):
        sum += vals[i]
    return sum       