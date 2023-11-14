"""One Shot Wordle - Another step to real Wordle!"""

__author__ = "730665100"

secret_word = str("python")
user_input1 = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i = int(0)
user_input_emoji = str()

while user_input1 != secret_word:
    if (len(user_input1) != len(secret_word)):
        user_input1 = str(input("That was not 6 letters! Try again: "))
    else:
        print("Not quite. Play again soon!")
        break

while i < len(secret_word):
    if (user_input1[i] == secret_word[i]):
        user_input_emoji = user_input_emoji + GREEN_BOX
    else:
        if_found = False
        secret_i = int(0)
        while not if_found and secret_i < len(secret_word):
            if (user_input1[i] == secret_word[secret_i]):
                if_found = True
            else:
                secret_i = secret_i + 1
        if (if_found):
            user_input_emoji = user_input_emoji + YELLOW_BOX
        else:
            user_input_emoji = user_input_emoji + WHITE_BOX
    i = i + 1

print(user_input_emoji)

if (user_input1 == secret_word):
    print("Woo! You got it!")