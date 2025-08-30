def pedir_positivo() -> int:
    """
    Pide y valida que el número sea positivo

    Pre: No se ingresan parámetros
    Post: Devuelve el número que ingresó el usuario
    """

    while True:
        num = int(input("Ingrese un número natural: "))
        if num > 0:
            break
        else:
            print("ERROR - El número debe ser mayor que 0.")
    
    return num

def main():
    num = pedir_positivo()
    es_oblongo = lambda x: int(x**(0.5)) * (int(x**(0.5))+1) == x # Si la parte entera de la raiz cuadrada del número, multiplicada por si misma más uno es igual al número que se ingresó, el número es oblongo
    es_triangular = lambda x: not ((8*x + 1)**0.5) % 1 # Si la raíz cuadrada del número multiplicado 8 y sumado 1 es una raíz perfecta (es un entero), el número es triangular (Si da 0.0 es False, negado es True)

    print()
    if es_oblongo(num):
        print(f"El número {num} es oblongo.")
    else:
        print(f"El número {num} no es oblongo.")
    
    if es_triangular(num):
        print(f"El número {num} es triangular.")
    else:
        print(f"El número {num} no es triangular.")

main()