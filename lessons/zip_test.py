from lessons.zip import zip

def test_empty_key() -> None:
    assert zip([], [1, 2, 3]) == {}

def test_empty_value() -> None:
    assert zip(["a", "b", "c"], []) == {}

def test_both_empty() -> None:
    assert zip([], []) == {}

def test_unequal() -> None:
    assert zip(["a", "b"], [1]) == {}

def test_normal() -> None:
    assert zip(["a", "b", "c"], [1, 2, 3]) == {"a":1, "b":2, "c": 3}
