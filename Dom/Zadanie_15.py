skarb_x = 8
skarb_y = 7

gracz_x = 3
gracz_y = 4
print(f"Znajdujesz się: ({gracz_x} , {gracz_y})")

polozenie_gracza = 0
i = 0

while i < 15:
    polozenie_gracza = str(input("Gdzie chcesz isć [w - góra, s - dół, d - prawo, a- lewo: "))
    i += 1
    if polozenie_gracza == "w":
        gracz_y += 1
        print(f"Ciepło! Jesteś w ({gracz_x}, {gracz_y}) ")
    elif polozenie_gracza == "s":
        gracz_y -= 1
        print(f"Zimno! Jesteś w ({gracz_x}, {gracz_y})")
    elif polozenie_gracza == "d":
        gracz_x += 1
        print(f"Ciepło! Jesteś w ({gracz_x}, {gracz_y})")
    elif polozenie_gracza == "a":
        gracz_x -= 1
        print(f"Zimno! Jesteś w ({gracz_x}, {gracz_y}) ")
    else:
        print("Zły kierunek")
    if gracz_x == 8 and gracz_y == 7:
        break
if gracz_x == 8 and gracz_y == 7:
    print("Udało Ci się znaleźć skarb !")
if gracz_x > 10 or gracz_x < 0 or gracz_y > 10 or gracz_y < 0:
    print("Nie udało się, spróbuj jeszcze raz!")

liczba_ruchów = 0

print(liczba_ruchów)
