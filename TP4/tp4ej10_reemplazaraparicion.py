import re

def reemplazar_apariciones(cadena: str, a_buscar: str, reemplazo: str) -> tuple[str, int]:
    """
    Reemplaza todas las apariciones de una palabra por otra en una cadena de caracteres y calcula la cantidad de reemplazos
    realizados. Sólo se reemplazan palabras completas, no fragmentos de palabras.

    Pre: Recibe como parámetros la cadena original, la palabra a buscar y el reemplazo de cada una de sus apariciones.
    Post: Retorna una tupla con la cadena modificada y un entero correspondiente a la cantidad de reemplazos realizados.
    """
    lista_cadena = cadena.split()
    longitud_buscar = len(a_buscar)
    cant_reemplazos = 0
    
    for i, palabra in enumerate(lista_cadena):
        # Si se encuentra una coincidencia, y la longitud de la palabra a buscar es igual a la longitud de la palabra en la lista sin los signos de puntuación significa que es la misma palabra y no una subcadena
        if re.findall(a_buscar, palabra) and len(palabra) - len(re.findall("[.,;¿?¡!()]", palabra)) == longitud_buscar:
            lista_cadena[i] = lista_cadena[i].replace(a_buscar, reemplazo) # Con el replace() reemplaza la palabra pero mantiene los signos de puntuación
            cant_reemplazos += 1
    cadena = " ".join(lista_cadena)

    return cadena, cant_reemplazos

def main():
    cadena = input("Ingrese una cadena: ")
    a_buscar = input("Ingrese la palabra que desea reemplazar en toda la cadena: ")
    reemplazo = input("Ingrese la palabra que debe reemplazar a la palabra indicada: ")
    cadena_mod, cant_reemplazos = reemplazar_apariciones(cadena, a_buscar, reemplazo)
    
    print(f"\nLa cadena con todas las apariciones de '{a_buscar}' reemplazadas por '{reemplazo}' es la siguiente:")
    print(f"\n{cadena_mod}\nLa cantidad de palabras reemplazadas es de {cant_reemplazos}")

main()