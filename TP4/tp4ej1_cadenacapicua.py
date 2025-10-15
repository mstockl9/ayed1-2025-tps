def es_capicua(cadena: str) -> bool:
    """
    Devuelve True o False dependiendo si la cadena de caracteres ingresada es o no capicúa.

    Pre: Recibe una cadena como parámetro.
    Post: Retorna True si la cadena es capicúa o False si no lo es.
    """

    mitad, sobrante = divmod(len(cadena), 2)
    if sobrante: # Redondea para arriba, también se podría con math.ceil()
        mitad += 1
    
    for i, i_inv in zip(range(mitad), range(-1, -(mitad)-1, -1)): # Compara el primer caracter con el último, el segundo con el anteúltimo, etc., a la vez hasta llegar al medio
        if cadena[i] != cadena[i_inv]:
            return False
    
    return True

def main():
    cadena = input("Ingrese una palabra o cadena de caracteres: ")
    if es_capicua(cadena):
        print("La cadena que usted ingresó es capicúa.")
    else:
        print("La cadena que usted ingresó no es capicúa.")

main()