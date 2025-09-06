from typing import List
import random as rnd

def intercalar(lista1: List, lista2: List) -> List:
    """
    Devuelve una lista resultante de intercalar las dos listas ingresadas como parámetros
    de manera entrelazada. Se modifica la primera lista (lista1).

    Pre: Las dos listas no deben estar vacías y pueden contener enteros, float o strings.
    Post: Retorna el resultado de intercalar las dos listas.
    """
    longitud_lista1 = len(lista1)
    longitud_lista2 = len(lista2)
    total_longitud = longitud_lista1 + longitud_lista2
    mas_corto = min([longitud_lista1, longitud_lista2])

    for i, dato_lista2 in zip(range(mas_corto), lista2):
        i_impar = i * 2 + 1 # Va a ser un impar en cada iteración
        lista1[i_impar:i_impar] = [dato_lista2] # lista1[1:1] = [x] no reemplaza el índice 1 de lista1 por x, sino que lo agrega entre medio de lista1[1] y lista1[2]
    
    if len(lista1) < total_longitud: # Al intercalarse la lista en base a lista1, si faltan elementos, se agregan los restantes de lista2
        lista1.extend(lista2[mas_corto: ])
    
    return lista1
    
def main():
    lista1 = [rnd.randint(1, 9) for i in range(rnd.randint(1, 10))]
    lista2 = [rnd.randint(1, 9) for i in range(rnd.randint(1, 10))]
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")

    lista_intercalada = intercalar(lista1, lista2)
    print(f"\nLista intercalada: {lista_intercalada}")

main()