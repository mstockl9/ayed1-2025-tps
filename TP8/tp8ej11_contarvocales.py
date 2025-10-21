import re

def contar_vocales(cadena: str) -> dict:
    """
    Cuenta cuántas veces apareció cada vocal en la palabra o frase ingresada.

    Pre: Recibe como parámetro una cadena.
    Post: Retorna un diccionario con cada vocal y las veces que aparece en la cadena.
    """
    diccionario_vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    cadena = cadena.lower()

    for vocal in diccionario_vocales.keys():
        diccionario_vocales[vocal] = cadena.count(vocal)
    
    return diccionario_vocales

def main():
    cadena = input("Ingrese una cadena: ")
    lista_cadena = [palabra for palabra in re.split("[.,;¿?¡!() ]", cadena) if palabra]

    for palabra in lista_cadena:
        print()
        diccionario_vocales = contar_vocales(palabra)
        print(f"'{palabra}'")
        for vocal, cant_vocal in diccionario_vocales.items():
            print(f"{vocal}: {cant_vocal}")

main()