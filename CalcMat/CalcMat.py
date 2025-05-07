"""
Práctica de clase: CalcMat

Este programa permite sumar, restar y multiplicar matrices 2x2.

Heyder Ivan Ramos Rodriguez
<hiramosr@academia.usbbog.edu.co
 heydercolegious@gmail.com>
2025-04-26
"""


class Matriz:
    def __init__(self, valores):
        self.valores = valores

    def __add__(self, matrix):
        nueva = []
        for i in range(2):
            fila = []
            for j in range(2):
                suma = self.valores[i][j] + matrix.valores[i][j]
                fila.append(suma)
            nueva.append(fila)
        return Matriz(nueva)

    def __sub__(self, matrix):
        nueva = []
        for i in range(2):
            fila = []
            for j in range(2):
                resta = self.valores[i][j] - matrix.valores[i][j]
                fila.append(resta)
            nueva.append(fila)
        return Matriz(nueva)

    def __mul__(self, matrix):
        nueva = []
        for i in range(2):
            fila = []
            for j in range(2):
                producto = (
                    self.valores[i][0] * matrix.valores[0][j] +
                    self.valores[i][1] * matrix.valores[1][j]
                )
                fila.append(producto)
            nueva.append(fila)
        return Matriz(nueva)

    def mostrar(self):
        for fila in self.valores:
            print(fila)


def pedir_matriz(nombre):
    print(f"\nIntroduce los valores para la matriz {nombre}:")
    valores = []
    for i in range(2):
        fila = []
        for j in range(2):
            valor = int(input(f"Elemento [{i+1}][{j+1}]: "))
            fila.append(valor)
        valores.append(fila)
    return Matriz(valores)


print("> Ingrese los valores de las matrices a calcular")

matriz1 = pedir_matriz(1)
matriz2 = pedir_matriz(2)

print("\n> ¿Qué operación desea realizar?")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")

operacion = input("< Escriba el número de la operación: ")

if operacion == "1":
    resultado = matriz1 + matriz2
    print("\n> Resultado de la suma:")
elif operacion == "2":
    resultado = matriz1 - matriz2
    print("\n> Resultado de la resta:")
elif operacion == "3":
    resultado = matriz1 * matriz2
    print("\n> Resultado de la multiplicación:")
else:
    print("Opción no válida.")
    resultado = None

if resultado:
    resultado.mostrar()
