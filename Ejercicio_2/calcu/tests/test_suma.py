from Ejercicio_2.calcu.src.calculadora import Calculator

# Cargamos el módulo unittest
import unittest
# Creamos una clase heredando de TestCase

class TestMyCalculator(unittest.TestCase):
 # Creamos una prueba para probar un valor inicial
    def test_initial_value(self):
        calc = Calculator()
        self.assertEqual(0, calc.value)