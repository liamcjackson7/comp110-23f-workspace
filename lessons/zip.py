"""Combining two lists into a dictionary."""

__author__ = "730665100"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """A function that zips two lists together."""
    if (len(list1) == 0 or len(list2) == 0):
        return {}
    if (len(list1) != len(list2)):
        return {}
    dictionary = {}
    for i in range(len(list1)):
        dictionary[list1[i]] = list2[i]
    return dictionary