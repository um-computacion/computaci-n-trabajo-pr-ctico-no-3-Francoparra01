# src/exceptions.py
class NumeroDebeSerPositivo(Exception):
    """Excepción lanzada cuando se ingresa un número negativo."""
    
    def __init__(self, mensaje="El número debe ser positivo"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)