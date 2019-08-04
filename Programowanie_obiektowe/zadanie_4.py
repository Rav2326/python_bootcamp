class Product:
    id_ = 0

    def __init__(self, nazwa, cena, id=None):

        if id is not None:
            self.id = id
        else:
            Product.id += 1
            self.nazwa = nazwa
            self.cena = cena

    def print_info(self):
        print(f"Produkt {self.nazwa}, id: {self.id}, cena: {self.cena} PLN")



class Basket:
    def __init__(self):
        self.entries = []

    def add_product(self, product, quantity: int):
        self.entries.append([product, quantity])

    def count_total_proce(self):
        total_price = 0
        for entry in self.entries:
            total_price += entry.count_price()
        return


    def generate_report(self):
        report = "Produkty w koszyku: \n"
        for entry in self.entries:
            report += f" - {entry.product.nazwa} ({entry.product.id}), cena: {entry.product.cena:.2f} x {entry.quantity}\n"
        report += f"W sumie: {self.count_total_proce():.2f}\n"

        return report

class TestBasket:

    def test_generate_report(self):
        basket = Basket()


