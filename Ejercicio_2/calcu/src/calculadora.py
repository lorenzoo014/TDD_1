import math
class Calculator():
    def __init__(self):
        self.value = 0
    def add(self, a, b):
        self.value = a + b

    def restar(self,a,b):
        self.value=a-b
    def multiplicar(self, a, b):
        self.value = a * b
    def dividir(self, a, b):
        self.value = a / b
        
    def potencia(self,a,b=2):
        self.value = a**b
    
    def factorial(self,a):
        self.value=math.factorial(a)
        
    def logaritmo(self,a,b=10):
        self.value=math.log(a,b)

    def raiz(self,a):
        self.value=math.sqrt(a)


    

