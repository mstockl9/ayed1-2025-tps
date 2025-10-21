def pedir_entero(a_pedir: str) -> int:
    """
    Pide un entero al usuario y valida que sea un número.

    Pre: Recibe como parámetro un string correspondiente al nombre del entero a pedir.
    Post: Retorna el entero validado previamente.
    """
    while True:
        entero = input(f"Ingrese {a_pedir.lower()}: ")
        try:
            entero = int(entero)
        except ValueError:
            print(f"ERROR - {a_pedir.capitalize()} debe ser un número entero.")
        else:
            return entero


def generar_diccionario_tablas(n: int) -> dict:
    """
    Genera un diccionario con la tabla de multiplicar de N del 1 al 12.

    Pre: Recibe como parámetro el valor de N, que debe ser un entero.
    Post: Retorna un diccionario con la tabla de multiplicar de N del 1 al 12.
    """
    return {multiplicar: n * multiplicar for multiplicar in range(1, 12+1)}


def imprimir_tabla_mult(tablas: dict) -> None:
    """
    Imprime las tablas de múltiplicar en formato apropiado.

    Pre: Recibe como parámetro el diccionario con las tablas a multiplicar.
    Post: No retorna nada, imprime las tablas de multiplicar del número.
    """
    print("Multiplicación    Resultado")
    for mult, resultado in tablas.items():
        print("-"*30)
        print(mult, " "*(16-len(str(mult))), resultado)


def main():
    n = pedir_entero("el valor de N")
    diccionario_tablas = generar_diccionario_tablas(n)
    print()
    imprimir_tabla_mult(diccionario_tablas)

main()