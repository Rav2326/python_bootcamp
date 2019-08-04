import random

random.randint

DEBUG = True

gracz_x = random.randint(0, 10)
gracz_y = random.randint(0, 10)

enemy_x = random.randint(0, 10) != gracz_x
enemy_y = random.randint(0, 10) != gracz_y



skarb_x, skarb_y = random.randint(0, 10), random.randint(0, 10)
odleglosc_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

liczba_ruchow = 0

if DEBUG:
    print(f"Położenie skarbu to: ({skarb_x}, {skarb_y}) ")
    print(f"Położenie gracza to: ({gracz_x}, {gracz_y})")
    print(f"Odległość po wylosowaniu to: {odleglosc_po_wylosowaniu}")

while True:

    kierunek = input ("Podaj kierunek [w-góra, a-lewo, d-prawo, s-dół]:")
    przed_ruchem = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    if kierunek == "w":
        gracz_y =+ 1
    elif kierunek == "a":
        gracz_x -= 1
    elif kierunek == "s":
        gracz_y -= 1
    elif kierunek == "d":
        gracz_x += 1

    if gracz_x < 0 or gracz_x > 10 or gracz_y < 0 or gracz_y > 10:
        print("Wypadłeś poza świat")
        break

    po_ruchu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    liczba_ruchow += 1

    if po_ruchu == 0:
        print("Znalazłeś skarb !")
        print(f"Wykonałeś {liczba_ruchow} ruchów")
        break

    if DEBUG:
        print(f"Położenie skarbu to: ({skarb_x}, {skarb_y}) ")
        print(f"Położenie gracza to: ({gracz_x}, {gracz_y})")
    los = random.randint(1,5)
    if DEBUG:
        print("Los: ", los)
    if los != 3:
        if po_ruchu > przed_ruchem:
            print("Zimno")
        else:
            print("Jestem złośliwy nie podpowiem Ci!")

    if po_ruchu > przed_ruchem:
        print("Zimno")

    else:
        print("cieplo")

    if odleglosc_po_wylosowaniu > odleglosc_po_wylosowaniu* 2:
        skarb_x, skarb_y = random.randint(0, 10), random.randint(0, 10)
        odleglosc_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

        liczba_ruchow = 0
        print("Jesteś gapa. Skarb zmienił położenie.")

class Hero:

    def __init__(self, name, attack, defence, energy):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.energy = energy
        self.equipment = []

    def __str__(self):
        if self.energy <= 0:
            return f"""{self.name} is dead!"""
        return f"""{self.name} (A: {self.attack} | D: {self.defence} | E: {self.energy})
    Equipment:
    """
        for item in self.equipment:
            result += str(item)
        return result


    def add_item(self, item):
        self.equipment.append(item)


    @property
    def attack(self):
        result = self.attack
        for item in self.equipment:
            result += item.attack_bonus
        return result


    @property
    def defence(self):
        result = self.defence
        for item in self.equipment:
            result += item.defence_bonus
        return result


    def get_damage(self, value):
        damage = value - random.randint(1, self.defense // 2)
        if damage > 0:
            self.energy -= damage
            print(f"{self.name} oberwał za {damage}")


    @staticmethod
    def fight(hero_a, hero_d):

        while hero_a.energy > 0 and hero_d.energy > 0:
            hero_d.get_damage(hero_a.attack)
            if hero_d.energy > 0:
                hero_a.get_damage(hero_d.attack)

        print(hero_a)
        print(hero_d)