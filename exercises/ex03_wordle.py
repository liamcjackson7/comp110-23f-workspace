"""The structured Worlde!"""

__author__ = "730665100"

i = int(0)
emoji = str()
guess_number = int(1)
guess_len = int(5)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def  contains_char(answer: str, input_char: str) -> bool:
    """A function that will called multiple times to see if a certain character is found in the user's input."""
    assert len(input_char) == 1
    i = 0
    while (i < len(answer)):
        if (input_char == answer[i]):
            return True
        i = i + 1
    return False
    
    
def emojified(user_input: str, answer: str) -> str:
    """Prints the green, yellow, and white boxes is response to the user input."""
    i = 0
    emojified_string = ""
    assert len(user_input) == len(answer)
    while (i < len(answer)):
        if (user_input[i] == answer[i]):
            emojified_string = emojified_string + GREEN_BOX
        else:
            if contains_char(answer, user_input[i]):
                emojified_string = emojified_string + YELLOW_BOX
            else:
                emojified_string = emojified_string + WHITE_BOX
        i = i + 1
    return emojified_string

def input_guess(exp_length: int) -> str:
    """Checks if the length of the word is what is expected."""
    user_input = ""
    user_input = str(input(f"Enter a {exp_length} character word: "))
    if (len(user_input) != exp_length):
        user_input = str(input(f"That wasn't {exp_length} chars! Try again: "))
    return user_input
    
def main() -> None: 
    """The main is what brings the whole function together by calling the other functions."""
    answer = str("codes")
    user_input = ""
    guess_number = int(0)
    while (guess_number <= 5 and answer != user_input):
        guess_number = guess_number + 1
        print(f"=== Turn {guess_number}/6 ===")
        user_input = input_guess(guess_len)
        correctness = emojified(user_input, "codes")
        print(correctness)
        if (user_input == answer):
            print(f"You won in {guess_number}/6 turns!")
        if (guess_number >= 6):
            print("X/6 - Sorry, try again tomorrow!")
        
if __name__ == "__main__":
    main()
    
    