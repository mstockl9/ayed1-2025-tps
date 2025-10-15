def pedir_clave_maestra() -> int:
    """
    Pide la clave maestra al usuario, validando que contenga por lo menos dos dígitos.

    Pre: No recibe parámetros.
    Post: Retorna la clave maestra validada previamente.
    """
    while True:
        clave_maestra = int(input("Ingrese la clave maestra: "))
        if clave_maestra >= 10:
            return clave_maestra
        else:
            print("ERROR - La clave debe tener mínimo dos dígitos.")

def calcular_claves(clave_maestra: int) -> tuple[int]:
    """
    Calcula las dos claves según la clave maestra ingresada como parámetro.

    Pre: Recibe como parámetro un entero de mínimo 2 dígitos.
    Post: Retorna una tupla con las dos claves correspondientes.
    """
    clave_maestra_str = str(clave_maestra)
    clave1 = int(clave_maestra_str[: :2])
    clave2 = int(clave_maestra_str[1: :2])

    return clave1, clave2

def main():
    clave_maestra = pedir_clave_maestra()
    clave1, clave2 = calcular_claves(clave_maestra)

    print(f"\nClave maestra: {clave_maestra}\nClave 1: {clave1}\nClave 2: {clave2}")

main()