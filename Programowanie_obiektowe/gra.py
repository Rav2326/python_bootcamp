import random


class Hero:

    def __init__(self, name, attack, defence, energy):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.energy = energy
        self.equipment = []

#     def __str__(self):
#         if self.energy <= 0:
#             return f"""{self.name} is dead!"""
#         return f"""{self.name} (A: {self.attack} | D: {self.defence} | E: {self.energy})
# Equipment:
# """
#         for item in self.equipment:
#             result += str(item)
#         return result

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


class Item:

    def __init__(self, name, attack_bonus, defence_bonus):
        self.name = name
        self.attack_bonus = attack_bonus
        self.defence_bonus = defence_bonus

    def __str__(self):
        return f"{self.name} A: {self.attack_bonus} | D: {self.defence_bonus}"


class Location:

    def __int__(self, x, y, max_x=10, max_y=10):
        self.x = x
        self.y = y
        self.max_x = x
        self.max_y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def up(self):
        self.y += 1
        if self.y > self.max_y:
            print()
            raise ValueError("Wyleciałeś poza planszę")

    def down(self):
        self.y -= 1
        if self.y < 1:
            raise ValueError("Wyleciałeś poza planszę")

    def right(self):
        self.x += 1
        if self.x > self.max_x:
            raise ValueError("Wyleciałeś poza planszę")

    def left(self):
        self.x -= 1
        if self.x < 1:
            raise ValueError("Wyleciałeś poza planszę")

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


class Board:
    def __init__(self, gracz, enemy, item):
        self.gracz = gracz
        self.enemy = enemy
        self.item = item
        self.gamer_location = Location(random.randint(1, 10), random.randint(1, 10))
        self.enemy_location = Location(random.randint(1, 10), random.randint(1, 10))
        self.item_location = Location(random.randint(1, 10), random.randint(1, 10))

    def move(self):
        print(f"Twoja pozycja to {self.gamer_location}")
        print(f'Pozycja rzeczy: {self.item_location}')
        print(f"Pozycja wroga: {self.item_location}")
        direction = str(input("Gdzie chcesz isc? "))
        if direction == "w":
            self.gamer_location.up()
        elif direction == "a":
            self.gamer_location.left()
        elif direction == "s":
            self.gamer_location.down()
        elif direction == "d":
            self.gamer_location.right()

        if self.gamer_location == self.item_location:
            print(f"Gracz znalazl przedmiopt: {self.item}")
            self.gamer.add_item(self.item)

        if self.gamer_location == self.enemy_location:
            print(self.gamer)
            print(self.enemy)
            Hero.fight(self.gamer, self.enemy)

        if self.gamer.energy < 0:
            raise Exception("End game")

    def run(self):
        while True:
            try:
                self.move()
            except:
                print("Gra zakonczona")
                break

class TestItem:
    def test_item_initialiozation(self):
        item = Item("Siekiera", attack_bonus=50, defence_bonus=10)
        assert item.name == "Siekiera"
        assert item.attack_bonus == 50
        assert item.defence_bonus == 10


class TestHero:

    def test_postac_initialization(self):
        postac = Hero("Albert", attack=10, defence=10, energy=100)
        assert postac.name == "Albert"
        assert postac.attack == 10
        assert postac.defence == 10
        assert postac.energy == 100
        assert len(postac.equipment) == 0

#     def test_postac_str(self):
#         postac = Hero("Albert", attack=10, defence=10, energy=100)
#         expected = """Albert (A: 10 | D: 10 | E: 100)
# Equipment:
# """
#         assert str(postac) == expected
#         postac = Hero("Albert", attack=10, defence=10, energy=100)
#         expected = """Albert is dead!"""
#         assert str(postac) == expected
#
#     def test_hero_with_item_str(self):
#         hero = Hero("Albert", attack=10, defence=10, energy=100)
#         item = Item("Siekiera", 50, 10)
#         hero.add_item(item)

        expected = """Albert (A: 60 | D: 20 | E: 100)
Equipment:
Siekiera A: 50 | D: 10
"""
       # assert str(hero) == expected

    def test_add_item(self):
        postac = Hero("Albert", attack=10, defence=10, energy=100)
        assert postac.name == "Albert"
        assert postac.attack == 10
        assert postac.defence == 10
        assert postac.energy == 100
        assert len(postac.equipment) == 0
        siekiera = Item("Siekiera", 50, 10)
        postac.add_item(siekiera)
        assert len(postac.equipment) == 1
        assert postac.attack == 10 + 50
        assert postac.defence == 10 + 10
        assert postac.energy == 100

    def test_hero_get_demage(self):
        postac = Hero("Albert", attack=10, defence=10, energy=100)
        postac.get_damage(10)
        assert postac.energy < 100


adam = Hero("Adam", 10, 10, 100)
anna = Hero("Anna", 10, 10, 100)
item = Item("Axe")

board = Board(adam, anna, item)
board.run()