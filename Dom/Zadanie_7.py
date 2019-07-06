x = int(input("Wprowadź liczbę: "))

# print(x%2 == 1)


print(f"Czy podana liczba jest nieparzysta, podzielna przez 3, większa od 10: {x % 2 == 1 and bool(x // 3) and x > 10}")
