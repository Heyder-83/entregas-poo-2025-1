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

    def __init__(self, nombre, precio_unitario, cantidad,
                 descripcion, categoria):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.categoria = categoria


def solicitar_float(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            if numero < 0:
                print("Por favor ingrese un precio valido (Mayor o igual a 0)")
            else:
                return numero
        except ValueError:
            print("Por favor ingrese un precio valido")


def solicitar_int(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                print(
                    "Por favor ingrese una cantidad valida (Mayor o igual a 0)"
                )
            else:
                return numero
        except ValueError:
            print("Por favor ingrese una cantidad valida")


def solicitar_descripcion(mensaje):
    return input(mensaje)


def solicitar_categoria(mensaje):
    return input(mensaje)


def mostrar_resumen(productos):
    print("\n> Resumen:")
    print("-" * 80)
    print(
        "| Producto  |  Cantidad     |   Precio     "
        "|   Descripción     | Clasificación  |"
    )
    print("-" * 80)
    for p_lista in productos:
        print(f"> |{p_lista.nombre:<9}|{p_lista.cantidad:>4} unidades |"
              f"{p_lista.precio_unitario:>7,.0f} pesos |"
              f"{p_lista.descripcion:<20}|{p_lista.categoria:<12}")
        # `:<9` alinea el texto a la izquierda con un ancho de 9 caracteres
    print("-" * 80)


def precio_categoria(productos):
    if not productos:
        print("\n No hay productos en la lista")
        return
    
    clasificacion_precios = {}


def run():
    productos = []  # Lista para almacenar los productos
    numero_producto = 1

    while True:
        nombre = input(
            f"Producto {numero_producto}, ¿cual es el nombre? "
            f"(Dejar en blanco para terminar)\n"
        )
        if nombre == "":
            break

        precio_unitario = solicitar_float(f"¿Qué precio tiene {nombre}?\n")
        cantidad = solicitar_int(f"¿Que cantidad hay de {nombre}?\n")
        descripcion = solicitar_descripcion(f"Descripción breve de {nombre}\n")
        categoria = solicitar_categoria(
            f"¿En que clasificación se encuentra {nombre}?\n"
        )
        producto = Producto(
            nombre, precio_unitario, cantidad, descripcion, categoria
        )
        productos.append(producto)  # Almacenar en la lista

        numero_producto += 1

    mostrar_resumen(productos)
    precio_categoria(productos)


if __name__ == "__main__":
    run()
