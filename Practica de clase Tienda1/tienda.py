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


def run():
    productos = []  # Lista para almacenar los productos

    for numero_producto in range(1, 4):  # Escoger 3 productos
        nombre = input(f"Producto {numero_producto}, ¿cual es el nombre?\n")
        precio_unitario = float(input(f"¿Qué precio tiene {nombre}?\n"))
        cantidad = int(input(f"¿Que cantidad hay de {nombre}?\n"))

        producto = Producto(nombre, precio_unitario, cantidad)
        productos.append(producto)  # Almacenar en la lista

    # Información en formato de tabla
    print("\n> Resumen:")
    print("| Producto  | Cantidad     | Precio    |")

    for p_lista in productos:
        print(f"> |{p_lista.nombre:<9}|{p_lista.cantidad:>4} unidades |"
              f"{p_lista.precio_unitario:>5} pesos |")
        # `:<9` alinea el texto a la izquierda con un ancho de 9 caracteres


if __name__ == "__main__":
    run()
