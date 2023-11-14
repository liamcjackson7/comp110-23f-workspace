"""Learning to work with lsits."""

__author__ = "730665100"


def all(given_list: list[int], given_int: int) -> bool:
    """Given a list see if it matches an int."""
    i = int(0)
    if (len(given_list)) == 0:
        return False
    while (i < len(given_list)):
        if (given_list[i] != given_int):
            return False
        i = i + 1
    return True


def max(input: list[int]) -> int:
    """Given a list max should return the largest int in the list."""
    i = int(0)
    found_max = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while (i < len(input)):
        if (input[i] >= found_max):
            found_max = input[i]
        i = i + 1
    return found_max


def is_equal(int_list1: list[int], int_list2: list[int]) -> bool:
    """Given two lists of int check if their all equal."""
    i = int(0)
    if len(int_list1) != len(int_list2):
        return False
    if (len(int_list1) and len(int_list2)) == 0:
        return True
    while (i < len(int_list1)):
        if (int_list1[i] != int_list2[i]):
            return False
        i = i + 1
    return True