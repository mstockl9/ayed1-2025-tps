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

def ultimos_caracteres(cadena: str, n: int) -> str:
    """
    Retorna una subcadena con los últimos N caracteres de la cadena ingresada. Si el valor de n es mayor
    a la cantidad de caracteres de la cadena, se retorna la cadena completa

    Pre: Recibe la cadena original y el número de últimos caracteres que se desea extraer.
    Post: Retorna la subcadena con los últimos N caracteres.
    """
    inicio = len(cadena)-n if n <= len(cadena) else 0
    return cadena[inicio:]

def main():
    cadena = input("Ingrese una cadena: ")
    n = pedir_n()
    subcadena = ultimos_caracteres(cadena, n)
    print(f"\nLos últimos {n} caracteres de la cadena ingresada son los siguientes:\n{subcadena}")

main()