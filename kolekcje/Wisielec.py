<<<<<<< HEAD
imie = str(input("Jak masz na imie ?: "))
haslo = "python"
szanse = 0
wynik = ["_" for x in haslo]
DEBUG = True

while True:
    litera = input("Podaj litere: ")


    if litera in haslo:
        for litera2 in haslo:
            if litera == litera2:
                wynik.append("_")
    else:
        wynik.append("_")



# wynik = ["_" for x in slowo]
#jest to samo co:
# wynik = [}
# for x i9n slowo:
=======
imie = str(input("Jak masz na imie ?: "))
haslo = "python"
szanse = 0
wynik = ["_" for x in haslo]
DEBUG = True

while True:
    litera = input("Podaj litere: ")


    if litera in haslo:
        for litera2 in haslo:
            if litera == litera2:
                wynik.append("_")
    else:
        wynik.append("_")



# wynik = ["_" for x in slowo]
#jest to samo co:
# wynik = [}
# for x i9n slowo:
>>>>>>> origin/master
    #wynik.append("_")