from typing import List

def pedir_n() -> int:
    """
    Pide al usuario el valor de N para realizar las matrices con los patrones de N x N, validando que sea mayor a 2.

    Pre: No recibe parámetros.
    Post: Retorna el valor de N, validado previamente.
    """
    while True:
        n = int(input("Ingrese el valor de N: "))
        if n > 1:
            break
        else:
            print("ERROR - El valor de N debe ser de mínimo 2.")
    
    return n

def diagonal_descen_impar(n: int) -> List[List[int]]:
    """
    Genera una matriz de N x N con un patrón que consiste en una diagonal descendente de impares,
    con el resto de números siendo 0.

    Pre: N debe ser un entero positivo.
    Post: Retorna la matriz de N x N con el patrón descrito previamente.
    """
    matriz = [[] for fila in range(n)]

    for i, fila in enumerate(matriz):
        nro_impar = i * 2 + 1
        for x in range(n):
            if i == x:
                fila.append(nro_impar)
            else:
                fila.append(0)
                
    return matriz

def diagonal_ascen_x3(n: int) -> List[List[int]]:
    """
    Genera una matriz de N x N con un patrón que consiste en una diagonal ascendente de números a partir
    del 1 que se multiplican por 3, con el resto de números siendo 0.

    Pre: N debe ser un entero positivo.
    Post: Retorna la matriz de N x N con el patrón descrito previamente.
    """
    matriz = [[] for fila in range(n)]
    nro_x3 = 1

    for i, fila in enumerate(matriz):
        for x in range(n):
            if i == x:
                fila.append(nro_x3)
            else:
                fila.append(0)
        nro_x3 *= 3
    
    matriz.reverse()
    return matriz

def escalonado_filas(n: int) -> List[List[int]]:
    """
    Genera una matriz de N x N con un patrón que consiste en una escalera descendente de izquierda a derecha,
    con números del 1 hasta N puestos en filas. El resto de números es 0.

    Pre: N debe ser un entero positivo.
    Post: Retorna la matriz de N x N con el patrón descrito previamente.
    """
    matriz = [[] for fila in range(n)]
    max_nro = n

    for i, fila in enumerate(matriz):
        for x in range(n):
            if x <= i:
                fila.append(max_nro)
            else:
                fila.append(0)
        max_nro -= 1
    
    return matriz

def filas_x2(n: int) -> List[List[int]]:
    """
    Genera una matriz de N x N con un patrón que consiste en filas que van desde 1 abajo de todo, y van multiplicando
    entre dos a medida que van subiendo.

    Pre: N debe ser un entero positivo.
    Post: Retorna la matriz de N x N con el patrón descrito previamente.
    """
    matriz = [[] for fila in range(n)]
    nro_x2 = 1

    for fila in matriz:
        for x in range(n):
            fila.append(nro_x2)
        nro_x2 *= 2
    
    matriz.reverse()
    return matriz

def entre_ceros(n: int) -> List[List[int]]:
    """
    Genera una matriz de N x N con un patrón que consiste en números desde el 1 hasta Nx2 separados por ceros
    entre las filas de la matriz.

    Pre: N debe ser un entero positivo.
    Post: Retorna la matriz de N x N con el patrón descrito previamente.
    """
    matriz = [[] for fila in range(n)]
    nro = 1
    cero = True

    for fila in matriz:
        for x in range(n):
            if cero:
                fila.append(0)
            else:
                fila.append(nro)
                nro += 1
            cero = not cero
        if not n%2:
            cero = not cero
    
    return matriz

def escalonado_proced(n: int) -> List[List[int]]:
    """
    Genera una matriz de N x N con un patrón que consiste en números desde el 1 hasta Nx2 separados por ceros
    entre las filas de la matriz.

    Pre: N debe ser un entero positivo.
    Post: Retorna la matriz de N x N con el patrón descrito previamente.
    """
    matriz = [[] for fila in range(n)]
    nro = 1

    for i, fila in enumerate(matriz):
        for x in range(n):
            if x <= i:
                fila.append(nro)
                nro += 1
            else:
                fila.append(0)
        fila.reverse()
    
    return matriz

def espiral(n: int) -> List[List[int]]:
    """
    Genera una matriz de N x N con un patrón que consiste en una progresión de números que rellena la matriz
    en forma de espiral recta, empezando desde el extremo superior izquierdo.

    Pre: N debe ser un entero positivo.
    Post: Retorna la matriz de N x N con el patrón descrito previamente.
    """
    matriz = [[0 for columna in range(n)] for fila in range(n)]
    nro = 1
    columna = -1
    fila = 0
    fin = n
    fin_inv = -1
    reverso = False

    while nro <= n**2:
        if not reverso:
            columna += 1
            for columna in range(columna, fin):
                matriz[fila][columna] = nro
                nro += 1
            
            fila += 1
            for fila in range(fila, fin):
                matriz[fila][columna] = nro
                nro += 1
            
            fin -= 1
        
        else:
            columna -= 1
            for columna in range(columna, fin_inv, -1):
                matriz[fila][columna] = nro
                nro += 1
            
            fin_inv += 1
            fila -= 1
            for fila in range(fila, fin_inv, -1):
                matriz[fila][columna] = nro
                nro += 1
        
        reverso = not reverso

    return matriz

def filas_diagonales(n: int) -> List[List[int]]:
    """
    Genera una matriz de N x N con un patrón que consiste en filas diagonales números del 1 a N**2.
    La diagonal se forma de forma descendente desde el extremo superior izquierdo.

    Pre: N debe ser un entero positivo.
    Post: Retorna la matriz de N x N con el patrón descrito previamente. 
    """
    matriz = [[] for i in range(n)]
    num = 1
    
    for fila in range(n):
        matriz[fila].append(num)
        num += 1
        for recorrer in range(fila+1):
            if len(matriz[recorrer]) == n:
                continue
            matriz[recorrer].append(num)
            num += 1
    
    # Rellena el resto de la matriz cuando el bucle de arriba termina con sólo dos números en la última fila
    for rellenar in range(2, n):
        matriz[rellenar].append(num)
        num += 1
        for recorrer in range(rellenar+1, n):
            if len(matriz[recorrer]) == n:
                continue
            matriz[recorrer].append(num)
            num += 1
    
    return matriz

def zigzag_diagonal(n: int) -> List[List[int]]:
    """
    Genera una matriz con un patrón que consiste en números del 1 a N**2 en forma de zig zag diagonal de forma descendente
    desde el extremo superior izquierdo.

    Pre: N debe ser un entero positivo.
    Post: Retorna la matriz de N x N con el patrón descrito previamente.
    """
    matriz = [[] for i in range(n)]
    num = 1
    reverso = False
    
    for fila in range(n):
        matriz[fila].append(num)
        if not reverso:
            num += fila+1
        else:
            num += fila+2
        if fila == n-1:
            if reverso:
                num -= 2
            break
        for recorrer in range(fila+1):
            if len(matriz[recorrer]) == n:
                continue
            matriz[recorrer].append(num)
            if not reverso:
                num += 1
            else:
                num -= 1
        reverso = not reverso

    # Rellena el resto de la matriz cuando el bucle de arriba termina con sólo dos números en la última fila
    for rellenar, rellenar_inv in zip(range(1, n), range(n-2, -1, -1)):
        matriz[rellenar].append(num)
        if reverso:
            num_sup = num
        for recorrer in range(rellenar+1, n):
            if len(matriz[recorrer]) == n:
                continue
            if not reverso:
                num += 1
            else:
                num -= 1
            matriz[recorrer].append(num)
        
        if not reverso:
            num += rellenar_inv
        else:
            num = num_sup+1

        reverso = not reverso

    return matriz

def mostrar_matriz(matriz: List[List[int]]) -> None:
    """
    Imprime la matriz por filas.

    Pre: Recibe la matriz como parámetro, que no debe estar vacía.
    Post: Imprime una por una las listas internas de la matriz. No retorna nada.
    """
    for fila in matriz:
        print(fila)

def main():
    n = pedir_n()
    titulos = ("Diagonal descendente de impares", "Diagonal ascendente multiplicado por tres", "Filas escalonadas", "Filas multiplicadas por dos", "Secuencia entre ceros", "Escalonado procedural",
               "Espiral", "Filas diagonales", "Zigzag diagonal")
    matrices = (diagonal_descen_impar(n), diagonal_ascen_x3(n), escalonado_filas(n), filas_x2(n), entre_ceros(n), escalonado_proced(n), espiral(n), filas_diagonales(n), zigzag_diagonal(n))
    
    print()
    for titulo, matriz in zip(titulos, matrices):
        print(titulo)
        mostrar_matriz(matriz)
        print()

main()