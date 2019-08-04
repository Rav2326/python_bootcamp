class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.length() > other.lenght()

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return Vector.__mul__(self, other)

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)


class TestVector:

    def test_vector_add(self):
        vector_1 = Vector(1, 2)
        vector_2 = Vector(2, 3)

        result = vector_1 + vector_2
        assert result.x == 3
        assert result.y == 5

    def test_vector_sub(self):
        vector_1 = Vector(1, 1)
        vector_2 = Vector(4, 5)

        result = vector_1 - vector_2
        assert result.x == -3
        assert result.y == -4

    def rest_vector_equal(self):
        vector_1 = Vector(1, 3)
        vector_2 = Vector(1, 3)

        assert vector_1 == vector_2

    def test_vector_lower_than(self):
        vector_1 = Vector(4, 4)
        vector_2 = Vector(1, 1)

        assert vector_2 < vector_1

    def test_vector_length(self):
        v = Vector(3, 4)
