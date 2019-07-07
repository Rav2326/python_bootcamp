# def sumator(a, *b, c=10, d=11, **kwargs):
#     print(a, type(a))
#     print(b, type(b))
#     return a + sum(b) + c + d
#
#
# def test_sumator():
#     assert sumator(1) == 1
#     assert sumator(1, 1) == 2
#     assert sumator(1, 1, 5, 6, 7) == 20
#     assert sumator(1, 1, 5, 6, 7, 8) == 28
#     assert sumator(1, 1, 5, 6, 7, 8, 10) == 38

slownik = {'a': 1, 'b': 2}
mapowanie = {'a': 'c', 'b': 'd'}
tekst1 = "aa bb ab"
tekst2 = "cc dd ac"
output = "cc dd cd cc dd cc"


def mapownik(*teksty, **kwargs):
    tekst = " ".join(teksty)

    for znak in kwargs:
        print(f"zamieniam {znak} na {kwargs[znak]}")
        tekst = tekst.replace(znak, kwargs[znak])
    return tekst


assert mapownik(tekst1, tekst2, a='c', b='d') == output
