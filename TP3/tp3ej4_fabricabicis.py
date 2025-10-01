import random as rnd
from typing import List

def pedir_fabricas() -> int:
    """
    Pide el número de fábricas que deben almacenarse en la matriz y valida que sea mayor a 0.

    Pre: No recibe parámetros.
    Post: Retorna el valor otorgado por el usuario.
    """
    while True:
        n_fabricas = int(input("Ingrese la cantidad de fábricas: "))
        if n_fabricas > 0:
            break
        else:
            print("ERROR - La cantidad de fábricas debe ser un entero positivo.")
    
    return n_fabricas

def mostrar_total_x_fabrica(matriz_fabricas: List[List[int]]) -> None:
    """
    Imprime un listado del total de bicicletas fproducidas en la semana por cada fábrica.

    Pre: Recibe como parámetro la matriz de las fábricas, que no debe estar vacía.
    Post: No retorna nada, sólo imprime el listado.
    """
    print("La lista del total de bicicletas producidas por cada fábrica es la siguiente:")
    for i, fabrica in enumerate(matriz_fabricas):
        print(f"Fábrica N°{i+1}: {sum(fabrica)} bicicletas producidas en total.")

def calcular_mayor_prod(matriz_fabrica: List[List[int]]) -> tuple[int, int]:
    """
    Calcula la fábrica que más produjo en un solo día.

    Pre: Recibe como parámetro la matriz de las fábricas, que no debe estar vacía.
    Post: Retorna una tupla con dos enteros correspondientes al número de fábrica y al día de la semana.
    """
    mayor_prod_x_fabrica = [max(fabrica) for fabrica in matriz_fabrica] # Almacena la mayor cantidad producida en un día de cada fábrica

    mayor_produccion = max(mayor_prod_x_fabrica) # Saca cual de esas cantidades es la mayor
    fabrica_mayor_prod = mayor_prod_x_fabrica.index(mayor_produccion) # El índice de la mayor producción es también el índice de la lista que representa la fábrica
    dia_mayor_prod = matriz_fabrica[fabrica_mayor_prod].index(mayor_produccion) # Saca el índice de la mayor producción en la lista de la fábrica con la mayor producción

    return fabrica_mayor_prod+1, dia_mayor_prod

def dia_mas_productivo(matriz_fabrica: List[List[int]]) -> int:
    """
    Calcula el día con mayor cantidad de producciones considerando los datos de todas las fábricas combinadas.

    Pre: Recibe como parámetro la matriz de las fábricas, que no debe estar vacía.
    Post: Retorna el entero correspondiente al día más productivo.
    """
    total_produccion_x_dia = [sum([fabrica[dia] for fabrica in matriz_fabrica]) for dia in range(len(matriz_fabrica[0]))] # Suma el total de producción de todas las fábricas por cada día
    dia_mayor_produccion = total_produccion_x_dia.index(max(total_produccion_x_dia)) # Saca el índice del mayor número en la lista

    return dia_mayor_produccion

def menor_produccion_x_fabrica(matriz_fabrica: List[List[int]]) -> List[int]:
    """
    Calcula la menor cantidad de producción por cada fábrica.

    Pre: Recibe como parámetro la matriz de las fábricas, que no debe estar vacía.
    Post: Retorna una lista con enteros correspondientes a la menor cantidad de producción por fábrica.
    """
    return [min(fabrica) for fabrica in matriz_fabrica]

def opciones() -> None:
    op = ["Salir del programa", "Mostrar el total de bicicletas producidas por fábrica", "Mostrar la fábrica que más produjo", "Mostrar el día más productivo considerando todas las fábricas",
          "Mostrar la menor cantidad fabricada por cada fábrica"]
    
    print("Las opciones disponibles son las siguientes:")
    for i, opcion in enumerate(op):
        print(f"{i}- {opcion}")

def menu():
    cant_dias = 6
    cant_fabricas = pedir_fabricas()
    matriz_fabricas = [[rnd.randint(0, 150) for dia in range(cant_dias)] for fabrica in range(cant_fabricas)]
    dias_str = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado")
    for fila in matriz_fabricas:
        print(fila)
    
    while True:
        opciones()
        op = input("Ingrese una de las opciones disponibles: ").strip()
    
        print()
        if op == "1":
            mostrar_total_x_fabrica(matriz_fabricas)
        
        elif op == "2":
            fabrica_mayor_prod, dia_mayor_prod = calcular_mayor_prod(matriz_fabricas)
            print(f"La fábrica que más produjo en un sólo día fue la Fábrica N°{fabrica_mayor_prod} en el día {dias_str[dia_mayor_prod]}.")
        
        elif op == "3":
            dia_mayor_produccion = dia_mas_productivo(matriz_fabricas)
            print(f"El día más productivo considerando la producción de todas las fábricas fue el día {dias_str[dia_mayor_produccion]}")
        
        elif op == "4":
            menores_producciones = menor_produccion_x_fabrica(matriz_fabricas)
            print("La lista de menores cantidades producidas por fábrica es la siguiente:")
            for i, cantidad in enumerate(menores_producciones):
                print(f"Fábrica N°{i+1}: {cantidad} bicicleta/s producidas.")
        
        elif op == "0":
            print("El programa ha finalizado.")
            break

        else:
            print("ERROR - Opción inválida.")
        print()

menu()