sklep = {
    "ogórki": 3.00,
    "pomidory": 4.00,
    "fasola": 6.50,
    "marchew": 3.75
}
magazyn = {
    "ogórki": 40,
    "pomidory": 40,
    "fasola": 40,
    "marchew": 40
}
print("W naszym sklepie kupisz: ogórki, pomidory, fasola, marchew") #wypisz produkty za pomnocaą petli i fstringa
co_chce = input("Co chcesz kupic?: ")
ilosc = float(input(f"Ile chcesz kupić? [{co_chce}]: "))
cena = sklep[co_chce] * ilosc
print(f"Za [{co_chce}] zapłacisz {cena}")

magazyn[co_chce] -= ilosc

print(f"Magazyn: {magazyn}")

if ilosc > magazyn[co_chce]:
    print("Nie ma tyle produktu")
