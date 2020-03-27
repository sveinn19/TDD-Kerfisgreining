from calculator import Calculator


def test_add_zero():
    assert Calculator.add("") == 0

def test_add_single_number():
    assert Calculator.add("1") == 1

def test_add_two_numbers():
    assert Calculator.add("1,2") == 3
    assert Calculator.add("5,6") == 11  

def test_add_multiple_numbers():
    assert Calculator.add("1,2,3,4,5") == 15

