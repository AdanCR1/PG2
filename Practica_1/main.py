from calculadora import calculadora
from factorial_poo import calcFactorial

print("\n", "------CALCULADORA ESTÁNDAR------")
c = calculadora()
print(c.suma(4,7), "\n", c.resta(6,9), "\n", c.multiplicacion(4,8), "\n", c.division(12,4), "\n")

print("------CALCULADORA FACTORIAL------")

calc = calcFactorial()
print(calc.calcular(4))