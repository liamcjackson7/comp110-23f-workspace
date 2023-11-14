"""EX01 Chardle - Step towards Wordle!"""

__author__ = "730665100"

index_count: int = 0
user_input1 = input("Enter a 5-character word: ")

if (len(user_input1) != 5):
    print("Error: Word must contain 5 characters")
    exit()

user_input2 = input("Enter a single character: ")

if (len(user_input2) != 1):
    print("Error: Character must be a single character")
    exit()

print("searching for " + str(user_input2) + " in " + str(user_input1))

if (user_input2 == user_input1[0]):
    print(str(user_input2) + " found at index 0")
    index_count = index_count + 1
    
if (user_input2 == user_input1[1]):
    print(str(user_input2) + " found at index 1")
    index_count = index_count + 1
    
if (user_input2 == user_input1[2]):
    print(str(user_input2) + " found at index 2")
    index_count = index_count + 1
    
if (user_input2 == user_input1[3]):
    print(str(user_input2) + " found at index 3")
    index_count = index_count + 1
    
if (user_input2 == user_input1[4]):
    print(str(user_input2) + " found at index 4")
    index_count = index_count + 1
    
if (index_count == 1):
    print(str(index_count) + " instance of " + str(user_input2) + " found in " + str(user_input1))
    
elif (index_count > 1):
    print(str(index_count) + " instances of " + str(user_input2) + " found in " + str(user_input1))
else:
    print("No instances of " + str(user_input2) + " found in " + str(user_input1))