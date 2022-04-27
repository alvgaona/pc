from functions import find_max


def test_find_max():
    assert find_max([1, 2, 3, 4]) == 4


def test_negative_values():
    assert find_max([-1, -2, -3, -4]) == -1