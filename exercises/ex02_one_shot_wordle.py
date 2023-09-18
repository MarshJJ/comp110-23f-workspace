"""My code for exercise 02."""

__author__ = "730665617"

secret_word: str = "python"

user_guess: str

real_guess: int = 0

while (real_guess < 1):
    user_guess = input("What is your 6-letter guess? ")
    if (len(user_guess) != len(secret_word)):
        print("That was not 6 letters! Try again: ")
    else:
        if (user_guess == secret_word):
            print("Woo! You got it!")
            real_guess += 1
        else:
            print("Not quite. Play again soon!")
            real_guess += 1

i: int = 0
j: int = 0
yellow: int = 0
emoji_boxes: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while (i < len(secret_word)):
    j = 0
    yellow = 0
    if (user_guess[i] == secret_word[i]):
        emoji_boxes += GREEN_BOX
        i += 1
    else:
        while (j < len(secret_word)):
            if(user_guess[i] == secret_word[j]):
                emoji_boxes += YELLOW_BOX
                j += len(secret_word)
                i += 1
                yellow += 1
            else:
                j += 1
        if (yellow != 1):
            emoji_boxes += WHITE_BOX
            i += 1
print(emoji_boxes)