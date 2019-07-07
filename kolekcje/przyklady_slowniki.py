osoba={

    "imie": "Rafał",
    "nazwisko": "Handzlik",
    "hobby": ["muzyka", "historia", "..."],
    "dzieci": {"Corka1", "Garbyiela" },
    1: "jeden"
}

print(osoba["imie"])
print(osoba["nazwisko"])
print(osoba[1])

# dzieci = osoba["dzieci"]
# # dzieci["Corka1"] = "Gabi"
# # print(osoba)

osoba["sport"] = ["armwrestling"]
print(osoba.get("zona", "brak")) #w przytpadku gdy nie ma "zona" daje sie komende .get
print(osoba.keys())
#print(osoba.pop)
print(osoba.values())


