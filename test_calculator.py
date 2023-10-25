from Calculator import Calculator
import pytest

my_calculator=Calculator()
def test_add():
    result=my_calculator.add(2,3)
    assert result == 5

def test_Substract():
    result=my_calculator.substract(5,3)
    assert result == 2

def test_Multiplicate():
    result=my_calculator.multiplicate(5,5)
    assert result == 25
    
def test_divide():
    result=my_calculator.divide(12,3)
    assert result == 4