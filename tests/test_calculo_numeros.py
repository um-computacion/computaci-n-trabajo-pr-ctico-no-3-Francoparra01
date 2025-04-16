import unittest
from unittest.mock import patch
# Importamos de forma separada para poder manejar importaciones incremental
# según vayamos avanzando en las issues
from src.calculo_numeros import ingrese_numero

class TestCalculoNumeros(unittest.TestCase):
    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, patch_input):
        """Prueba el caso de ingreso de un número válido positivo"""
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

if __name__ == '__main__':
    unittest.main()