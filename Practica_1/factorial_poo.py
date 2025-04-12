from calculadora import calculadora

class calcFactorial(calculadora):
    def __init__(self):
        super().__init__()
        
    def calcular(self, num):
        self.operacion ="Factorial de"
        factorial = 1
        cont =1
        while cont <= int(num):
            factorial = self._multiplicacion(factorial, cont)
            cont += 1
        self.resultado = factorial
        return self.mostrar_operacion(num)
        
    def mostrar_operacion(self, num):
        return f"{self.operacion}: {num} = {self.resultado}"