
def factorial(numero):
    try:
        if numero<0:
            raise ValueError("Value Error: ")
        else:
            fact = 1 #var.local
            for i in range(1,numero+1):
                fact = fact * i
            return fact
    except ValueError as err:
        print(err, "No se admiten numeros negativos")
        return None

print(factorial(3))
print(factorial(0))
print(factorial(-4))

