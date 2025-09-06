import random
from typing import List

def eliminar_de_lista(lista_orig: List, lista_a_eliminar: List) -> List:
    """
    Elimina de la lista original todos los valores que se encuentran en la segunda lista ingresada
    como parámetro. Modifica la lista original.

    Pre: Ambas listas no deben estar vacías y la segunda lista debería contener valores que tenga la
    lista original.
    Post: Retorna la lista original modificada, sin los valores de la segunda lista.
    """
    for a_eliminar in lista_a_eliminar:
        for veces in range(lista_orig.count(a_eliminar)):
            lista_orig.remove(a_eliminar)
    
    return lista_orig

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
    a_eliminar = [3, 8]

    print(f"Lista original: {lista}")
    print(f"Valores a eliminar: {a_eliminar}")
    print(f"Lista resultante: {eliminar_de_lista(lista, a_eliminar)}")

main()
