# test_math.py

import pytest
from pytest import mark
def suma(a, b):
    return a + b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

@mark.unit_test
def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0

@mark.unit_test
def test_division_valida():
    assert division(10, 2) == 5

@mark.unit_test
def test_division_cero():
    # Aquí indica el tipo de error que estamos esperando
    with pytest.raises(ValueError):
        division(5, 0)
