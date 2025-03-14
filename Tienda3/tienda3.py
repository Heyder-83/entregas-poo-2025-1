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

    def __init__(self, nombre, precio_unitario, cantidad, descripcion,
                 categoria):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.categoria = categoria

    def precio_inventario(self):
        return self.cantidad * self.precio_unitario

    def calcula_precio(self, cantidad):
        return self.precio_unitario * cantidad


def solicitar_precio(precio_unitario):
    while True:
        try:
            precio_producto = float(input(precio_unitario))
            if precio_producto < 0:
                print("Por favor ingrese un precio valido")
            else:
                return precio_producto
        except ValueError:
            print("Por favor ingrese un precio valido")


def solicitar_cantidad(cantidad_producto):
    while True:
        try:
            cantidad = int(input(cantidad_producto))
            if cantidad < 0:
                print("Por favor ingrese una cantidad valida")
            else:
                return cantidad
        except ValueError:
            print("Por favor ingrese una cantidad valida")


def solicitar_descripcion(descripcion_producto):
    return input(descripcion_producto)


def solicitar_categoria(categoria_producto):
    return input(categoria_producto)


def resumen(productos):
    print("\n> Resumen:")
    print("-" * 160)
    print(
        "| Producto  |  Cantidad    |   Precio     "
        "|   Descripción     | Clasificación  |Total en inventario "
        "|Precio x5 unidades |"
    )
    print("-" * 160)
    for p_lista in productos:
        total_inventario = p_lista.precio_inventario()
        precio_5_u = p_lista.calcula_precio(5)
        print(f"> |{p_lista.nombre:<9}|{p_lista.cantidad:>4} unidades |"
              f"{p_lista.precio_unitario:>7,.0f} pesos |"
              f"{p_lista.descripcion:<20}|{p_lista.categoria:<12}|"
              f"{total_inventario:>14,.0f} pesos |"
              f"{precio_5_u:>14,.0f} pesos |")
    print("-" * 160)


def precio_categoria(productos):
    if not productos:
        print("\nNo hay productos en la lista")
        return

    precios_categoria = {}

    for p in productos:
        precio_total = p.precio_unitario
        if p.categoria in precios_categoria:
            precios_categoria[p.categoria] += precio_total
        else:
            precios_categoria[p.categoria] = precio_total

    print("\n> Precio por clasificación")
    print("-" * 40)
    print(f"| {'Clasificación':<15} | {'Precio':<10} |")
    print("-" * 40)
    for categoria, precio in precios_categoria.items():
        print(f"| {categoria:<15} | {precio:>7,.0f} pesos |")
    print("-" * 40)


def run():
    productos = []
    numero_producto = 1

    while True:
        nombre = input(
            f"Producto {numero_producto}, ¿cual es el nombre? "
            f"(Dejar en blanco para terminar)\n"
        )
        if nombre == "":
            break

        precio_unitario = solicitar_precio(f"¿Que precio tiene {nombre}?\n")
        cantidad = solicitar_cantidad(f"¿Que cantidad hay de {nombre}?\n")
        descripcion = solicitar_descripcion(f"Descripción breve de {nombre}\n")
        categoria = solicitar_categoria(
            f"¿A que categoria pertence {nombre}?\n"
            )
        producto = Producto(
            nombre, precio_unitario, cantidad, descripcion, categoria
        )
        productos.append(producto)

        numero_producto += 1

    resumen(productos)
    precio_categoria(productos)


if __name__ == "__main__":
    run()
