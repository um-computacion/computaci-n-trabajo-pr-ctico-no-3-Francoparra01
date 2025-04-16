# src/calculo_numeros.py
from exceptions import ingrese_numero, NumeroDebeSerPositivo

def main():
    """
    Programa principal que solicita números al usuario y muestra los resultados.
    """
    while True:
        try:
            numero = ingrese_numero()
            print(f"Número válido: {numero}")
        except ValueError:
            print(f"Error: La entrada debe ser un número válido")
        except NumeroDebeSerPositivo as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nPrograma finalizado.")
            break

if __name__ == "__main__":
    main()