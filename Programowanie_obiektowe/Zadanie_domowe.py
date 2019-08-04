class Konwerter:

    def cel_to_farh(self, cel):
        farh = cel * 9/5 + 32
        return farh


assert Konwerter().cel_to_farh(0) == 32
