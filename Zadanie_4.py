imie = str(input("Jak masz na imie ?: "))
haslo = "python"
szanse = 0

DEBUG = True

while szanse < 10:
    litera = str(input("Podaj litere: "))
    szanse += 1
    if litera in haslo:
        print(f"Brawo zgadłeś literę {litera}")
    else:
        print("Próbuj dalej")
        continue
