"""EX03 - Structured Wordle: Wordle That Allows Multiple Tries"""

__author__ = "730398384"

def contains_char(input_string: str, char_string: str) -> bool:
    """A loop that tests each letter of the input_string to a single character."""
    assert len(char_string) == 1
    i = 0
    while i < len(input_string):
        if(input_string[i] == char_string[0]):
            return True
        i = i + 1
    return False

def emojified(guess: str, secret: str) -> str:
    """A function that tests if the letters match up in equivalence and position, and assigns respective emojis for each result."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"  
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    letter_box = ""
    i = 0
    while i < len(guess):
        if(guess[i] == secret[i]):
            letter_box = letter_box + GREEN_BOX
        elif contains_char(secret, guess[i]):
            letter_box = letter_box + YELLOW_BOX
        else:
            letter_box = letter_box + WHITE_BOX
        i = i + 1
    return letter_box

def input_guess(input_length: int) -> str:
    """A function that prompts for a guess, and ensures that the length of the secret word be equivalent to that guess."""
    i: int = 0
    query: str = input(f"Enter a {input_length} character word: ")
    while i < input_length: 
        if len(query) != input_length:
            query = input(f"That wasn't {input_length} chars! Try again: ")
        elif (len(query) == input_length):
            return query
        i = i + 1
    return query

def main() -> None:
    """The entrypoint of the program and main game loop."""
    answer: str = "codes"
    i = 1
    while i <= 6:
        print(f"=== Turn {i}/6 ===")
        user_input: str = input_guess(len(answer))
        print(emojified(user_input, answer))
        if answer == user_input:
            print(f"You won in {i}/6 turns!")
            return
        else:    
            i = i+1
    print("X/6 - Sorry, try again tomorrow!")
    return

if __name__ == "__main__":
    main()