liczby = []
i = 0
podana_liczba = 0
while i < 10:
    podana_liczba = int(input("Wprowadź liczbę: "))
    liczby.append(podana_liczba)
    i += 1
print(liczby)


print()
print(f"Średnia podanych liczb to: {sum(liczby)}")
