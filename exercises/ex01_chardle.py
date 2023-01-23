"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730398384"

word_input: str = input("Enter a 5-character word: ")  # Getting word input
if (len(word_input) != 5):   # Checking for word input length
    print("Error: Word must contain 5 characters")
    exit()
character_input: str = input("Enter a single character: ")  # Getting character input
if (len(character_input) != 1):  # Checking for character input length
    print("Error: Character must be a single character.")
    exit()
index_zero: str = word_input[0]  # indexing the word
index_one: str = word_input[1]
index_two: str = word_input[2]
index_three: str = word_input[3]
index_four: str = word_input[4]
matching_character_count: int = 0
word_input_length: int = len(word_input)

print("Searching for", character_input, "in", word_input)

if (index_zero == character_input):  # trying to match character input to indexes
    print(character_input, "found at index 0")
if (index_one == character_input):
    print(character_input, "found at index 1")
if (index_two == character_input):
    print(character_input, "found at index 2")
if (index_three == character_input):
    print(character_input, "found at index 3")
if (index_four == character_input):
    print(character_input, "found at index 4")

if (index_zero == character_input):
    matching_character_count += 1
if (index_one == character_input):
    matching_character_count += 1
if (index_two == character_input):
    matching_character_count += 1
if (index_three == character_input):
    matching_character_count += 1
if (index_four == character_input):
    matching_character_count += 1
                        
if (matching_character_count > 1):
    print(matching_character_count, "instances of", character_input, "found in", word_input)
elif (matching_character_count == 1):
    print(matching_character_count, "instance of", character_input, "found in", word_input)
else:
    print("No instances of", character_input, "found in", word_input)