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

def calcular_digitos(num: int) -> int:
    """
    Calcula la cantidad de dígitos que contiene un número entero.

    Pre: Recibe como parámetro el número entero.
    Post: Retorna un entero correspondiente a la cantidad de dígitos de dicho número.
    """
    if num < 0: # Para que funcione con números negativos
        num = abs(num)
    if num < 10:
        return 1
    else:
        return 1 + calcular_digitos(num // 10)

def main():
    num = pedir_entero("un número entero")
    cant_digitos = calcular_digitos(num)

    print(f"\nEl número {num} contiene {cant_digitos} dígitos.")

main()

