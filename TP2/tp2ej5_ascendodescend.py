import random as rnd
from typing import List

def ascendente_o_descendente(lista: List) -> bool:
    """
    Recibe una lista ordenada y determina si la misma está ordenada de forma ascendente o descendente.

    Pre: La lista debe estar ordenada de alguna de las dos formas y no debe estar vacía.
    Post: Retorna True si la lista es ascendente, y False si es descendente.
    """
    return lista[0] < lista[-1]

def main():
    lista_random = [rnd.randint(1, 100) for x in range(20)] # Lista de 20 elementos aleatorios del 1 al 100
    lista_ordenada = sorted(lista_random, reverse=(rnd.randint(0, 1))) # Ordena la lista, cuyo tipo de ordenamiento se decide aleatoriamente
    
    if ascendente_o_descendente(lista_ordenada):
        print(f"La lista aleatoria está ordenada de forma ascendente:\n{lista_ordenada}")
    else:
        print(f"La lista aleatoria está ordenada de forma descendente:\n{lista_ordenada}")

main()