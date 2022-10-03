
# Cargamos el módulo unittest
import unittest
# Creamos una clase heredando de TestCase
import sys
sys.path.insert(0,'/Users/Lorenzo/Documents/programacion/TDD_1/Ejercicio_2/calcu/src')

from calculadora import Calculator

#clase heredad de Test Case
class TestMyCalculator(unittest.TestCase):
 # Creamos una prueba para probar un valor inicial
    def test_initial_value(self):
        calc = Calculator()
        self.assertEqual(0, calc.value)

