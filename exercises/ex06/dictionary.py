"""Learning how to do dictionaries."""

__author__ = "730665100"


def invert(input: dict[str, str]) -> dict[str, str]:
    """A function that inverts a dictionary and makes the old values the new keys."""
    inverted_dict: dict[str, str] = {}
    for i in input:
        if (input == input[i]):
            raise KeyError("The dictionary must have unique keys!")
        inverted_dict[input[i]] = i
    return inverted_dict


def favorite_color(fav_color_dict: dict[str, str]) -> str:
    """A function that repeats the color that appears most in the dictionary."""
    count: dict[str, int] = {}
    pop_color: str = ""
    highest_count: int = 0
    for i in fav_color_dict:
        color = fav_color_dict[i]
        if color in count:
            count[color] += 1
        else:
            count[color] = 1
        if count[color] > highest_count or (count[color] == highest_count and pop_color == ""):
            pop_color = color
            highest_count = count[pop_color]
    return pop_color
        

def count(count_list: list[str]) -> dict[str, int]:
    """Counts the items in a dictionary."""
    count_dict: dict[str, int] = {}
    for i in count_list:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict


def alphabetizer(a_list: list[str]) -> dict[str, list[str]]:
    """Sorts a dictionary by the first letter."""
    sorted_dict: dict[str, list[str]] = {}
    for word in a_list:
        if word[0].isalpha():
            letter = word[0].lower()
            if letter not in sorted_dict:
                sorted_dict[letter] = []
            sorted_dict[letter].append(word)
    return sorted_dict
    
    
def update_attendance(calender_dict: dict[str, list[str]], day_of_week: str, student: str) -> dict[str, list[str]]:
    """Makes a dictionary that records attendence."""
    if day_of_week in calender_dict:
        calender_dict[day_of_week].append(student)
    else:
        calender_dict[day_of_week] = [student]
    return calender_dict
        
    