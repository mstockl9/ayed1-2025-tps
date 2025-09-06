from typing import List

def pedir_n() -> int:
    """
    Pide al usuario el valor de N y valida que sea un entero positivo.

    Pre: No ingresan parámetros.
    Post: Retorna el valor ingresado por el usuario y validado previamente.
    """
    while True:
        n = int(input("Ingrese el valor de N: "))
        if n < 1:
            print("ERROR - N debe ser un positivo.")
        else:
            break
    
    return n

def listar_cuadrados(n: int) -> List[int]:
    """
    Genera una lista con los cuadrados de los números del 1 hasta el parámetro ingresado por el usuario
    (ambos incluídos).

    Pre: N debe ser un entero positivo.
    Post: Retorna una lista con N elementos enteros, correspondientes a los cuadrados del 1 a N.
    """
    return [elem**2 for elem in range(1, n+1)]

def main():
    n = pedir_n()
    lista_cuadr = listar_cuadrados(n)

    if len(lista_cuadr) <= 10:
        print(f"La lista de cuadrados del 1 al {n} es la siguiente:\n{lista_cuadr}")
    else:
        print(f"Los últimos 10 valores de la lista de cuadrados del 1 al {n} es la siguiente:\n{lista_cuadr[n-10:]}")

main()