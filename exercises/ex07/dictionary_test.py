"""Tests for EX07: Dictionary Functions."""

__author__ = "730398384"

from exercises.ex07.dictionary import invert, favorite_color, count 


def test_one_pair() -> None:
    """Use case: Testing for when there is only one key-value pair in the dictionary."""
    test_dict: dict[str, str] = {"Joe": "Bob"}
    assert invert(test_dict) == {"Bob": "Joe"}


def test_many_pairs() -> None:
    """Use case: Testing for when there are multiple key-value pairs in the dictionary."""
    test_dict: dict[str, str] = {"Joe": "Bob", "Blue": "Red", "Sky": "Earth"}
    assert invert(test_dict) == {"Bob": "Joe", "Red": "Blue", "Earth": "Sky"}


def test_empty_dict() -> None:
    """Edge case: Testing for when there is no key-value pair in the dictionary."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_single_pair() -> None:
    """Use case: Testing for when there is only one key-value pair in the dictionary."""
    test_dict: dict[str, str] = {"Joe": "Blue"}
    assert favorite_color(test_dict) == {"Blue"}


def test_equal() -> None:
    """Edge case: Testing for when there is an equal number of favorite colors, so that the first one input comes out first."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Joe": "yellow"}
    assert favorite_color(test_dict) == {"yellow"}


def test_empty_input() -> None:
    """Edge case: Testing for when there is no key-value pair in the dictionary."""
    test_dict: dict[str, int] = {}
    assert favorite_color(test_dict) == {}


def test_one_element() -> None:
    """Use case: Testing for when there is only one item in the list."""
    test_list: list[str] = ["Joe"]
    assert count(test_list) == {"Joe": 1}


def test_many_items() -> None:
    """Use case: Testing for when there are multiple int in the list."""
    test_list: list[str] = ["Joe", "Joe", "Bob", "Linda", "Linda", "Linda"]
    assert count(test_list) == {"Joe": 2, "Bob": 1, "Linda": 3}


def test_empty_list() -> None:
    """Edge case: Testing for when there is an empty list."""
    test_list: list[str] = []
    assert count(test_list) == {}