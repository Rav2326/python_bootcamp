"""

Napisz funkcje, która:

1. dla listy, tupli, zbioru zwróci sumę elementów
2. jesli argument bedzie słownikiem, to zwróci sumę wartosci

"""
def to_numeric(value):
    if isinstance(value, str) and value.isnumeric():
        return int(value)
    elif isinstance(value, bool):
        return None
    elif isinstance(value, int):
        return value


def my_sum(numbers):
    if isinstance(numbers, dict):
        numbers = numbers.values()
    data = []
    for n in numbers:
        if isinstance(n, str) and n.isnumeric():
            data.append(int(n))
        elif isinstance(n, int):
            data.append(n)
    return sum(data)

def test_sum_for_list():
    assert my_sum([1, 2, 3]) == 6
    assert my_sum([1, 2, 3, 'a']) == 6
    assert my_sum(['1', 2, '3', 'a']) == 6


def test_sum_for_set():
    assert my_sum({1, 2, 3}) == 10
    assert my_sum({1, 2, 3, 'a'}) == 6



def test_sum_for_tuple():
    assert my_sum({1, 2, 3, 4, 5}) == 15


def test_sum_for_dict():
    assert my_sum({'a': 1, "b": 11}) == 12

