x = int(input("Podaj pozycję gracza X: "))
y = int(input("Podaj pozycję gracza Y: "))
print()

if x > 100 or x < 0:
    print("Gracz jest poza planszą!")

if y > 100 or y < 0:
    print("Gracz jest poza planszą! ")

if x > 10 and x < 90 and y >= 90:
    print("Gracz jest w GÓRNEJ KRAWĘDZI")
elif x >= 90 and y > 10 and y < 90:
    print("Gracz jest w PRAWEJ KRAWĘDZI")
elif x > 10 and x < 90 and y <= 10:
    print("Gracz jest w DOLNEJ KRAWĘDZI")
elif x <= 10 and y >10 and y < 90:
    print("Gracz jest w LEWEJ KRAWEDZI")
elif x <= 10 and y >= 90:
    print("Gracz jest w LEWYM GÓRNYM ROGU")
elif x >= 90 and y >= 90:
    print("Gracz jest w PRAWYM GÓRNYM ROGU")
elif x>= 90 and y <=10:
    print("Gracz jest w PRAWYM DOLNYM ROGU")
elif x <= 10 and y <= 10:
    print("Gracz jest w LEWYM DOLNYM ROGU")
else:
    print("Gracz jest w CENTRUM")

