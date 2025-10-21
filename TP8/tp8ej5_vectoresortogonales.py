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


def pedir_vector() -> tuple[int]:
    """
    Pide dos enteros correspondientes a las coordenadas de un vector.

    Pre: No recibe parámetros.
    Post: Retorna una tupla con dos enteros correspondientes a las coordenadas del vector
    """
    num1 = pedir_entero("el valor de x")
    num2 = pedir_entero("el valor de y")

    return (num1, num2)


def es_ortogonal(vector1: tuple[int], vector2: tuple[int]) -> bool:
    """
    Determina si los dos vectores ingresados son o no ortogonales (perpendiculares entre sí).

    Pre: Recibe como parámetros dos tuplas con dos enteros cada una, representando sus coordenadas.
    Post: Retorna True si los dos vectores son ortogonales, de lo contrario retorna False.
    """
    return vector1[0] * vector2[0] + vector1[1] * vector2[1] == 0

def main():
    print("---Ingrese el primer vector---")
    vector1 = pedir_vector()
    print("\n---Ingrese el segundo vector---")
    vector2 = pedir_vector()

    print()
    if es_ortogonal(vector1, vector2):
        print(f"Los vectores con coordenadas {vector1} y {vector2} son ortogonales.")
    else:
        print(f"Los vectores con coordenadas {vector1} y {vector2} no son ortogonales.")

main()