def pedir_posicion_y_caract() -> tuple[int]:
    """
    Pide la posición y la cantidad de caracteres, controlando que ambos sean positivos.

    Pre: No recibe parámetros.
    Post: Retorna una tupla con la posición y la cantidad de caracteres ingresados por el usuario y validados previamente.
    """
    while True:
        posicion = input("Ingrese la posición de inicio: ")
        caracteres = input("Ingrese la cantidad de caracteres desde esa posición: ")
        try:
            posicion = int(posicion)
            caracteres = int(caracteres)
        except ValueError:
            print("ERROR - Ambos deben ser números enteros.")
        else:
            if posicion > 0 and caracteres > 0:
                return posicion, caracteres
            else:
                print("ERROR - Ambos deben ser números positivos.")

def eliminar_subcadena_v1(cadena: str, posicion: int, caracteres: int) -> str: # Usa slices
    """
    Elimina la subcadena de la cadena ingresada, que comience en la posición recibida y tenga la cantidad
    de caracteres deseada.

    Pre: Recibe como parámetros la cadena, la posición en la que comienza la subcadena y la cantidad de caracteres que tiene.
    Post: Retorna una string correspondiente a la cadena ingresada sin la subcadena con las características recibidas.
    """
    return cadena[:posicion] + cadena[posicion+caracteres:]

def eliminar_subcadena_v2(cadena: str, posicion: int, caracteres: int) -> str: # No usa slices
    """
    Elimina la subcadena de la cadena ingresada, que comience en la posición recibida y tenga la cantidad
    de caracteres deseada.

    Pre: Recibe como parámetros la cadena, la posición en la que comienza la subcadena y la cantidad de caracteres que tiene.
    Post: Retorna una string correspondiente a la cadena ingresada sin la subcadena con las características recibidas.
    """
    subcadena = ""
    
    for c in range(len(cadena)):
        if c >= posicion and c < posicion+caracteres:
            continue
        elif c >= len(cadena):
            break

        subcadena += cadena[c]
    
    return subcadena

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    posicion, caracteres = pedir_posicion_y_caract()
    subcadena_v1, subcadena_v2 = eliminar_subcadena_v1(cadena, posicion, caracteres), eliminar_subcadena_v2(cadena, posicion, caracteres)

    print(f"\nLa subcadena sin los caracteres desde la posición {posicion} seguido de {caracteres} caracteres es la siguiente:")
    print(f"Versión 1: {subcadena_v1}")
    print(f"Versión 2: {subcadena_v2}")

main()