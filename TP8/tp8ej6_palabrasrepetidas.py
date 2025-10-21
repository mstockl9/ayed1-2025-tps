import re

def eliminar_palabras_repetidas(frase: str) -> str:
    """
    Elimina las palabras repetidas de la frase que recibe, dejando un solo ejemplar de cada una.
    No toma en cuenta signos de puntuación en el resultado.

    Pre: Recibe como parámetro un string correspondiente a la frase.
    Post: Retorna un string con la frase sin palabras repetidas.
    """
    frase_dividida = [palabra for palabra in re.split("[.,;¿?¡!() ]", frase) if palabra] # Divide la frase en palabras sin contar signos de puntuación. Filtra los elementos vacíos que puedan generarse
    frase_dividida = list(set(frase_dividida))
    frase = " ".join(frase_dividida)

    return frase


def ordenar_palabras(frase: str) -> str:
    """
    Ordena las palabras según su longitud de mayor a menor en una cadena.

    Pre: Recibe como parámetro una string correspondiente a una frase.
    Post: Retorna una string con las palabras ordenadas de mayor a menor según su longitud.
    """
    frase_dividida = frase.split()
    frase_dividida = sorted([(len(palabra), palabra) for palabra in frase_dividida], reverse=True)
    frase_dividida = [tupla_palabra[1] for tupla_palabra in frase_dividida]
    frase = " ".join(frase_dividida)

    return frase


def main():
    cadena = input("Ingrese una cadena: ")
    cadena_sin_repetir = eliminar_palabras_repetidas(cadena)
    palabras_ordenadas = ordenar_palabras(cadena_sin_repetir)

    print(f"\nLas palabras sin repetir ordenadas de mayor a menor según su longitud son las siguientes:\n{palabras_ordenadas}")

main()