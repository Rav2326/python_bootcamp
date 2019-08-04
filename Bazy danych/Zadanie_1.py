import json

pracownicy = []

while True:
    des = input("Co chcesz zrobic ? [d- dodaj(wcisnij 'k' by przerwac), w - wypisz]")
    if des == "d":
        dict = {"Imię": str(input("Imię: ")),
                "Nazwisko": str(input("Nazwisko: ")),
                "Rok urodzenia": int(input("Rok urodzenia: ")),
                "Pensja": float(input("Pensja: ")), }
    elif des == "k":
        break
    print()
    pracownicy.append(dict)

des = input("Co chcesz zrobic ? [d- dodaj, w - wypisz]")

if des == "w":
    print(pracownicy)

with open("json-zad_1.txt", "wt") as f:
    s = json.dumps(pracownicy)
    print(s)
    json.dump(pracownicy, f)

with open("json-zad_1.txt", "rt") as f:
    s = f.read()
    dict1 = json.loads(s)
    print(dict1)
