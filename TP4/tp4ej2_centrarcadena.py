def centrar(cadena: str, separacion: str=" ", ) -> None:
    """
    Imprime la cadena de caracteres centrada en pantalla.

    Pre: Recibe como parámetro la cadena y, si el usuario quiere, la separación a los lados de la cadena, sino son espacios.
    Post: No retorna nada, imprime la cadena centrada en pantalla.
    """
    largo = 80
    sobrante = 1 if len(cadena)%2 else 0 # Si el número de letras del string es impar, se añade una separación más a la derecha para que el total sea 80
    lado = (largo-len(cadena))//2

    cadena_centrada = f"{separacion*lado}{cadena}{separacion*(lado+sobrante)}"
    print(cadena_centrada)

def main():
    cadena = input("Ingrese una palabra o cadena de caracteres: ")
    centrar(cadena, "-")

main()