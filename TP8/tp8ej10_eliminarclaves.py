def eliminar_claves(diccionario: dict, lista_claves: list) -> tuple[dict, int]:
    """
    Elimina del diccionario recibido todas las claves contenidas en la lista ingresada.
    Si no encuentra alguna de las claves no hace nada y pasa a la siguiente.

    Pre: Recibe como parámetros un diccionario y una lista con elementos correspondientes a las claves a eliminar.
    Post: Retorna una tupla con el diccionario modificado y un entero correspondientes a la cantidad de claves eliminadas.
    """
    diccionario_mod = {clave: valor for clave, valor in diccionario.items() if clave not in lista_claves}
    cant_eliminadas = len(diccionario) - len(diccionario_mod)
    
    return diccionario_mod, cant_eliminadas


def main():
    diccionario = {"manzana": 7, "frutilla": 8, "kiwi": 4, "banana": 6, "naranja": 7, "durazno": 7, "sandía": 6, "mango": 5}
    lista_claves = []

    print(f"El diccionario original es el siguiente:\n{diccionario}\n")
    while True:
        a_eliminar = input("Ingrese una clave para eliminar (-1 para salir): ")
        if a_eliminar == "-1":
            break

        lista_claves.append(a_eliminar)
    
    diccionario_mod, cant_eliminadas = eliminar_claves(diccionario, lista_claves)
    print(f"\nEl diccionario modificado sin las claves que usted ingresó es el siguiente:\n{diccionario_mod}")
    print(f"Se eliminaron {cant_eliminadas} claves en total.")

main()