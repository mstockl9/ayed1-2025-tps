def buscar_clave(diccionario: dict, a_buscar) -> list:
    """
    Devuelve la lista de claves que apunten o mapeen al valor recibido.

    Pre: Recibe como parámetros el diccionario y el valor a buscar en las claves.
    Post: Retorna una lista con las claves que apunten al valor.
    """
    lista_claves = [clave for clave, valor in diccionario.items() if valor == a_buscar]

    return lista_claves

def main():
    diccionario = {"nombre": "banana", "color_exterior": "amarillo", "letras": 6, "vocales": 3, "consonantes": 3, "nombre_ingles": "banana", "color_interior": "amarillo", "silabas": 3, "continente_origen": "asia"} # Diccionario de ejemplo, tiene valores de enteros y strings que se repiten
    print(f"El diccionario es el siguiente:\n{diccionario}")

    a_buscar = input("\nIngrese el valor a buscar entre las claves: ").lower().strip()
    if a_buscar.isdigit():
        a_buscar = int(a_buscar)
    
    print()
    lista_claves = buscar_clave(diccionario, a_buscar)
    if lista_claves:
        print(f"La lista de claves que apuntan a el dato '{a_buscar}' son las siguientes:")
        for clave in lista_claves:
            print(clave)
    else:
        print("No hay claves que apunten a ese dato.")

main()