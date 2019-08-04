# a = int(input("Podaj wartość podstawy: "))
# h = int(input("Podaj wartość wysokości "))
#
# pole_trojkata = a/2 * h
#
# print(f"Pole wynosi : {pole_trojkata}")
# print()
# promien = int(input("Podaj promień koła: "))
#
# pole_kola = 3.14 * promien**2
#
# print(f"Pole koła wynosi: {pole_kola}")
# print()
#
# a1= int(input("Podaj długość pierszej podstawy "))
# a2 = int(input("Podaj długość drugiej podstawy "))
# h1 = int(input("Podaj długość wysokości: "))
# pole_trapezu = (a1+a2)*h / 2
#
#
# print(f"Pole trapezu wynosi: {pole_trapezu}")
# print()
#
# promien_kuli = int(input("Podaj promień kuli: "))
#
# objetosc = 4/3*3.14*promien_kuli**3
# print(f"Objętość kuli wynosi: {objetosc}")

class Pole:

    def __init__(self, a, h):
        self.a = a
        self.h = h

    def pole_trojkata(self):
        return 1 / 2 * (self.a * self.h)



pole = Pole()

pole.pole_trojkata(10, 5)

class TestPole:

    def test_pole_trojkata(self):
        pole_trojkata = Pole()
        assert pole_trojkata(10, 5) == 25

    # def test_pole_koła(self):
    #     assert pole_kola() = 153.86
