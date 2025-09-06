import random as rnd
from typing import List

def pedir_cant() -> int:
    """
    Pide la cantidad de elementos y valida que sea mayor a 0.

    Pre: No recibe parámetros.
    Post: Retorna el número validado que ingresó el usuario.
    """
    while True:
        cant_elementos = int(input("Ingrese la cantidad de elementos de la lista aleatoria: "))
        if cant_elementos < 1:
            print("ERROR - La cantidad de elementos debe ser un número positivo.")
        else:
            break
    
    return cant_elementos

def generar_lista_rnd(cant_elem: int) -> List[int]:
    """
    Genera una lista de elementos aleatorios del 1 al 100. La cantidad de elementos es ingresada
    como parámetro.

    Pre: Recibe la cantidad de elementos, que debe ser un entero positivo.
    Post: Retorna la lista cargada con N elementos aleatorios.
    """
    return [(rnd.randint(1, 100)) for x in range(cant_elem)]

def contiene_repetidos(lista: List[int]) -> bool:
    """
    Determina si la lista contiene o no algún elemento repetido retornando True o False.

    Pre: La lista no debe estar vacía y debe contener números enteros.
    Post: Retorna True o False dependiendo si hay elementos repetidos o no.
    """
    for elem in lista:
        if lista.count(elem) > 1:
            return True
    
    return False

def eliminar_repetidos(lista: List[int]) -> List[int]:
    """
    Devuelve una nueva lista sin los elementos repetidos de la lista que ingresa. No modifica la lista original

    Pre: La lista no debe estar vacía y debe contener números enteros.
    Post: Retorna una nueva lista sin los elementos repetidos
    """
    lista_local = lista.copy()

    if contiene_repetidos(lista):
        
        for elem in lista_local:
            for i in range(lista_local.count(elem)-1): # Borra los elementos extra de la lista al contarlos, si se encontraron 4 iguales, se borran 3 dejando uno único. Si se encuentra uno sólo, al restarse 1 el bucle for no se ejecuta
                lista_local.remove(elem)
    
    return lista_local

def main():
    cant_elementos = pedir_cant()
    lista_rnd = generar_lista_rnd(cant_elementos)
    print(f"La lista generada es la siguiente:\n{lista_rnd}")

    print()
    if contiene_repetidos(lista_rnd):
        lista_sin_repetidos = eliminar_repetidos(lista_rnd)
        print(f"La lista contiene elementos repetidos, la misma lista sin repetidos quedaría así:\n{lista_sin_repetidos}")
    else:
        print("La lista no contiene elementos repetidos.")

main()