import unittest
from tienda3 import Producto, solicitar_precio, solicitar_cantidad
from tienda3 import solicitar_descripcion, solicitar_categoria
from unittest.mock import patch


class TestProducto(unittest.TestCase):
    """Pruebas unitarias para la clase Producto"""

    def test_creacion_producto(self):
        """Prueba que el producto se crea correctamente"""
        producto = Producto(
            "Leche", 5000, 2, "Leche descremada", "Alimentación"
            )
        self.assertEqual(producto.nombre, "Leche")
        self.assertEqual(producto.precio_unitario, 5000)
        self.assertEqual(producto.cantidad, 2)
        self.assertEqual(producto.descripcion, "Leche descremada")
        self.assertEqual(producto.categoria, "Alimentación")

    def test_precio_inventario(self):
        """Prueba que el cálculo del inventario es correcto"""
        producto = Producto("Pan", 2000, 10, "Pan tajado", "Alimentación")
        self.assertEqual(producto.precio_inventario(), 20000)

    def test_calcula_precio(self):
        """Prueba el cálculo de precio por cantidad"""
        producto = Producto("Huevo", 500, 200,
                            "Cartón de huevos", "Alimentación")
        self.assertEqual(producto.calcula_precio(5), 2500)


class TestFunciones(unittest.TestCase):
    """Pruebas unitarias para las funciones de entrada"""

    @patch('builtins.input', return_value="1500")
    def test_solicitar_precio(self, mock_input):
        """Verifica que solicitar_precio retorne un número válido"""
        self.assertEqual(solicitar_precio("Ingrese el precio: "), 1500.0)

    @patch('builtins.input', return_value="10")
    def test_solicitar_cantidad(self, mock_input):
        """Verifica que solicitar_cantidad retorne un número entero válido"""
        self.assertEqual(solicitar_cantidad("Ingrese la cantidad: "), 10)

    @patch('builtins.input', return_value="Descripción de prueba")
    def test_solicitar_descripcion(self, mock_input):
        """Verifica que solicitar_descripcion retorne la cadena esperada"""
        self.assertEqual(solicitar_descripcion("Ingrese una descripción: "),
                         "Descripción de prueba")

    @patch('builtins.input', return_value="Categoría de prueba")
    def test_solicitar_categoria(self, mock_input):
        """Verifica que solicitar_categoria retorne la cadena esperada"""
        self.assertEqual(solicitar_categoria("Ingrese una categoría: "),
                         "Categoría de prueba")


if __name__ == "__main__":
    unittest.main()
