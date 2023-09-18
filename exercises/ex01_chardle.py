"""My code for exercise 01."""

__author__ = "730665617"

word_choice: str = input("Enter a 5-character word: ")

if (len(word_choice) != 5):
    print("Error: Word must contain 5 characters")
    exit()

user_guess: str = input("Enter a single character: ")

if (len(user_guess) != 1):
    print("Error: Character must be a single character.")
    exit()

total_count: int = 0

print("Searching for " + user_guess + " in " + word_choice)

if (user_guess == word_choice[0]):
    print(user_guess + " found at index 0")
    total_count += 1
if (user_guess == word_choice[1]):
    print(user_guess + " found at index 1")
    total_count += 1
if (user_guess == word_choice[2]):
    print(user_guess + " found at index 2")
    total_count += 1
if (user_guess == word_choice[3]):
    print(user_guess + " found at index 3")
    total_count += 1
if (user_guess == word_choice[4]):
    print(user_guess + " found at index 4")
    total_count += 1

if (total_count < 1):
    print("No instances of " + user_guess + " found in " + word_choice)
elif (total_count == 1): 
    print(str(total_count) + " instance of " + user_guess + " found in " + word_choice)
else:
    print(str(total_count) + " instances of " + user_guess + " found in " + word_choice)