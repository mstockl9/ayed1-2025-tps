import re

def ordenar_palabras(cadena: str, descendente: bool=True) -> str:
    """
    Ordena en una cadena todas las palabras de la cadena recibida ordenadas por su longitud.
    Los signos de puntuación no se toman en cuenta al momento de calcular las longitudes.

    Pre: Recibe una cadena de caracteres y un booleano, que sería False en caso de querer ordenar de forma ascendente y en caso contrario, True o sin aclarar.
    Post: Retorna una cadena con las palabras ordenadas de menor a mayor según su longitud.
    """
    lista_cadena = cadena.split() # Se dividen las palabras separadas por espacios en una lista
    longitudes_tupla = [(len(palabra) - (len(re.findall("[.,;¿?¡!()]", palabra))), palabra) for palabra in lista_cadena] # Por cada palabra en la lista acumula el len(), restando los signos de puntuación que encuentre (el len() de la lista que genere el re.findall()) y la palabra en una tupla
    longitudes_tupla = sorted(longitudes_tupla, reverse=descendente) # sorted() ordena las tuplas teniendo en cuenta su primer elemento (correspondiente a la longitud) en la lista
    cadena = " ".join([tupla_longitud[1] for tupla_longitud in longitudes_tupla]) # Se junta en una cadena el segundo elemento (correspondiente a la palabra) de cada tupla, separado por espacios

    return cadena

def main():
    cadena = input("Ingrese una cadena: ")
    cadena_ord = ordenar_palabras(cadena)
    print(f"\nLa cadena que usted ingresó con las palabras ordenadas según su longitud es la siguiente:\n{cadena_ord}")

main()