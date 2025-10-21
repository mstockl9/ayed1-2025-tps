import re

def fragmentar_correo(direccion_correo: str) -> tuple[str]:
    """
    Retorna las distintas partes que conforman el correo electrónico ingresado siempre y cuando sea
    un formato válido.

    Pre: Recibe como parámetro un string correspondiente a la dirección de correo electrónico.
    Post: Retorna una tupla con strings correspondientes a las partes que componen la dirección. Si la misma está en un formato inválido, se retorna una tupla vacía.
    """
    patron_correo = "[a-zA-Z0-9]+@[a-zA-Z]+.[a-zA-Z]+\.[a-zA-Z]{2,}"
    if not bool(re.fullmatch(patron_correo, direccion_correo)):
        return ()
    
    patron_partes = "[@.]"
    partes_correo = tuple(re.split(patron_partes, direccion_correo))

    return partes_correo


def main():
    correo = input("Ingrese la dirección de correo electrónico: ")
    partes_correo = fragmentar_correo(correo)

    print()
    if partes_correo:
        print("Las partes que componen al correo electrónico que usted ingresó son las siguientes:")
        for p in partes_correo:
            print(p, end=" ")
    else:
        print("ERROR - La dirección de correo electrónico que usted ingresó es inválida.")

main()