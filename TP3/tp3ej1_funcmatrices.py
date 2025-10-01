from typing import List
import copy

def pedir_n() -> int:
    """
    Pide al usuario el valor de N, valida que sea 2 o mayor y lo retorna.

    Pre: No recibe parámetros.
    Post: Retorna el valor de N, validado previamente.
    """
    while True:
        n = int(input("Ingrese las dimensiones que va a tener la matriz: "))
        if n < 2:
            print("ERROR - Debe ser mayor o igual a 2.")
        else:
            break
    
    return n

def cargar_matriz(n: int) -> List[List[int]]:
    """
    Genera una matriz de N x N y pide al usuario los elementos de cada fila y columna.

    Pre: Recibe el valor de N, que debe ser un entero positivo.
    Post: Retorna la matriz de N x N cargada con los datos que ingresó el usuario.
    """
    matriz = []

    for fila in range(n):
        matriz.append([])
        for columna in range(n):
            print(f"--Fila {fila+1}, Columna {columna+1}--")
            dato = int(input("Ingrese el número a ingresar: "))
            matriz[fila].append(dato)

    return matriz

def ordenar_filas(matriz: List[List[int]]) -> List[List[int]]:
    """
    Ordena de forma ascendente cada fila de la matriz que ingresa como parámetro.
    No modifica a la matriz original.

    Pre: La matriz no debe estar vacía.
    Post: Retorna una matriz con cada fila ordenada de forma ascendente.
    """
    matriz_local = matriz.copy()
    for i, fila in enumerate(matriz_local):
        matriz_local[i] = sorted(fila)
        
    return matriz_local

def intercambiar_filas(fila1: int, fila2: int, matriz: List[List[int]]) -> List[List[int]]:
    """
    Intercambia de lugar dos filas de la matriz, cuya posición (no índice) se ingresa como parámetro.
    No modifica a la matriz original.

    Pre: La matriz no debe estar vacía, y las filas ingresadas como parámetros deben existir.
    Post: Retorna una matriz con las filas intercambiadas.
    """
    matriz_local = matriz.copy()

    fila1 -= 1
    fila2 -= 1
    matriz_local[fila1], matriz_local[fila2] = matriz_local[fila2], matriz_local[fila1]

    return matriz_local

def intercambiar_columnas(columna1: int, columna2: int, matriz: List[List[int]]) -> List[List[int]]:
    """
    Intercambia de lugar dos columnas de la matriz, cuya posición (no índice) se ingresa como parámetro.
    No modifica a la matriz original.

    Pre: La matriz no debe estar vacía, y las columnas ingresadas como parámetros deben existir.
    Post: Retorna una matriz con las columnas intercambiadas.
    """
    matriz_local = copy.deepcopy(matriz)

    columna1 -= 1
    columna2 -= 1
    for fila in range(len(matriz_local)):
        matriz_local[fila][columna1], matriz_local[fila][columna2] = matriz_local[fila][columna2], matriz_local[fila][columna1]
    
    return matriz_local

def trasponer_matriz(matriz: List[List[int]]) -> List[List[int]]:
    """
    Traspone la matriz sobre sí misma, es decir, por cada elemento, por ejemplo matriz[2, 1] pasaría
    a ser matriz[1, 2]. No modifica a la matriz original.
    """
    matriz_local = copy.deepcopy(matriz)
    n = len(matriz_local)

    for fila in range(n):
        for columna in range(n):
            matriz_local[fila][columna] = matriz[columna][fila]
    
    return matriz_local

def promedio_matriz(fila: int, matriz: List[List[int]]) -> float:
    """
    Calcula el promedio de todos los elementos de la fila (posición) recibida como parámetro.

    Pre: La matriz no debe estar vacía. La fila ingresada debe existir.
    Post: Retorna un flotante correspondiente al promedio de todos los elementos de la fila. 
    """
    fila -= 1
    total_fila = sum(matriz[fila])
    cant_fila = len(matriz[fila])

    return total_fila / cant_fila

def calcular_porcent_impar(columna: int, matriz: List[List[int]]) -> float:
    """
    Calcula el porcentaje de elementos con valor impar en la columna ingresada como parámetro.

    Pre: Se recibe la columna (la posición, no el índice) y la matriz a calcular. La matriz no debe estar vacía y la columna debe existir.
    Post: Retorna el porcentaje de números impares en la columna.
    """
    columna -= 1
    total_numeros = len(matriz)
    total_impares = len([fila[columna] for fila in matriz if fila[columna] % 2])

    return total_impares * 100 / total_numeros

def simetrica_diag_principal(matriz: List[List[int]]) -> bool:
    """
    Determina si la matriz es simétrica respecto a su diagonal principal (descendente, de izquierda a derecha).

    Pre: La matriz no debe estar vacía y debe ser tener forma cuadrada (NxN).
    Post: Retorna True si la matriz es simétrica, de lo contrario retorna False.
    """
    lista_arriba = []
    lista_abajo = []

    # Hace una deepcopy y da vuelta la matriz para el segundo bucle for
    matriz_inv = copy.deepcopy(matriz)
    matriz_inv.reverse()

    for i, fila in enumerate(matriz): # Recorre de arriba hacia abajo, la parte superior derecha respecto a la diagonal de izquierda a derecha
        lista_arriba.extend(fila[i+1: ])
    
    for i, fila in enumerate(matriz_inv): # Recorre de abajo hacia arriba, la parte inferior izquierda respecto a la diagonal de derecha a izquierda
        fila.reverse()
        lista_abajo.extend(fila[i+1: ])

    return lista_arriba == lista_abajo # Si reunieron los mismos números, la lista es simétrica

def simetrica_diag_secundaria(matriz: List[List[int]]) -> bool:
    """
    Determina si la matriz es simétrica respecto a su diagonal secundaria (ascendente, de izquierda a derecha).

    Pre: La matriz no debe estar vacía y debe ser tener forma cuadrada (NxN).
    Post: Retorna True si la matriz es simétrica, de lo contrario retorna False.
    """
    lista_arriba = []
    lista_abajo = []

    # Hace una deepcopy y da vuelta la matriz para el segundo bucle for
    matriz_inv = copy.deepcopy(matriz)
    matriz_inv.reverse()

    for i, fila in enumerate(matriz): # Recorre de arriba hacia abajo, la parte superior izquierda respecto a la diagonal de derecha a izquierda
        lista_arriba.extend(fila[-i-2: -len(matriz)-1: -1]) # Desde uno antes de la diagonal hasta el principio de la fila
    
    for i, fila in enumerate(matriz_inv): # Recorre de abajo hacia arriba, la parte inferior derecha respecto a la diagonal de izquierda a derecha
        lista_abajo.extend(fila[i+1: ])

    return lista_arriba == lista_abajo # Si reunieron los mismos números, la lista es simétrica

def calcular_capicuas(matriz: List[List[int]]) -> List[int]:
    """
    Determina qué columnas de la matriz son capicúa, devolviendo sus posiciones (no índices).
    
    Pre: La matriz no debe estar vacía.
    Post: Retorna una lista con los enteros correspondientes a las posiciones de las columnas que son capicúa.
    """
    posiciones_capicua = []

    for columna in range(len(matriz[0])):
        lista_columna = [fila[columna] for fila in matriz]
        lista_columna_inv = lista_columna.copy()
        lista_columna_inv.reverse()
        
        if lista_columna == lista_columna_inv:
            posiciones_capicua.append(columna+1)
    
    return posiciones_capicua

def mostrar_matriz(matriz):
    """
    Imprime las filas de la matriz una debajo de la otra.

    Pre: Recibe la matriz como parámetro.
    Post: No retorna nada, solo imprime la matriz por filas.
    """
    for fila in matriz:
        print(fila)

def main():
    n = pedir_n()
    matriz = cargar_matriz(n)
    lista_comentarios = ("Matriz original:", "Filas ordenadas en forma ascendente:", "Intercambiadas las filas 1 y 3:", "Intercambiadas las columnas 1 y 3:",
                         "Traspuesta sobre sí misma:", "Promedio de los elementos de la fila 1:", "Porcentaje de valores impares en la columna 1:",
                         "Es simétrica respecto a su diagonal principal:", "Es simétrica respecto a su diagonal secundaria:", "Posiciones de columnas capicúa:")
    lista_datos = (matriz, ordenar_filas(matriz), intercambiar_filas(1, 3, matriz), intercambiar_columnas(1, 3, matriz), trasponer_matriz(matriz), promedio_matriz(1, matriz),
                   calcular_porcent_impar(1, matriz), simetrica_diag_principal(matriz), simetrica_diag_secundaria(matriz), calcular_capicuas(matriz))

    print("-"*40)
    for comentario, dato in zip(lista_comentarios, lista_datos):
        print(comentario)
        if isinstance(dato, List) and len(dato) and isinstance(dato[0], List): # Si es una matriz llama a la función de imprimir matrices
            mostrar_matriz(dato)
        else:
            print(dato)

main()