"""
Práctica de clase: Tienda1

Este programa maneja el inventario de una tienda.

Heyder Ivan Ramos Rodriguez
<hiramosr@academia.usbbog.edu.co
 heydercolegious@gmail.com>
2025-02-28
"""


class Producto:
    """Clase para manejar productos"""

    def __init__(self, nombre, precio_unitario, cantidad):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad


def solicitar_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor ingrese un numero valido")


def solicitar_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Porfavor ingrese un numero valido")


def mostrar_resumen(productos):
    print(">\n Resumen:")
    print("-" * 40)
    print("| Producto  | Cantidad     | Precio    |")
    print("-" * 40)
    for p_lista in productos:
        print(f"> |{p_lista.nombre:<9}|{p_lista.cantidad:>4} unidades |"
              f"{p_lista.precio_unitario:>5,.0f} pesos |")
        # `:<9` alinea el texto a la izquierda con un ancho de 9 caracteres
    print("-" * 40)


def run():
    productos = []  # Lista para almacenar los productos

    for numero_producto in range(1, 4):  # Escoger 3 productos
        nombre = input(f"Producto {numero_producto}, ¿cual es el nombre?\n")
        precio_unitario = solicitar_float(f"¿Qué precio tiene {nombre}?\n")
        cantidad = solicitar_int(f"¿Que cantidad hay de {nombre}?\n")

        producto = Producto(nombre, precio_unitario, cantidad)
        productos.append(producto)  # Almacenar en la lista


if __name__ == "__main__":
    run()
