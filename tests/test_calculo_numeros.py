import unittest
from unittest.mock import patch
# Importamos de forma separada para poder manejar importaciones incremental
# según vayamos avanzando en las issues
from src.calculo_numeros import ingrese_numero
# Importar la excepción personalizada
from src.exceptions import NumeroDebeSerPositivo

class TestCalculoNumeros(unittest.TestCase):
    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, patch_input):
        """Prueba el caso de ingreso de un número válido positivo"""
        numero = ingrese_numero()
        self.assertEqual(numero, 100)
        
    @patch('builtins.input', return_value='-100')
    def test_ingreso_negativo(self, patch_input):
        """Prueba que se lance una excepción cuando el número es negativo"""
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()
            
    @patch('builtins.input', return_value='AAA')
    def test_ingreso_letras(self, patch_input):
        """Prueba que se lance ValueError cuando la entrada no es un número"""
        with self.assertRaises(ValueError):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main()