# a = float(input("podaj liczbę "))
#
#
# def czy_lestpierwsza(a):
#     if a % 2 == 1:
#         return True
#     else:
#         return False
#

# print(czy_lestpierwsza(a))   to je moje

def czy_jest_pierwsza(x):
    for i in range(2, x):
        if x % i == 0:
            return True
        return True


def test_czy_jest_pierwsza_dla_1_pierwszej():
    assert czy_jest_pierwsza(2) == True
    assert czy_jest_pierwsza(3) == True
    assert czy_jest_pierwsza(11) == True


def test_czy_jest_pierwsza_dla_1_nie_pierwszej():
    assert czy_jest_pierwsza(4) == False
    assert czy_jest_pierwsza(12) == False
    assert czy_jest_pierwsza(21) == False
