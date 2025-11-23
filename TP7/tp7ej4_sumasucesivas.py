def pedir_entero(a_pedir: str) -> int:
    """
    Pide un entero al usuario y valida que sea un número y que sea mayor o igual a 0.

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
            if entero >= 0:
                return entero
            else:
                print("ERROR - El número debe ser mayor o igual a 0.")

def calcular_producto_sucesivo(a: int, b: int) -> int:
    """
    Calcula el producto de A y B mediante sumas sucesivas. A y B deben ser enteros mayores o iguales a 0.

    Pre: Recibe como parámetros dos enteros correspondientes a A y B. Ambos deben ser mayores o iguales a 0.
    Post: Retorna un entero correspondiente al resultado de A x B.
    """
    if a == 0 or b == 0: # Si alguno de los dos es 0 directamente retorna 0
        return 0
    if b == 1:
        return a
    else:
        return a + calcular_producto_sucesivo(a, b - 1)

def main():
    a = pedir_entero("el valor de A")
    b = pedir_entero("el valor de B")
    producto = calcular_producto_sucesivo(a, b)

    print(f"\nEl resultado de {a} x {b} es de: {producto}")

main()