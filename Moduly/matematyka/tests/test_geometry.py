from matematica.geometry.figures import square_area, trangle_area


def test_squre_area():
    assert square_area(2) == 4
    assert square_area(0) == 0
    assert square_area(3) == 9


def test_trangle_area():
    assert trangle_area(2, 2) == 2
