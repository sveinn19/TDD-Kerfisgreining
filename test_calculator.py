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
    assert Calculator.add("10,2,5,22,1,1") == 41

def test_add_with_newline_delimater():
    assert Calculator.add("1\n2,3") == 6

