import sys
sys.path.insert(0,'/Users/Lorenzo/Documents/programacion/TDD_1/Ejercicio_2/calcu/src')
from calculadora import Calculator

#calculadora
c = Calculator()
while True:
    print("========================")
    print(" BIENVENIDO AL Manager ")
    print("========================")
    print("[1] Operar con la calculadora ")
    print("[2] Cerrar el Manager ")
    print("========================")
    opcion = input("> ")
    if opcion=='1':
        a = input("Introduce un numero entero ")
        b= input("Introduce un segundo numero entero ")
        a=int(a)
        b=int(b)
        #Suma
        c.add(a, b)
        print("Suma: {} + {} = {}".format(a, b, c.value))

        # Resta
        c.restar(a, b)
        print("Resta: {} - {} = {}".format(a, b, c.value))

        # Multiplicacion
        c.multiplicar(a, b)
        print("Multiplicación: {} * {} = {}".format(a, b, c.value))

        #Division
        c.dividir(a, b)
        print("División: {} / {} = {}".format(a, b, c.value))

        # Potencia
        c.potencia(a, b)
        print("Potencia: {} ^ {} = {}".format(a, b, c.value))

        # factorial
        c.factorial(a)
        print("Factorial: {}! = {}".format(a, c.value))
        #logaritmo
        c.logaritmo(a)
        print("Logartimo: log{} = {}".format(a, c.value))
        #raiz
        c.raiz(a)
        print("Raiz_cuadrada: {} = {}".format(a, c.value))
        
    if opcion == '2':
        print("Saliendo...\n")
        break