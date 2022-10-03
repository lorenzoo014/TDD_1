
# Cargamos el módulo unittest
import unittest
# Creamos una clase heredando de TestCase
import sys
sys.path.insert(0,'/Users/Lorenzo/Documents/programacion/TDD_1/Ejercicio_2/calcu/src')

from calculadora import Calculator

#clase heredad de Test Case
class TestMyCalculator(unittest.TestCase):
 # Creamos una prueba para probar un valor inicial

    def setUp(self):
        self.calc = Calculator()

    def test_initial_value(self):
        calc = Calculator()
        self.assertEqual(0, calc.value)

    # Creamos un nuevo test para comprobar una suma
    def test_add_method(self):
        # Ejecutamos el método
        self.calc.add(1, 3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(4, self.calc.value)

    def test_resta(self):
        self.calc.restar(4,2)
        self.assertEqual(2, self.calc.value)
    def test_multi(self):
        self.calc.multiplicar(4,2)
        self.assertEqual(8, self.calc.value)
    def test_divide(self):
        self.calc.dividir(6,2)
        self.assertEqual(3, self.calc.value)

    def test_potencia(self):
        self.calc.potencia(6,2)
        self.assertEqual(36, self.calc.value)
    def test_factorial(self):
        self.calc.factorial(5)
        self.assertEqual(120,self.calc.value)
    def test_logatirmo(self):
        self.calc.logaritmo(100)
        self.assertEqual(2,self.calc.value)

    def test_raiz(self):
        self.calc.raiz(100)
        self.assertEqual(10,self.calc.value)


     
    

