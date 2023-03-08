"""EX05 - 'list' Utility Functions: The Functions."""

__author__ = "730398384"


def only_evens(input_list: list[int]) -> list[int]:
    """A function that when given a list of ints, returns a list of even ints from within that list."""
    even_list: list = []
    i = 0
    if input_list == []:
        return even_list
    while i < len(input_list):
        if input_list[i] % 2 == 0:  # Checks for evenness here
            even_list.append(input_list[i])
        i += 1
    return even_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """A function that wehn given two lists of ints, returns a combined list of the elements of first list and the second list in that order."""
    concat_list: list = []
    i = 0
    j = 0
    if list_one != []:  # Checking for empty lists
        while i < len(list_one):
            concat_list.append(list_one[i])
            i += 1
    if list_two != []:
        while j < len(list_two):
            concat_list.append(list_two[j])
            j += 1
    return concat_list


def sub(orig_list: list[int], start_index: int, end_index: int) -> list[int]:
    """A function that when given a list of ints, an int to serve as the start of an index, and an int to serve as the end of the index, returns a list that begins at the start and ends at the element before the end index."""
    sub_list: list = []
    if start_index < 0:  # Checking for negative start indexes
        start_index = 0
    if end_index > len(orig_list):  # Checking for too-large end indexes
        end_index = len(orig_list)
    i = start_index
    while i < end_index:
        sub_list.append(orig_list[i])
        i += 1
    return sub_list
