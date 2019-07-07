"""

Napisz funkcję, która wypisze n pierwszych wierszy trójkąta pascala

[1]
[1, 1]
[1, 2 , 1]


"""
liczby = [1]


def trojkat_pascala(n):
    wiersz = [1]
    wiersze = [wiersz]
    for i in range(n - 1):
        nowywiersz = [1]
        for j in range(len(wiersz) - 1):
            nowywiersz.append(wiersz[j] + wiersz[j + 1])
        nowywiersz.append(1)
        wiersz = nowywiersz
        wiersze.append(wiersz)

    out = ""
    for line in wiersze:
        out += str(line) + "\n"
    return out


print(trojkat_pascala(1))
print("-" * 40)
print(trojkat_pascala(2))
print("-" * 40)
print(trojkat_pascala(3))


def test_trojkat_pascala():
    expected = """[1]
[1, 1]
[1, 2, 1]"""
    assert trojkat_pascala(3) == expected
