# przytnij(
# data= [1, 2, 3, 4, 5, 6, 7],
# start = lambda x: x >3,
# stop = lambda x: x> 3,
# )
#
# ["a", "b", "c", 2, 4, "dy", "x",  5, 6, "a", "b", "c", "dy", "x"]
#
# przytnij(
# data= ["a", "b", "c", "dy", "x"],
# start = lambda x: x == "b",
# stop = lambda x: ,
# )

def przytnij(data, start, stop):
    rezultat = []
    czy_dodawac = False

    for element in data:
        if start(element):
            czy_dodawac = True

        if czy_dodawac:
            rezultat.append(element)
            if stop(element):
                break
                # czy_dodawac = False
    return rezultat


def test_przytnij():
    actual = przytnij(
        data=[1, 2, 3, 4, 1, 6, 7],
        start=lambda x: x > 3,
        stop=lambda x: x == 6
    )

    assert actual == [4, 1, 6]
