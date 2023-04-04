"""EX07: Dictionary Functions."""

__author__ = "730398384"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """This function switches the key and value of an input dictionary."""
    invert_dict: dict[str, str] = {}
    for key in input_dict:
        if input_dict[key] in invert_dict:
            raise KeyError("KeyError")
        invert_dict[input_dict[key]] = key
    return invert_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """This function calculates which color is the most favorite of an input dictionary."""
    rank_dict: dict[str, int] = {}
    color_list: list(str) = []
    rank: list(int) = []
    highest_number: int = 0
    i: int = 0
    j: int = 1
    # Sets up relevant dicts, lists, and other variables
    if len(input_dict) == 0:
        return ""
        # If the input is empty, returns an empty string
    for key in input_dict:
        rank_dict[input_dict[key]] = 0
    for key in input_dict:
        rank_dict[input_dict[key]] += 1
    for key in rank_dict:
        color_list.append(key)
        rank.append(rank_dict[key])
        # Sets up the dicts and lists to calculate values from
    while i < len(rank) and j < len(rank):
        if rank[i] >= rank[j]:
            highest_number = i
            j += 1
        else:
            highest_number = j
            i += 1 
        # Comparing between values to find the most favorite color
    return color_list[highest_number]
    

def count(input_list: list[str]) -> dict[str, int]:
    """This function adds up the number of times a word is within a list."""
    count_dict: dict[str, int] = {}
    # Sets up an empty dict to fill in
    for item in input_list:
        if item in count_dict:
            # If an item is in the dictionary, it adds 1 to the count
            count_dict[item] += 1
        else: 
            count_dict[item] = 1
        # Otherwise, it adds the term and sets its value to 1
    return count_dict