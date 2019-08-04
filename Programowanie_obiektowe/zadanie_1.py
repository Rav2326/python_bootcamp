class Product:

    def __init__(self, id, rzecz, cena):
        self.id = id
        self.rzecz = rzecz
        self.cena = cena

    def print_info(self):
        print(f"Produkt {self.rzecz}, id: {self.id}, cena: {self.cena} PLN")


woda = Product(1, "Woda", 2.99)
piwo = Product(2, "Piwo", 3.00)

woda.print_info()
piwo.print_info()



