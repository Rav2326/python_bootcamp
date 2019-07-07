"""


Napisz funkcję, która sprawdzi, czy podany napis jest palindromem

"""


def is_palindrom(tekst: str) -> bool:
    tekst = tekst.lower()
    tekst = tekst.replace(" ", "")
    # return tekst == tekst[::-1] #1 rozwiazanie

    poczatek = 0
    koniec = len(tekst) - 1

    while poczatek <= koniec:
        if not tekst[poczatek] == tekst[koniec]:
            return False
        poczatek += 1
        koniec -= 1
    return True

def test_is_paindrom():
    # assert is_palindrom("ala") == True
    # assert is_palindrom("ala") == True
    # assert is_palindrom("może jeż łysy łże jeżom") == True
    # assert is_palindrom("ala ma kota") == False

    assert is_palindrom("ala")
    assert is_palindrom("Ala")
    assert is_palindrom("może jeż łysy łże jeżom")
    assert is_palindrom("ala ma kota")
