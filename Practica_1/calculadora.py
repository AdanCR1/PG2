class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.resultado = 0
        self.operacion = ""

    def suma(self):
        self.operacion = "Suma"
        self.resultado = self.a + self.b
        return self.mostrar_operacion()
    
    def resta(self):
        self.operacion = "Resta"
        self.resultado = self.a - self.b
        return self.mostrar_operacion()

    def multiplicacion(self):
        self.operacion = "Multiplicación"
        self.resultado = self.a * self.b
        return self.mostrar_operacion()

    def division(self):
        if self.b != 0:
            self.operacion = "División"
            self.resultado = self.a / self.b
        else:
            return "Error: División por cero"
        return self.mostrar_operacion()

    def mostrar_operacion(self):
        return f"{self.operacion}: {self.a} y {self.b} = {self.resultado}"

c = Calculadora(5, 15)

print(c.suma(), "|", c.resta(), "|", c.multiplicacion(), "|", c.division())