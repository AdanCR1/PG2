class calculadora:
    def __init__(self):
        self.resultado = 0
        self.operacion = ""

    def suma(self,a,b):
        self.operacion ="Suma"
        self.resultado= a+ b
        return self.mostrar_operacion(a, b)

    def resta(self ,a,b):
        self.operacion ="Resta"
        self.resultado = a - b
        return self.mostrar_operacion(a, b)

    def _multiplicacion(self,a ,b):
        return a * b

    def multiplicacion(self ,a ,b):
        self.operacion ="Multiplicacion"
        self.resultado = self._multiplicacion(a, b)
        return self.mostrar_operacion(a, b)

    def division(self ,a ,b):
        self.operacion ="Dividion"
        self.resultado = a / b
        return self.mostrar_operacion(a,b)

    def mostrar_operacion(self ,a ,b):
        return f"{self.operacion} {a} y {b} = {self.resultado}"