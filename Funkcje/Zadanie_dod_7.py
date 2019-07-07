# splaszcz liste tak zeby byla bez zagniezdzenia
# lista = [1, 2, 3, [4, 5, [6]], 7]

def splaszcz(lista):
    rezultat = []
    for el in lista:
        if isinstance(el, list):
            rezultat.extend(splaszcz(el))
        else:
            rezultat.append(el)
    return rezultat

def test_splascz():
    assert splaszcz([]) == []
    assert splaszcz([1, 2, 3]) == [1, 2, 3]
    assert splaszcz([1, 2, [3, [4]]]) == [1, 2, 3, 4]





