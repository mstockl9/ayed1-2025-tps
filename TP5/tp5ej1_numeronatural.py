class MenorIgualCero(Exception):
    """
    Número menor o igual a 0
    """
    pass

def pedir_natural() -> int:
    """
    Pide un número natural y valida que el mismo sea un entero y mayor que 0.

    Pre: No recibe parámetros.
    Post: Retorna el número natural validado previamente.
    """
    while True:
        nro = input("Ingrese un número natural: ")
        
        try:
            nro = int(nro)
            if nro <= 0:
                raise MenorIgualCero
        except ValueError:
            print("ERROR - Debe ingresar un número entero.\n")
        except MenorIgualCero:
            print("ERROR - El número debe ser mayor a 0\n")
        else:
            return nro

def main():
    n = pedir_natural()
    print(f"Número validado: {n}")

main()