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

def extraer_subcadena_v1(cadena: str, posicion: int, caracteres: int) -> str: # Usa slices
    """
    Extrae la subcadena de la cadena ingresada, que comience en la posición recibida y tenga la cantidad
    de caracteres deseada.

    Pre: Recibe como parámetros la cadena, la posición en la que comienza la subcadena y la cantidad de caracteres que debe tener.
    Post: Retorna una string correspondiente a dicha subcadena con las características ingresadas.
    """
    return cadena[posicion:posicion+caracteres]

def extraer_subcadena_v2(cadena: str, posicion: int, caracteres: int) -> str: # No usa slices
    """
    Extrae la subcadena de la cadena ingresada, que comience en la posición recibida y tenga la cantidad
    de caracteres deseada.

    Pre: Recibe como parámetros la cadena, la posición en la que comienza la subcadena y la cantidad de caracteres que debe tener.
    Post: Retorna una string correspondiente a dicha subcadena con las características ingresadas.
    """
    subcadena = ""
    
    for c in range(posicion, posicion+caracteres):
        if c >= len(cadena): # Si se sale del rango de caracteres de la cadena, rompe el bucle y la retorna hasta el final, similar al slice
            break
        subcadena += cadena[c]
    
    return subcadena

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    posicion, caracteres = pedir_posicion_y_caract()
    subcadena_v1, subcadena_v2 = extraer_subcadena_v1(cadena, posicion, caracteres), extraer_subcadena_v2(cadena, posicion, caracteres)

    print(f"\nLa subcadena comenzando desde la posición {posicion}, con {caracteres} caracteres es la siguiente:")
    print(f"Versión 1: {subcadena_v1}")
    print(f"Versión 2: {subcadena_v2}")

main()