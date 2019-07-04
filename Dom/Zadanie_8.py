a = int(input("Wprowadź szerokość pudełka: "))
b = int(input("Wprowadź wysokość pudełka: "))
c =  int(input("Wprowadź długość pudełka: "))

objetosc = a*b*c
print()

print(f"Objętość zawartosci pudełka wynosi: {objetosc} ")
print()
print(f"Objętość pudełka jest większa od 1 litra: {objetosc > 1000}")
