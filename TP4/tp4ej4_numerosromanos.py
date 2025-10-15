def pedir_numero() -> int:
    """
    Pide al usuario un número para la conversión a romano, y valida que se encuentre entre 1 y 3999 para que dicha conversión sea posible,
    (con números de 4000 para arriba conllevaría una implmentar líneas encima de algunos números para indicar que los mismos se multiplican por mil, al no poder poner 4 "M" seguidas).

    Pre: No recibe parámetros.
    Post: Retorna el número ingresado por el usuario, validado previamente.
    """
    while True:
        num = input("Ingrese un número entre 1 y 3999: ")
        try:
            num = int(num)
        except ValueError:
            print("ERROR - Debe ingresar un número entero.")
        else:
            if num >= 1 and num <= 3999:
                return num
            else:
                print("ERROR - El número debe ser entre 1 y 3999 para que su conversión sea posible.")

def pasar_a_romanos(num: int) -> str:
    """
    Convierte el número ingresado a números romanos.

    Pre: Recibe como parámetro un número entero, que debe estar entre 1 y 3999 para que sea posible su conversión.
    Post: Retorna una cadena correspondiente a la expresión en números romanos del número ingresado.
    """
    diccionario_romanos = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    num_en_romano = ""

    for entero, romano in diccionario_romanos.items():
        cant_unidad = num // entero
        num %= entero

        num_en_romano += romano*cant_unidad
    
    return num_en_romano

def main():
    num = pedir_numero()
    num_en_romano = pasar_a_romanos(num)
    print(f"El número {num} expresado en números romanos es el siguiente: {num_en_romano}")

main()