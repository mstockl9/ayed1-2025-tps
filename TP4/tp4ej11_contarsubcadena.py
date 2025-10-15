def contar_subcadenas(cadena: str, subcadena: str) -> int:
    """
    Cuenta cuántas veces se encuentra una subcadena dentro de la cadena recibida, sin que sus caracteres
    estén necesariamente en forma consecutiva, pero si en el orden de la subcadena.

    Pre: Recibe como parámetros la cadena original y la subcadena a buscar.
    Post: Retorna un entero correspondiente a la cantidad de veces que se encontró la subcadena.
    """
    cadena = cadena.lower()
    subcadena = subcadena.lower()
    i_subcadena = 0
    cant_encontrado = 0

    for caracter in cadena:
        if caracter == subcadena[i_subcadena]:
            i_subcadena = i_subcadena+1 if i_subcadena < len(subcadena)-1 else 0
            cant_encontrado += 1 if caracter == subcadena[-1] else 0
    
    return cant_encontrado

def main():
    cadena = input("Ingrese una cadena: ")
    subcadena = input("Ingrese la subcadena a buscar: ")
    cant_encontrado = contar_subcadenas(cadena, subcadena)

    print(f"\nLa subcadena '{subcadena}' fue encontrada {cant_encontrado} veces en el texto.")

main()