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

def binario_a_decimal(binario: int, posicion=0) -> int:
    """
    Convierte el número binario ingresado a base decimal.

    Pre: Recibe como parámetro un entero correspondiente al número binario.
    Post: Retorna un entero correspondiente al número en base decimal que representa.
    """
    if len(str(binario)) == 1:
        return binario * 2**posicion
    else:
        calculo_digito = (binario % 10) * 2**posicion
        return calculo_digito + binario_a_decimal(binario // 10, posicion+1)

def main():
    binario = pedir_entero("un número binario")
    decimal = binario_a_decimal(binario)

    print(f"\nEl número binario {binario} convertido a base decimal es: {decimal}")

main()