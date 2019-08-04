class Employee:

    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka

    def register_time(self, rej_czasu):
        self.rej_czasu = rej_czasu
        return self.stawka * self.rej_czasu


employee = Employee("Jan", "Nowak", 100)
wyplata = employee.register_time(5)


print(wyplata)


class TestEmployee:

    def test_wyplata(self):
        assert wyplata == 500
#dokończ