import random as rnd
from typing import List

def pedir_nym() -> tuple[int]:
    """
    Pide al usuario los valores de N y de M, los valida y los retorna.

    Pre: No recibe parámetros.
    Post: Retorna los valores de N y M validados previamente.
    """
    while True:
        n = int(input("Ingrese el valor de N: "))
        m = int(input("Ingrese el valor de M: "))
        if n > 0 and m > 0:
            break
        else:
            print("ERROR - Valores inválidos.")
    
    return n, m

def mostrar_butacas(matriz_butacas: List[List[str]]) -> None:
    """
    Muestra por pantalla el estado de cada una de las butacas del cine.

    Pre: Recibe la matriz de butacas, que no debe estar vacía.
    Post: Imprime cada una de las butacas y su estado, libre o reservado.
    """
    for fila in matriz_butacas:
        print(fila)

def reservar(matriz_butacas: List[List[int]], butaca_selec: int) -> bool:
    """
    Actualiza el estado de la butaca que seleccionó el usuario para reservar.

    Pre: Recibe la matriz de butacas, que no debe estar vacía, y el número de butaca seleccionada.
    Post: Modifica la matriz y retorna True en caso de reservarse con éxito, o False en caso de no estar disponible dicha butaca.
    """
    i_fila = 0
    i_butaca = -1

    if butaca_selec < 1 or butaca_selec > sum([len(fila) for fila in matriz_butacas]):
        return False

    for i in range(butaca_selec):
        i_butaca += 1
        if i_butaca > len(matriz_butacas[0])-1:
            print(i_fila, i_butaca)
            i_fila += 1
            i_butaca = 0
    
    if not matriz_butacas[i_fila][i_butaca]:
        matriz_butacas[i_fila][i_butaca] = 1
        return True
    else:
        return False

def cargar_sala(matriz_butacas: List[List], m: int) -> None:
    """
    Carga con valores aleatorios la matriz de butacas para simular una sala con butacas ya reservadas.

    Pre: Recibe la matriz a cargar, que debe estar vacía.
    Post: Carga la matriz con M valores aleatorios de 0 y 1 en cada fila. No retorna nada
    """
    for fila in matriz_butacas:
        for butaca in range(m):
            fila.append(rnd.randint(0, 1))

def butacas_libres(matriz_butacas: List[List[int]]) -> int:
    """
    Calcula cuántas butacas desocupadas hay en la sala de cine.

    Pre: Recibe la matriz de butacas como parámetro, que no debe estar vacía.
    Post: Retorna un entero correspondiente a la cantidad de butacas libres.
    """
    cant_libres = 0
    for fila in matriz_butacas:
        for butaca in fila:
            if not butaca:
                cant_libres += 1
    
    return cant_libres

def butacas_contiguas(matriz_butacas: List[List[int]]) -> tuple[int]:
    """
    Encuentra las coordenadas de inicio de la secuencia más larga de butacas libres contiguas en una misma fila.

    Pre: Recibe la matriz de butacas como parámetro, que no debe estar vacía.
    Post: Retorna una tupla con dos enteros, correspondientes al número de fila y número de butaca (no los índices).
    """
    max_butacas_seguidas = 0
    fila_contigua = 0
    butaca_contigua = 0

    for i, fila in enumerate(matriz_butacas):
        butacas_seguidas = 0
        for x, butaca in enumerate(fila):
            if not butaca:
                butacas_seguidas += 1
            else:
                if butacas_seguidas > max_butacas_seguidas:
                    max_butacas_seguidas = butacas_seguidas
                    fila_contigua = i+1
                    butaca_contigua = x-butacas_seguidas+1
                butacas_seguidas = 0
    
    return fila_contigua, butaca_contigua

def opciones() -> None:
    op = ["Salir del programa", "Mostrar butacas", "Reservar butaca", "Calcular butacas libres", "Calcular secuencia más larga de butacas contiguas"]
    
    print("Las opciones disponibles son las siguientes:")
    for i, opcion in enumerate(op):
        print(f"{i}- {opcion}")

def menu():
    n, m = pedir_nym()
    matriz_butacas = [[] for fila in range(n)]
    cargar_sala(matriz_butacas, m)

    while True:
        opciones()
        op = input("Ingrese una de las opciones disponibles: ").strip()

        print()
        if op == "1":
            print("El estado de las butacas es el siguiente (1: Reservado, 0: Sin reservar):")
            mostrar_butacas(matriz_butacas)
        
        elif op == "2":
            butaca_seleccionada = int(input("Ingrese el número de la butaca: "))
            if reservar(matriz_butacas, butaca_seleccionada):
                print("La butaca se reservó con éxito.")
            else:
                print("ERROR - La butaca que usted ingresó no existe o ya está reservada.")
        
        elif op == "3":
            cant_butacas_libres = butacas_libres(matriz_butacas)
            print(f"La cantidad de butacas libres en la sala de cine es de: {cant_butacas_libres} butacas.")
        
        elif op == "4":
            fila_contigua, butaca_contigua = butacas_contiguas(matriz_butacas)
            print(f"La secuencia más larga de butacas libres seguidas en la sala de cine comienza en la fila {fila_contigua}, butaca {butaca_contigua}.")
        
        elif op == "0":
            print("El programa ha finalizado.")
            break
        
        else:
            print("ERROR - Opción inválida")
        print()

menu()