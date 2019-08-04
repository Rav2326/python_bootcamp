class Employee:

    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka

    def register_time(self, rej_czasu):
        self.rej_czasu = rej_czasu
        return self.stawka * self.rej_czasu


employee = Employee("Jan", "Nowak", 100)
salary = employee.register_time(5)


class PremiumEmployee(Employee):

    def give_bonus(self, bonus):
        self.bonus = bonus
        return salary + self.bonus

pay_salary = employee.give_bonus(1000.0)

