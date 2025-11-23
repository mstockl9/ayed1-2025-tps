def pedir_entero(a_pedir: str, min) -> int:
    """
    Pide un entero al usuario y valida que sea un número y que sea mayor o igual al mínimo establecido.

    Pre: Recibe como parámetro un string correspondiente al nombre del entero a pedir y un entero correspondiente al mínimo posible.
    Post: Retorna el entero validado previamente.
    """
    while True:
        entero = input(f"Ingrese {a_pedir.lower()}: ")
        try:
            entero = int(entero)
        except ValueError:
            print(f"ERROR - {a_pedir.capitalize()} debe ser un número entero.")
        else:
            if entero >= min:
                return entero
            else:
                print(f"ERROR - El número debe ser mayor o igual a {min}.")

def calcular_resto_sucesivo(a: int, b: int) -> int:
    """
    Calcula el resto de A entre B mediante restas sucesivas.

    Pre: Recibe como parámetros dos enteros correspondientes a A y B. B no puede ser 0 y tanto A como B deben ser enteros positivos (exceptuando si A es 0).
    Post: Retorna un entero correspondiente al resto de A entre B
    """
    if a < b:
        return a
    else:
        return calcular_resto_sucesivo(a - b, b)

def main():
    a = pedir_entero("el valor de A", 0)
    b = pedir_entero("el valor de B", 1)
    resto = calcular_resto_sucesivo(a, b)

    print(f"\nEl resto de calcular {a} entre {b} es de: {resto}")

main()