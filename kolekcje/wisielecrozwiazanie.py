slowo = "python"
wynik = ["_" for x in slowo]
szanse = len(slowo) + 3  #czyli slowo + 3 szanse
print(slowo)
print(wynik)

while True:
    if szanse == 0:
        print("Przegrałeś")
        break

    znak = input("Wprowadź znak: ")

    if znak not in slowo:
        szanse -= 1
    i = 0
    for litera in slowo:
        if znak == litera:
            wynik[i] = znak
        i += 1
    if wynik == slowo:
           #print("Wygrałeś! ")  - wlacz to i zastanow co jest zle
           #break



     print(wynik)