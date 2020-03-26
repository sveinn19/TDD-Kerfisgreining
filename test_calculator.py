from calculator import Calculator


def test_add_zero():
    assert Calculator.add("") == 0

def test_add_single_number():
    assert Calculator.add("1") == 1
