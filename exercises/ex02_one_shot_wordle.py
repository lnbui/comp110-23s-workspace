"""EX02 - One Shot Wordle - A Wordle that allows only one try."""

__author__ = "730398384"

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")  # getting the word input and ensuring the length of the word is correct
normalized_guess: str = guess.lower()  # ensuring that capitalization doesn't matter

WHITE_BOX: str = "\U00002B1C"  # declaring box colors for correct or incorrect boxes
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
letter_box = ""

i: int = 0

while i < len(secret):
    if len(secret) != len(normalized_guess):
        guess = input(f"That was not {len(secret)} letters! Try again! ") # ensuring guess is as long as secret
        normalized_guess = guess.lower()
    elif secret[i] == normalized_guess[i]:
        letter_box = letter_box + GREEN_BOX
    elif secret[i] != normalized_guess[i]:
        j = 0
        letter_match = "False" # if index of guess doesn't match up to secret then it goes into the loop
        while j < len(secret):
            if secret[j] == normalized_guess[i]:
                letter_match = "True"
            j += 1
        if letter_match == "True":
            letter_box = letter_box + YELLOW_BOX
        else:
            letter_box = letter_box + WHITE_BOX
    i += 1

if len(secret) == len(normalized_guess):  # if guess is the secret than "Woo! you got it! appears, and if not, then "Not quite. Play again soon!" does
    if secret == normalized_guess:
        print(letter_box)
        print("Woo! You got it!")
    elif secret != normalized_guess:
        print(letter_box)
        print("Not quite. Play again soon!")
