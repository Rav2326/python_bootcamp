x = int(input("Wprowadź rok urodzenia: "))

if x >= 2002 and x < 2020:
    print("Nie jesteś pełnoletni !")
elif x < 2002:
    print("Jesteś pełnoletni !")
else:
    print("Jeszcze się nie narodziłeś !")

