from typing import List

def pedir_ayb() -> tuple[int]:
    """
    Pide los números A y B y valida que estos sean enteros y que el primero sea mayor al segundo.

    Pre: No se reciben parámetros.
    Post: Retorna una tupla con los números A y B dentro.
    """
    while True:
        a = int(input("Ingrese el valor de A: "))
        b = int(input("Ingrese el valor de B: "))
        if b <= a:
            print("ERROR - Números inválidos.")
        else:
            break
    
    return a, b


def multiplos7no5(a: int, b: int) -> List[int]:
    """
    Genera una lista con los números entre A y B que son múltiplos de 7 que no son múltiplos de 5.

    Pre: Recibe como parámetros los enteros A y B. A no puede ser mayor ni igual a B.
    Post: Retorna la lista mencionada previamente.
    """
    return [elem for elem in range(a, b+1) if not elem % 7 and elem % 5]

def main():
    a, b = pedir_ayb()
    lista_multip7no5 = multiplos7no5(a, b)
    print(f"La lista de números entre {a} y {b} que son múltiplos de 7 y no son múltiplos de 5 es la siguiente:\n{lista_multip7no5}")

main()