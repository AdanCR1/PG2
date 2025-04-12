# PRÁCTICA 1

En esta práctica se implementa una calculadora estándar y una calculadora factorial utilizando programación orientada a objetos en Python.

## Estructura del Proyecto

```
PG2/
    README.md
    Practica_1/
        calculadora.py
        factorial_poo.py
        main.py
        __pycache__/
```

### Archivos principales:

- **`calculadora.py`**: Contiene la clase base `calculadora` con operaciones básicas como suma, resta, multiplicación y división.
- **`factorial_poo.py`**: Contiene la clase `calcFactorial`, que hereda de `calculadora` y añade la funcionalidad para calcular el factorial de un número.
- **`main.py`**: Archivo principal que ejecuta ejemplos de uso de las clases `calculadora` y `calcFactorial`.

---

## Cómo clonar el repositorio

Para obtener una copia local del proyecto, ejecuta el siguiente comando en tu terminal:

```bash
git clone <(https://github.com/AdanCR1/PG2.git)>
cd PG2/Practica_1
```

---

## Requisitos

- Python 3.10 o superior.
- Un entorno virtual (opcional, pero recomendado).

---

## Ejecución del proyecto

Para ejecutar el proyecto, navega a la carpeta `Practica_1` y ejecuta el archivo `main.py`:

```bash
cd PG2/Practica_1
python main.py
```

---

## Ejemplo de salida

Al ejecutar el archivo `main.py`, obtendrás una salida similar a la siguiente:

```
 ------CALCULADORA ESTÁNDAR------
Suma 4 y 7 = 11 
Resta 6 y 9 = -3 
Multiplicacion 4 y 8 = 32 
Dividion 12 y 4 = 3.0 

------CALCULADORA FACTORIAL------
Factorial de: 4 = 24
```

---

## Explicación del código

### `calculadora.py`

Este archivo define la clase base `calculadora`, que implementa operaciones matemáticas básicas. Es un ejemplo de encapsulación y reutilización de código en POO.

```python
class calculadora:
    def __init__(self):
        # Constructor que inicializa los atributos de la clase.
        self.resultado = 0  # Almacena el resultado de la operación.
        self.operacion = ""  # Almacena el nombre de la operación realizada.

    def suma(self, a, b):
        # Método público para realizar la suma de dos números.
        self.operacion = "Suma"
        self.resultado = a + b
        return self.mostrar_operacion(a, b)

    def resta(self, a, b):
        # Método público para realizar la resta de dos números.
        self.operacion = "Resta"
        self.resultado = a - b
        return self.mostrar_operacion(a, b)

    def _multiplicacion(self, a, b):
        # Método privado para realizar la multiplicación de dos números.
        # Este método no está destinado a ser llamado directamente desde fuera de la clase.
        return a * b

    def multiplicacion(self, a, b):
        # Método público para realizar la multiplicación, utilizando el método privado.
        self.operacion = "Multiplicacion"
        self.resultado = self._multiplicacion(a, b)
        return self.mostrar_operacion(a, b)

    def division(self, a, b):
        # Método público para realizar la división de dos números.
        self.operacion = "Dividion"
        self.resultado = a / b
        return self.mostrar_operacion(a, b)

    def mostrar_operacion(self, a, b):
        # Método público que devuelve una cadena con el resultado de la operación.
        return f"{self.operacion} {a} y {b} = {self.resultado}"
```

### `factorial_poo.py`

Este archivo define la clase `calcFactorial`, que hereda de la clase `calculadora` y añade funcionalidad para calcular el factorial de un número.

```python
from calculadora import calculadora

class calcFactorial(calculadora):
    def __init__(self):
        # Constructor que llama al constructor de la clase base.
        super().__init__()

    def calcular(self, num):
        # Método público para calcular el factorial de un número.
        self.operacion = "Factorial de"
        factorial = 1
        cont = 1
        while cont <= int(num):
            # Reutiliza el método privado _multiplicacion de la clase base.
            factorial = self._multiplicacion(factorial, cont)
            cont += 1
        self.resultado = factorial
        return self.mostrar_operacion(num)

    def mostrar_operacion(self, num):
        # Sobrescribe el método mostrar_operacion para adaptarlo al cálculo factorial.
        return f"{self.operacion}: {num} = {self.resultado}"
```

### `main.py`

Este archivo es el punto de entrada del programa. Muestra cómo usar las clases `calculadora` y `calcFactorial`.

```python
from calculadora import calculadora
from factorial_poo import calcFactorial

# Imprime un encabezado para la calculadora estándar.
print("\n", "------CALCULADORA ESTÁNDAR------")

# Crea una instancia de la clase calculadora.
c = calculadora()

# Realiza operaciones básicas y las imprime.
print(c.suma(4, 7), "\n", c.resta(6, 9), "\n", c.multiplicacion(4, 8), "\n", c.division(12, 4), "\n")

# Imprime un encabezado para la calculadora factorial.
print("------CALCULADORA FACTORIAL------")

# Crea una instancia de la clase calcFactorial.
calc = calcFactorial()

# Calcula el factorial de 4 y lo imprime.
print(calc.calcular(4))
```

---

## Nota adicional

- El método `_multiplicacion` en `calculadora.py` es privado y se utiliza internamente para calcular el factorial.

---

#### Explicación de POO:
- **Encapsulación**: Los atributos `resultado` y `operacion` están encapsulados dentro de la clase. El método `_multiplicacion` es privado, lo que significa que no debería ser accedido directamente desde fuera de la clase.
- **Reutilización**: Los métodos como `suma`, `resta`, etc., reutilizan el método `mostrar_operacion` para generar una salida uniforme.
- **Herencia**: La clase `calcFactorial` hereda de `calculadora`, lo que permite reutilizar métodos como `_multiplicacion` y `mostrar_operacion`.
- **Polimorfismo**: El método `mostrar_operacion` es sobrescrito para adaptarse al contexto del cálculo factorial.

---

### Resumen del uso de POO en el proyecto

1. **Clases y Objetos**: 
   - `calculadora` y `calcFactorial` son clases que encapsulan datos y comportamientos relacionados con cálculos matemáticos.
   - Los objetos (`c` y `calc`) son instancias de estas clases.

2. **Encapsulación**:
   - Los atributos (`resultado`, `operacion`) y métodos (`_multiplicacion`) están encapsulados dentro de las clases.

3. **Herencia**:
   - `calcFactorial` hereda de `calculadora`, reutilizando y extendiendo su funcionalidad.

4. **Polimorfismo**:
   - El método `mostrar_operacion` es sobrescrito en `calcFactorial` para adaptarse al cálculo factorial.

Este diseño modular y orientado a objetos facilita la reutilización del código y su mantenimiento.

AdanCR1: @workspace /explain 

Workspace: El código proporcionado implementa una calculadora básica y una calculadora factorial utilizando programación orientada a objetos en Python. Está compuesto por tres archivos principales: calculadora.py, factorial_poo.py y main.py.

### Archivo calculadora.py
Este archivo define la clase base `calculadora`, que incluye métodos para realizar operaciones matemáticas básicas como suma, resta, multiplicación y división. Cada operación actualiza los atributos `operacion` y `resultado` para reflejar el tipo de operación realizada y su resultado. Además, el método `mostrar_operacion` devuelve una cadena formateada que describe la operación realizada y su resultado. Cabe destacar que la multiplicación tiene un método privado `_multiplicacion`, que se utiliza internamente para encapsular la lógica de esta operación.

### Archivo factorial_poo.py
En este archivo se define la clase `calcFactorial`, que hereda de `calculadora`. Esta clase añade la funcionalidad para calcular el factorial de un número mediante el método `calcular`. Este método utiliza un bucle `while` para multiplicar los números desde 1 hasta el número dado, utilizando el método privado `_multiplicacion` de la clase base. Al final, el resultado se almacena en el atributo `resultado` y se utiliza el método `mostrar_operacion` para devolver una descripción del cálculo realizado.

### Archivo main.py
Este archivo actúa como punto de entrada para el programa. Primero, crea una instancia de la clase `calculadora` y muestra ejemplos de operaciones básicas como suma, resta, multiplicación y división. Luego, crea una instancia de la clase `calcFactorial` y calcula el factorial de un número (en este caso, 4). Los resultados de ambas calculadoras se imprimen en la consola.

### Resumen
El diseño del código sigue los principios de la programación orientada a objetos, como la herencia y la encapsulación. La clase `calculadora` sirve como base reutilizable para extender funcionalidades, como se demuestra con la clase `calcFactorial`. Además, el uso de métodos como `mostrar_operacion` mejora la legibilidad y la reutilización del código. Sin embargo, sería recomendable manejar posibles errores, como divisiones por cero o entradas no válidas, para hacer el programa más robusto.

AdanCR1: @workspace /explain 

En el archivo calculadora.py, se define la clase base `calculadora`, que incluye métodos para realizar operaciones matemáticas básicas como suma, resta, multiplicación y división. Cada operación actualiza los atributos `operacion` y `resultado` para reflejar el tipo de operación realizada y su resultado. Además, el método `mostrar_operacion` devuelve una cadena formateada que describe la operación realizada y su resultado. Un detalle interesante es que la multiplicación tiene un método privado `_multiplicacion`, que encapsula la lógica de esta operación y se utiliza tanto en la multiplicación estándar como en el cálculo del factorial.

El archivo factorial_poo.py define la clase `calcFactorial`, que hereda de `calculadora`. Esta clase amplía la funcionalidad de la calculadora básica al añadir un método llamado `calcular`, que permite calcular el factorial de un número. Este método utiliza un bucle `while` para multiplicar los números desde 1 hasta el número dado, aprovechando el método privado `_multiplicacion` de la clase base. Al final, el resultado se almacena en el atributo `resultado` y se utiliza el método `mostrar_operacion` para devolver una descripción del cálculo realizado.

Por último, el archivo main.py actúa como punto de entrada para el programa. Primero, crea una instancia de la clase `calculadora` y muestra ejemplos de operaciones básicas como suma, resta, multiplicación y división. Luego, crea una instancia de la clase `calcFactorial` y calcula el factorial de un número (en este caso, 4). Los resultados de ambas calculadoras se imprimen en la consola, mostrando cómo se pueden usar las clases para realizar cálculos matemáticos.

En general, el diseño del código sigue los principios de la programación orientada a objetos, como la herencia y la encapsulación. La clase `calculadora` sirve como base reutilizable para extender funcionalidades, como se demuestra con la clase `calcFactorial`. Además, el uso de métodos como `mostrar_operacion` mejora la legibilidad y la reutilización del código. Sin embargo, sería recomendable manejar posibles errores, como divisiones por cero o entradas no válidas, para hacer el programa más robusto.