def pedir_entero(a_pedir: str, minimo: int, maximo: int) -> int:
    """
    Pide un entero al usuario y valida que sea un número y que se encuentre dentro del rango especificado.

    Pre: Recibe como parámetro un string correspondiente al nombre del entero a pedir, y dos enteros que indican el mínimo y máximo aceptados.
    Post: Retorna el entero validado previamente.
    """
    while True:
        entero = input(f"Ingrese {a_pedir.lower()}: ")
        try:
            entero = int(entero)
        except ValueError:
            print(f"ERROR - {a_pedir.capitalize()} debe ser un número entero.")
        else:
            if entero >= minimo and entero <= maximo:
                return entero
            else:
                print("ERROR - Rango inválido.")


def encajan_fichas(ficha1: tuple[int], ficha2: tuple[int]) -> bool:
    """
    Determina si las dos fichas de dominó ingresadas encajan o no.

    Pre: Recibe dos tuplas, correspondientes a dos fichas, con dos enteros cada una, representando los números de las mismas.
    Post: Retorna True si las fichas encajan, de lo contrario retorna False.
    """
    total_fichas = ficha1 + ficha2
    total_fichas = set(total_fichas)

    return len(total_fichas) < 4 # Si el conjunto mide menos, había números repetidos


def pedir_ficha() -> tuple[int]:
    """
    Pide al usuario los dos valores de una ficha de dominó.

    Pre: No recibe parámetros.
    Post: Retorna una tupla con dos enteros correspondientes a los dos números de la ficha de dominó.
    """
    num1 = pedir_entero("el primer número de la ficha", 0, 6)
    num2 = pedir_entero("el segundo número de la ficha", 0, 6)

    return (num1, num2)


def main():
    print("---Ingrese la primer ficha---")
    ficha1 = pedir_ficha()
    print("\n---Ingrese la segunda ficha---")
    ficha2 = pedir_ficha()

    print()
    if encajan_fichas(ficha1, ficha2):
        print(f"Las fichas {ficha1} y {ficha2} encajan.")
    else:
        print(f"Las fichas {ficha1} y {ficha2} no encajan.")

main()