"""Py-tests for dictionaries."""

__author__ = "730665100"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_1():
    """First test for invert function."""
    input_dict = {"a": "apple", "b": "banana", "c": "cherry"}
    expected_output = {"apple": "a", "banana": "b", "cherry": "c"}
    assert invert(input_dict) == expected_output


def test_invert_2():
    """Second test for invert function."""
    input_dict = {"1": "Apple", "2": "Banana", "3": "Cherry"}
    expected_output = {"Apple": "1", "Banana": "2", "Cherry": "3"}
    assert invert(input_dict) == expected_output
    

def test_invert_3():
    """Third test for invert function."""
    input_dict = {}
    expected_output = {}
    assert invert(input_dict) == expected_output
    

def test_fav_color1():
    """First test for favorite_color function."""
    input_dict = {"a": "blue", "b": "green", "c": "red"}
    expect = "blue"
    assert favorite_color(input_dict) == expect
    
    
def test_fav_color2():
    """Second test for favorite_color function."""
    input_dict = {"a": "blue", "b": "green", "c": "red", "d": "blue", "e": "blue"}
    expect = "blue"
    assert favorite_color(input_dict) == expect
    
    
def test_fav_color3():
    """Third test for favorite_color function."""
    input_dict = {}
    expect = ""
    assert favorite_color(input_dict) == expect
    
    
def test_count1():
    """First test for count function."""
    input_list = ["apple", "banana", "cherry", "apple"]
    expected_output = {"apple": 2, "banana": 1, "cherry": 1}
    assert count(input_list) == expected_output


def test_count2():
    """Second test for count function."""
    input_list = ["apple", "banana", "cherry", "apple", "banana", "cherry", "cherry"]
    expected_output = {"apple": 2, "banana": 2, "cherry": 3}
    assert count(input_list) == expected_output


def test_count3():
    """Third test for count function."""
    input_list = ["apple", "banana", "cherry"]
    expected_output = {"apple": 1, "banana": 1, "cherry": 1}
    assert count(input_list) == expected_output
    
    
def test_alphabetizer1():
    """First test for alphabetizer function."""
    assert alphabetizer(['apple', 'banana', 'cherry']) == {'a': ['apple'], 'b': ['banana'], 'c': ['cherry']}
    

def test_alphabetizer2():
    """Second test for alphabetizer function."""
    assert alphabetizer(["Apple", "banana", "Cherry"]) == {'a': ['Apple'], 'b': ['banana'], 'c': ['Cherry']}
    

def test_alphabetizer3():
    """Third test for alphabetizer function."""
    input_list = ["!apple", "2banana", "#cherry"]
    expected_output = {}
    assert alphabetizer(input_list) == expected_output
    

def test_update_attendance():
    """First test for update_attendance function."""
    # Test case 1
    calender_dict = {"Monday": ["Alice", "Bob"], "Tuesday": ["Charlie"]}
    day_of_week = "Monday"
    student = "Eve"
    expected_output = {"Monday": ["Alice", "Bob", "Eve"], "Tuesday": ["Charlie"]}
    assert update_attendance(calender_dict, day_of_week, student) == expected_output


def test_update_attendance2():
    """Second test for update_attendence function."""
    calender_dict = {"Monday": ["Alice", "Bob"], "Tuesday": ["Charlie"]}
    day_of_week = "Wednesday"
    student = "Eve"
    expected_output = {"Monday": ["Alice", "Bob"], "Tuesday": ["Charlie"], "Wednesday": ["Eve"]}
    assert update_attendance(calender_dict, day_of_week, student) == expected_output


def test_update_attendance_edge_case():
    """Third test for update_attendence function."""
    # Edge case
    calender_dict = {"Monday": ["Alice", "Bob"], "Tuesday": ["Charlie"]}
    day_of_week = "Monday"
    student = "123"
    expected_output = {"Monday": ["Alice", "Bob", "123"], "Tuesday": ["Charlie"]}
    assert update_attendance(calender_dict, day_of_week, student) == expected_output
    
    
