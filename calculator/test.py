import pytest
from calc import Calculator  # Assuming the class is in a file named 'calculator.py'

@pytest.fixture
def calc():
    return Calculator()

def test_initial_value(calc):
    assert calc.get_current_value() == 0

def test_addition(calc):
    calc.add(5)
    assert calc.get_current_value() == 5

def test_subtraction(calc):
    calc.add(10)
    calc.subtract(4)
    assert calc.get_current_value() == 6

def test_multiplication(calc):
    calc.add(3)
    calc.multiply(5)
    assert calc.get_current_value() == 15

def test_division(calc):
    calc.add(20)
    calc.divide(4)
    assert calc.get_current_value() == 5

# test ZeroDivision Exeption
def test_divide_by_zero(calc):
    result = calc.divide(0)
    assert result == "Error: Division by zero is not allowed."
    assert calc.get_current_value() == 0
 
 
# parametrized tests    
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 3, 3),
    (-1, 1, 0),
    (4.4, -4, 0.4),
    (10.5, 0, 10.5)
])    
def test_add_param(calc, a, b, expected):
    calc.add(a)
    calc.add(b)
    assert calc.get_current_value() == pytest.approx(expected)

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),
    (0, 3, 0),
    (-1, 1, -1),
    (0, -4, 0),
    (10.5, 5.4, 56.7),
    (-5, 4.6, -23)
])    
def test_multiplication_param(calc, a, b, expected):
    calc.add(a)
    calc.multiply(b)
    assert calc.get_current_value() == expected
    
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 2),
    (1, 2, 0.5),
    (-1, 1, -1),
    (0, -4, 0)
])    
def test_division_param(calc, a, b, expected):
    calc.add(a)
    calc.divide(b)
    assert calc.get_current_value() == expected


def test_reset(calc):
    calc.add(100)
    calc.reset()
    assert calc.get_current_value() == 0

def test_multiple_operations(calc):
    calc.add(10)
    calc.subtract(2)
    calc.multiply(5)
    calc.divide(4)
    assert calc.get_current_value() == 10

