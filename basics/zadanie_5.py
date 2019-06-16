a = input("Podaj miasto A : ")
b = input("Podaj miasto B : ")
dystans = float(input(f"Dystans {a}-{b}:"))
cena = float(input("Cena paliwa: "))
spalanie = float(input("Spalanie na 100 km: "))
print()

koszt = (dystans / 100) * spalanie * cena

print(f"Koszt przejazdu {a}-{b} {koszt} PLN")
