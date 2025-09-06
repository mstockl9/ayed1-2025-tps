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
    longitud_total = longitud_lista1 + longitud_lista2 # Lo que tendría que medir la lista al final del proceso es la suma de los len()
    mas_corto = min([longitud_lista1, longitud_lista2])
    i_lista1 = 0

    for i_lista2 in range(mas_corto):
        lista1[i_lista1 : i_lista1+1] = [lista1[i_lista1], lista2[i_lista2]] # El subindice 0 de lista1 se reemplaza por lista1 y lista2 subindice 0, quedando el primer elemento de lista1 y siendo el siguiente el de lista2
        i_lista1 += 2 # Se suman dos ya que se agregan 2 números por cada número de lista1
    
    # Si el len() más corto era el de lista2, la lista ya está completa, debido a que lo que sobra de lista1 quedó en dicha lista, ya que la intercalación se construye a partir de ella
    # Si el más corto era el de lista1, quedán por agregar los elementos sobrantes de lista2
    if len(lista1) < longitud_total:
        lista1.extend(lista2[mas_corto: ]) # Se extiende la lista con lo restante de lista2
    
    return lista1

def main():
    lista1 = [rnd.randint(1, 9) for i in range(rnd.randint(1, 10))]
    lista2 = [rnd.randint(1, 9) for i in range(rnd.randint(1, 10))]
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")

    lista_intercalada = intercalar(lista1, lista2)
    print(f"\nLista intercalada: {lista_intercalada}")

main()