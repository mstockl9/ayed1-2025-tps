from typing import List

def pedir_entero() -> int:
    """
    Pide un número y controla que sea uno válido.

    Pre: No recibe parámetros.
    Post: Retorna el número ingresado validado previamente.
    """
    while True:
        entero = input("Ingrese un número: ")
        try:
            entero = int(entero)
        except ValueError:
            print("ERROR - Debe ingresar un número entero.")
        else:
            return entero

def armar_lista() -> List[int]:
    """
    Arma una lista de números que pide al usuario hasta que ingrese -1.

    Pre: No recibe parámetros.
    Post: Retorna la lista con números ingresados por el usuario.
    """
    lista_numeros = []
    while True:
        nro = pedir_entero()
        if nro == -1:
            break
        lista_numeros.append(nro)
    
    return lista_numeros

def main():
    lista_numeros = armar_lista()
    
    print(f"\nLa lista se construyó con éxito, comienza la búsqueda de números...")
    intentos = 0
    while intentos < 3:
        a_buscar = pedir_entero()

        try:
            posicion = lista_numeros.index(a_buscar)+1
        except ValueError:
            print("ERROR - El número que usted ingresó no se encuentra en la lista.")
            intentos += 1
        else:
            print(f"El número {a_buscar} se encuentra en la posición {posicion}.")
        print()
    
    print("Se excedió el límite de 3 errores detectados, el proceso ha finalizado.")

main()