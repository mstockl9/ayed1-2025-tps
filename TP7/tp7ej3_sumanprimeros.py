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

def calcular_n_primeros(n: int) -> int:
    """
    Calcula la suma de los N primeros números naturales.

    Pre: Recibe como parámetro un entero correspondiente al valor de N.
    Post: Retorna un entero correspondiente a la suma de 1 hasta N.
    """
    if n == 1:
        return 1
    else:
        return n + calcular_n_primeros(n - 1)

def main():
    n = pedir_entero("el valor de N")
    suma_hasta_n = calcular_n_primeros(n)

    print(f"\nLa suma de los {n} primeros números naturales es de: {suma_hasta_n}")

main()