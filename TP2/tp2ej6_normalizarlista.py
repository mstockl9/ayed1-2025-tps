from typing import List
import random as rnd

def normalizar(lista: List[int]) -> List[float]:
    """
    Normaliza la lista ingresada como parámetro, de manera que todos sus elementos den como resultado 1.

    Pre: La lista debe contener números enteros y no debe estar vacía.
    Post: Retorna una lista normalizada respetando las proporciones de la lista original.
    """
    total_lista = sum(lista)
    lista_normalizada = list(map(lambda x: x/total_lista, lista)) # A cada elemento de la lista lo divide por la suma total

    return lista_normalizada

def main():
    lista_rnd = [rnd.randint(1, 15) for i in range(10)] # Lista de 10 números aleatorios del 1 al 15
    lista_normaliz = normalizar(lista_rnd)
    total_suma = sum(lista_normaliz)

    print(f"La lista original es:\n{lista_rnd}")
    print(f"La lista normalizada quedaría:\n{lista_normaliz}")
    print(f"\nLa suma total da como resultado: {total_suma}")

main()