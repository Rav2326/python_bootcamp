a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = str(input("Podaj rodzaj operacji: "))

if c == "+":
    print(f"Wynik: {a+b}")
elif c == "-":
    print(f"Wynik: {a-b}")
elif c == "*":
    print(f"Wynik: {a*b}")
elif c == "/":
    print(f"Wynik: {a/b}")