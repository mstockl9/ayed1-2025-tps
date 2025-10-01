from typing import List
import random as rnd

def pedir_n() -> int:
    """
    Pide al usuario el valor de N, valida que sea positivo y lo retorna.

    Pre: No recibe parámetros.
    Post: Retorna el valor de N, validado previamente.
    """
    while True:
        n = int(input("Ingrese las dimensiones que va a tener la matriz: "))
        if n < 1:
            print("ERROR - Debe ser un número positivo.")
        else:
            break
    
    return n

def cargar_matriz(n: int) -> List[List[int]]:
    """
    Genera una matriz de N x N con números enteros al azar entre 0 y N al cuadrado de forma
    que ninguno se repite.

    Pre: N debe ser un entero positivo.
    Post: Retorna una matriz con las características descriptas previamente.
    """
    matriz = [[] for i in range(n)]
    for fila in range(n):
        for columna in range(n):
            while True:
                num_rnd = rnd.randint(0, n**2)
                repetido = False
                for comprobar in matriz:
                    if num_rnd in comprobar:
                        repetido = True
                
                if not repetido:
                    matriz[fila].append(num_rnd)
                    break
    
    return matriz

def main():
    n = pedir_n()
    matriz = cargar_matriz(n)
    for fila in matriz:
        print(fila)

main()