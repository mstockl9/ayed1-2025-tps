from typing import List

def generar_naipes() -> List[str]:
    """
    Genera una lista con los naipes de la baraja española.

    Pre: No recibe parámetros.
    Post: Retorna una lista con cadenas correspondientes a los naipes de la baraja española
    """
    palos = ("Oros", "Espadas", "Bastos", "Copas")
    lista_naipes = [str(naipe)+" "+palo for palo in palos for naipe in range(1, 13) if naipe < 8 or naipe > 9]

    return lista_naipes

def main():
    lista_naipes = generar_naipes()
    print(f"La lista generada con los naipes de cartas en la baraja española es la siguiente:\n{lista_naipes}")

main()