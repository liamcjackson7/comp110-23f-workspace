"""Test my zip function."""

__author__ = "730665100"

from lessons.zip import zip


def test_emptylist() -> bool:
    """py.test to see if there is an empty list."""
    d = zip([], [])
    if d == {}:
        return True
    else:
        return False


def test_unevenlist() -> bool:
    """py.test to see if length of lists are different."""
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3, 4]
    d = zip(list1, list2)
    if d == {}:
        return True
    else:
        return False
    
    
def test_validlist() -> bool:
    """Test to see if a list is valid."""
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    d = zip(list1, list2)
    if d == {"a": 1, "b": 2, "c": 3}:
        return True
    else:
        return False
    