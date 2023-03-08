"""EX04 - List Utility Functions: Implementing Algorithms to Practice Computational Thinking!"""

__author__ = "730398384"


def all(int_list: list[int], compared_int: int) -> bool:
    """A function that compares a list and a single int to see if all ints in the list are the same as the given single int."""
    i = 0
    if len(int_list) == 0:  # ensuring list isn't empty
        return False
    while i < len(int_list):
        if compared_int == int_list[i]:
            i += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """A function that when given a list of ints, returns the largest in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i = 1
    highest_number = input[0]
    while i < len(input):
        if highest_number < input[i]:
            highest_number = input[i]
            i += 1
        else:
            i += 1
    return highest_number


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """A function that when given two lists of int values, returns True if every element at every index is equal in both lists."""
    if len(list_one) != len(list_two):  # ensures lists are equal length 
        return False
    i = 0
    while i < len(list_one):
        if list_one[i] == list_two[i]:
            i += 1
        else:
            return False
    return True