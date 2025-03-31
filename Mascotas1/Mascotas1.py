from datetime import datetime


"""
Práctica de clase: Tienda1

Este programa maneja el inventario de una tienda.

Heyder Ivan Ramos Rodriguez
<hiramosr@academia.usbbog.edu.co
 heydercolegious@gmail.com>
2025-03-30
"""


class Mascota:
    """Clase que da estructura"""
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().isoformat()  # Fecha y Hora actual

class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza)
        self.especie = "Perro"


class Gato(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza)
        self.especie = "Gato"

mascotas = []  # Lista que almacena las mascotas ingresadas

numero_mascotas = int(input("¿Cuantas mascotas va a ingresar? \n"))

for i in range(1, numero_mascotas + 1):
    print(f"> Mascota {i}, ¿qué clase es? (P)erro o (G)ato?")
    tipo = input("< ").strip().lower()  # Tomara de igual manera minusculas y mayusculas

    while tipo not in ("p" , "g"):
        print("> Opcion invalida. Escriba (P) para perro y (g) para gato")
        tipo = input("< ").strip().lower()

    clase = "Perro" if tipo == "p" else "Gato"
    print(f"> ¿Cuál es el nombre del {clase}?")
    nombre = input("< ").strip()

    print(f"Que edad tiene {nombre}")
    print(f"> ¿Qué edad tiene '{nombre}'?")
    edad = int(input("< ").strip())

    print(f"> ¿De qué raza es '{nombre}'?")
    raza = input("< ").strip()
    if clase == "Perro":
        mascota = Perro(nombre, edad, raza)
    else:
        mascota = Gato(nombre, edad, raza)

    mascotas.append(mascota)

# Imprimimos resumen
print("\n> Resumen:")
print(f"{'Clase':<6} | {'Nombre':<10} | {'Edad':<5} | {'Raza':<15} | {'Fecha de ingreso'}")
print("-" * 75)

for mascota in mascotas:
    print(f"{mascota.especie:<6} | {mascota.nombre:<10} | {mascota.edad:<5} años | {mascota.raza:<15} | {mascota.fecha_ingreso}")
