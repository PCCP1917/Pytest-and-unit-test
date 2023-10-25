from Calculator import Calculator


def test_calculator_operations():
    my_calculator=Calculator()
    result=my_calculator.add(2,3)
    assert result == 5
    result=my_calculator.substract(9,3)
    assert result == 6
    result=my_calculator.multiplicate(2,3)
    assert result == 6
    result=my_calculator.divide(3,3)
    assert result == 1