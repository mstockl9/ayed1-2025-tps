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


def main():
    conjunto = {num for num in range(9+1)}
    while True:
        print(conjunto)
        num = pedir_entero("un valor")
        if num == -1:
            print("\nEl programa ha finalizado.")
            break

        try:
            conjunto.remove(num)
        except KeyError:
            print(f"\nERROR - El elemento de valor {num} no existe en el conjunto.")
        print()

main()