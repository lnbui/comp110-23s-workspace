"""EX05 - 'list' Utility Functions: Testing the Functions."""

__author__ = "730398384"

from exercises.ex05.utils import only_evens, sub, concat


def test_odd_list() -> None:
    """Edge case: Testing for when all ints in the list are odd ints."""
    test_list: list[int] = [1, 3, 5]
    assert only_evens(test_list) == []


def test_one_element() -> None:
    """Use case: Testing for when there is only one int in the list."""
    test_list: list[int] = [2]
    assert only_evens(test_list) == [2]


def test_many() -> None:
    """Use case: Testing for when there are multiple int in the list."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(test_list) == [2, 4, 6]


def test_empty_lists() -> None:
    """Edge case: Testing for when there is an empty list for both lists."""
    test_list_one: list[int] = []
    test_list_two: list[int] = []
    assert concat(test_list_one, test_list_two) == []


def test_one_element_in_lists() -> None:
    """Use case: Testing for when there is one element in both lists."""
    test_list_one: list[int] = [1]
    test_list_two: list[int] = [3]
    assert concat(test_list_one, test_list_two) == [1, 3]


def test_multiple() -> None:
    """Use case: testing for when there are multiple elements in both lists."""
    test_list_one: list[int] = [1, 3, 8]
    test_list_two: list[int] = [2, 5, 15]
    assert concat(test_list_one, test_list_two) == [1, 3, 8, 2, 5, 15]


def test_empty_list() -> None:
    """Edge case: testing for when the list is empty."""
    test_list: list[int] = []
    test_start: int = 0
    test_end: int = 15
    assert sub(test_list, test_start, test_end) == []


def test_negative_start() -> None:
    """Edge case: testing for when the start index is negative."""
    test_list: list[int] = [1, 2, 3]
    test_start: int = -1
    test_end: int = 3
    assert sub(test_list, test_start, test_end) == [1, 2, 3]


def test_end_too_large() -> None:
    """Edge case: testing for when the end index is greater than the length of the index."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    test_start: int = 1
    test_end: int = 15
    assert sub(test_list, test_start, test_end) == [2, 3, 4, 5, 6, 7, 8]


def test_entire_list() -> None:
    """Use case: testing for when it is appending the entire original list into the subset list."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    test_start: int = 0
    test_end: int = 8
    assert sub(test_list, test_start, test_end) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_one_int_list() -> None:
    """Use case: testing for when there is only one element in the list."""
    test_list: list[int] = [1]
    test_start: int = 0
    test_end: int = 1
    assert sub(test_list, test_start, test_end) == [1]