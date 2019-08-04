class ElectricCar:
    def __init__(self, max_range):
        self.max_range = max_range
        self._traceled_distance = 0

    def drive(self, distance):
        if distance + self._traceled_distance < self.max_range:
            self._traceled_distance += distance
            return distance
        else:
            to_travel = self.max_range - self._traceled_distance
            self._traceled_distance = self.max_range
            return to_travel

    def charge(self):
        self._traceled_distance = 0


class TestElectricCar:

    def test_initialization(self):
        car = ElectricCar(100)
        assert car.max_range == 100

    def test_drive_below_range(self):
        car = ElectricCar(100)
        assert car.drive(70) == 70

    def test_drive_above_max_range(self):
        car = ElectricCar(100)
        assert car.drive(120) == 100

    def test_many_drives(self):
        car = ElectricCar(100)
        assert car.drive(50) == 50
        assert car.drive(70) == 50
        assert car.drive(10) == 0

    def test_charge(self):
        car = ElectricCar(100)
        assert car.drive(50) == 50
        assert car.drive(70) == 50
        assert car.drive(10) == 0
        car.charge()
        assert car.drive(50) == 90
        assert car.drive(70) == 10
        assert car.drive(10) == 0
