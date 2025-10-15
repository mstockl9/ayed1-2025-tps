import re
from typing import List

def validar_correo(direccion_correo: str) -> bool:
    """
    Recibe una dirección de correo electrónico y determina si es válida o no.

    Pre: Recibe como parámetro una cadena correspondiente a la dirección de correo.
    Post: Retorna True si la dirección es válida o False si no lo es.
    """
    patron_correo = "[a-zA-Z0-9]+@[a-zA-Z]+.com(.ar)?"
    return bool(re.fullmatch(patron_correo, direccion_correo))

def listar_dominios(lista_correos: List[str]) -> List[str]:
    """
    Realiza un listado de todos los dominios ordenados alfabéticamente de los correos que ingresan.

    Pre: Recibe como parámetro una lista con cadenas correspondientes a direcciones de correo electrónico, que no debe estar vacía.
    Post: Retorna una lista de cadenas ordenadas alfabéticamente con los dominios ingresados sin repetir.
    """
    lista_dominios = []
    patron_dominio = "@([a-zA-z]+)."

    for direccion in lista_correos:
        coincidencias = re.findall(patron_dominio, direccion)
        lista_dominios.extend(coincidencias)
    
    lista_dominios = [dominio.title() for dominio in lista_dominios]
    lista_dominios = list(set(lista_dominios))
    lista_dominios = sorted(lista_dominios)

    return lista_dominios
    
def main():
    lista_correos = []
    while True:
        direccion = input("Ingrese una dirección de correo electrónico: ")
        if not direccion:
            break

        if validar_correo(direccion):
            lista_correos.append(direccion)
            print("Correo electrónico registrado con éxito.")
        else:
            print("ERROR - Dirección de correo no válida.")
    
    if lista_correos:
        lista_dominios = listar_dominios(lista_correos)
        print("\nLa lista de todos los dominios ingresados es la siguiente:")
        for dominio in lista_dominios:
            print(dominio)
    else:
        print("\nNo se registraron correos electrónicos.")

main()