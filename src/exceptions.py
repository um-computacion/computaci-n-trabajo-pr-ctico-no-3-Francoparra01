# src/exceptions.py
class NumeroDebeSerPositivo(Exception):
    """Excepción lanzada cuando se ingresa un número negativo."""
    
    def __init__(self, mensaje="El número debe ser positivo"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def ingrese_numero():
    """
    Solicita al usuario ingresar un número y valida que sea positivo.
    
    Returns:
        int: El número ingresado si es válido.
        
    Raises:
        ValueError: Si la entrada no es un número válido.
        NumeroDebeSerPositivo: Si el número ingresado es negativo.
    """
    entrada = input("Ingrese un número: ")
    numero = int(entrada)  # Puede lanzar ValueError si no es un número
    
    if numero < 0:
        raise NumeroDebeSerPositivo("El número debe ser positivo")
        
    return numero