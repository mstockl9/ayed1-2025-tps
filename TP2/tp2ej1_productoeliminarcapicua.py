import random as rnd
from typing import List

def cargar_lista_rnd() -> List[int]:
    """
    Carga una lista con elementos aleatorios de 4 digitos. La cantidad de elementos es, a su vez,
    un número aleatorio de 2 digitos.

    Pre: La función no recibe parámetro alguno.
    Post: Se retorna una lista de enteros, con las características aleatorias descritas previamente 
    """

    return [(rnd.randint(1000, 9999)) for i in range(rnd.randint(10, 99))]

def multiplicar_lista(lista: List[int]) -> int:
    """
    Calcula el resultado de multiplicar todos los elementos de la lista de enteros que ingresa.

    Pre: La lista no debe estar vacía.
    Post: Retorna un entero, correspondiente al producto de todos los elementos de la lista
    """

    multiplicador = 1
    for elem in lista:
        multiplicador *= elem
    
    return multiplicador

def eliminar_de_lista(lista: List[int], a_eliminar: int) -> List[int]:
    """
    Elimina todas las apariciones del valor ingresado en la lista, modificándola.

    Pre: Se recibe el valor a eliminar, y la lista del que se debe eliminar
    Post: Retorna la lista que ingresó, sin el valor a eliminar.
    """
    cant_encontrado = lista.count(a_eliminar)
    for i in range(cant_encontrado): # No especifica si se debe modificar o no la lista pero dice sin listas auxiliares. Para no modificarla se podría usar lista.copy()
        lista.remove(a_eliminar)
    
    return lista

def es_capicua(lista: List[int]) -> bool:
    """
    Devuelve True o False dependiendo si la lista ingresada es o no capicúa.

    Pre: Recibe la lista de enteros como parámetro. La lista no debe estar vacía.
    Post: Retorna True si la lista es capicúa o False si no lo es.
    """

    mitad, sobrante = divmod(len(lista), 2)
    if sobrante: # Redondea para arriba, también se podría con math.ceil()
        mitad += 1
    
    for i, i_inv in zip(range(mitad), range(-1, -(mitad)-1, -1)): # Compara el primer elemento con el último, el segundo con el anteúltimo, etc., a la vez hasta llegar al medio
        if lista[i] != lista[i_inv]:
            return False
    
    return True

def main():
    lista = cargar_lista_rnd()
    print(f"La lista cargada aleatoriamente es la siguiente:\n{lista}")

    producto_lista = multiplicar_lista(lista)
    print(f"\nEl producto de todos los elementos de la lista es de: {producto_lista}")

    eliminar_valor = int(input("\nIngrese el valor que quiere eliminar de la lista: "))
    lista_mod = eliminar_de_lista(lista, eliminar_valor)
    print(f"La lista sin el valor que usted ingresó es la siguiente:\n{lista_mod}")

    print()
    if es_capicua(lista):
        print("La lista generada es capicúa.")
    else:
        print("La lista generada no es capicúa.")

main()