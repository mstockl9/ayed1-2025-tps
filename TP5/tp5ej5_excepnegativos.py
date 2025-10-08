import math

class NumeroNegativo(Exception):
    """
    Número menor a cero
    """
    pass

def pedir_n() -> int:
    """
    Pide un número al usuario y valida que no sea negativo.

    Pre: No recibe parámetros.
    Post: Retorna el número que ingresó el usuario validado previamente.
    """
    while True:
        n = input("Ingrese un número entero positivo: ")
        
        try:
            n = int(n)
            if n < 0:
                raise NumeroNegativo
        except ValueError:
            print("ERROR - Debe ingresar un número entero")
        except NumeroNegativo:
            print("ERROR - El número no puede ser negativo")
        else:
            return n

def main():
    n = pedir_n()
    raiz_cuadrada = math.sqrt(n)
    print(f"La raíz cuadrada de {n} es de: {raiz_cuadrada}")

main()