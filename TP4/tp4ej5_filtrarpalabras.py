def pedir_n() -> int:
    """
    Pide un número y controla que sea mayor a 0.

    Pre: No recibe parámetros.
    Post: Retorna el número ingresado validado previamente.
    """
    while True:
        n = input("Ingrese un número: ")
        try:
            n = int(n)
        except ValueError:
            print("ERROR - Debe ingresar un número entero.")
        else:
            if n > 0:
                return n
            else:
                print("ERROR - El valor de N debe ser positivo.")

def filtrar_palabras_v1(frase: str, n: int) -> str: # Usa ciclos normales
    """
    Devuelve un string con las palabras de la frase ingresada, que tengan una cantidad igual o mayor
    al entero recibido como parámetro.
    
    Pre: Recibe una cadena con una frase y un número entero N.
    Post: Retorna una cadena con las palabras de dicha frase que contengan N o más carácteres. 
    """
    frase = frase.split()
    palabras_menor_o_n = []
    for palabra in frase:
        if len(palabra) >= n:
            palabras_menor_o_n.append(palabra)
    
    palabras_menor_o_n = " ".join(palabras_menor_o_n)

    return palabras_menor_o_n
    
def filtrar_palabras_v2(frase: str, n: int) -> str: # Usa listas por comprensión
    """
    Devuelve un string con las palabras de la frase ingresada, que tengan una cantidad igual o mayor
    al entero recibido como parámetro.
    
    Pre: Recibe una cadena con una frase y un número entero N.
    Post: Retorna una cadena con las palabras de dicha frase que contengan N o más carácteres. 
    """
    frase = frase.split()
    palabras_menor_o_n = " ".join([palabra for palabra in frase if len(palabra) >= n])

    return palabras_menor_o_n

def filtrar_palabras_v3(frase: str, n: int) -> str: # Usa la función filter
    """
    Devuelve un string con las palabras de la frase ingresada, que tengan una cantidad igual o mayor
    al entero recibido como parámetro.
    
    Pre: Recibe una cadena con una frase y un número entero N.
    Post: Retorna una cadena con las palabras de dicha frase que contengan N o más carácteres. 
    """
    frase = frase.split()
    palabras_menor_o_n = " ".join(list(filter(lambda palabra: len(palabra) >= n, frase)))

    return palabras_menor_o_n

def main():
    frase = input("Ingrese una frase: ")
    n = pedir_n()
    resultado = (filtrar_palabras_v1(frase, n), filtrar_palabras_v2(frase, n), filtrar_palabras_v3(frase, n))

    print("\nLa frase que usted ingresó con las palabras de N o más caracteres es la siguiente:")
    for v, x in enumerate(resultado):
        print(f"Versión {v+1}: {x}")

main()