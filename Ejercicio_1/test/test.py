import pytest
from Ejercicio_1.src.my_factorial import factorial

def test_myfactorial():
    assert factorial(3)==6

def test_cerofactorial():
    assert factorial(0)==1

def test_negfactorial():
    assert factorial(-3)==None
 