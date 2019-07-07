# litera= {" "}, {"a"}
# napis = "ala ma kota a kot ma ale"
# prog = 3

def czy_litera_wiecej_niz(litera, napis, prog):
    if napis.count(litera) > prog:
        return True
    return False


def wiecej_niz(napis, prog):
    wynik = set()
    for litera in napis:
        if czy_litera_wiecej_niz(litera, napis, prog):
            wynik.add(litera)
    return wynik


def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("", 0) == set()


def test_wiecej_niz_z_napisem_i_progiem():
    assert wiecej_niz("aaaa", 3) == {'a'}
