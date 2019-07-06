pierwsza_liczba = int(input("Podaj pierwszą liczbę: "))
druga_liczba = int(input("Podaj drugą liczbę "))
operacja = str(input("Podaj rodzaj operacji: "))

if operacja == "+":
    wynik = pierwsza_liczba + druga_liczba
    print(wynik)
elif operacja == "-":
    wynik = pierwsza_liczba - druga_liczba
    print(wynik)
elif operacja == "*":
    wynik = pierwsza_liczba * druga_liczba
    print(wynik)
elif operacja == "/":
    wynik = pierwsza_liczba / druga_liczba
    if druga_liczba == 0:
        print("Nie dziel przez zero")
    else:
        print(wynik)
