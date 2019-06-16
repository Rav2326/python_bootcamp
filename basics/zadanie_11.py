x = int(input("Podaj pozycję gracza X: "))
y = int(input("Podaj pozycję gracza Y: "))

if x >= 90:
    print("Górna")
if x < 90 or x > 10:
    print("Środkowa")
if x <= 10:
    print("Dolna")
if y <= 10:
    print(f"Lewa {x >= 90} , {x < 90 or x > 10} , {x <= 10}")
if y > 10 or y < 90:
    print("")
if y >= 90:
    print(f"Prawa {x >= 90} , {x < 90 or x > 10} , {x <= 10}")

