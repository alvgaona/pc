from functions import reverse_list


def test_reverse_list():
    assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]

def test_empty_list():
    assert reverse_list([]) == []

def test_multiple_types_list():
    assert reverse_list([1, [1,2], "2", "Hello", (3,)]) == [(3,), "Hello", "2", [1, 2], 1]
