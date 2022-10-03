import sys
sys.path.insert(0,'/Users/Lorenzo/Documents/programacion/TDD_1/Ejercicio_2/calcu/src')
from calculadora import Calculator

#calculadora
c = Calculator()
#Suma
a = 1
b = 3
c.add(a, b)
print("Suma: {} + {} = {}".format(a, b, c.value))

# Resta
a = 3
b = 1
c = Calculator()
c.restar(a, b)
print("Resta: {} - {} = {}".format(a, b, c.value))

# Multiplicacion
a = 4
b = 2
c.multiplicar(a, b)
print("Multiplicación: {} * {} = {}".format(a, b, c.value))

#Division
a = 6
b = 2
c.dividir(a, b)
print("División: {} / {} = {}".format(a, b, c.value))

# Potencia
a = 6
b = 2
c.potencia(a, b)
print("Potencia: {} ^ {} = {}".format(a, b, c.value))

# Prueba de factorial
a = 5
c.factorial(a)
print("Factorial: {}! = {}".format(a, c.value))
