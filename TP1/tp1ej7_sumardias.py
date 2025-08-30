from typing import List

def es_bisiesto(anio: int) -> bool:
    """
    Calcula si el año ingresado es bisiesto o no

    Pre: El año debe ser un entero positivo
    Post: Se devuelve True o False depende si el año es bisiesto o no
    """
    if ((anio % 4 != 0) or (anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0)):
        return False
    else:
        return True

def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """
    Verifica si la fecha ingresada en los tres parámetros (día, mes y año) es válida

    Pre: Los tres parámetros deben ser enteros positivos
    Post: Devuelve True o False de acuerdo a si es válida o no la fecha
    """

    if (mes < 1 or mes > 12) or (dia < 1) or (anio < 1000 or anio > 9999): # Sólo se pueden años de 4 cifras
        return False
    
    elif (dia > 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12)) or (dia > 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11)) or (dia > 29 and mes == 2):
        return False
    
    elif (dia == 29 and mes == 2) and es_bisiesto(anio) == False:
        return False
    
    else:
        return True

def pedir_fecha() -> tuple[int]:
    """
    Pide un día, mes y año y valida que sea correcto con la función declarada arriba

    Pre: No requiere de parámetros
    Post: Se retornan tres números enteros correspondientes al día, mes y el año que proporciona el usuario
    """
    while True:
        dia = int(input("Ingrese el día: "))
        mes = int(input("Ingrese el mes: "))
        anio = int(input("Ingrese el año: "))

        if validar_fecha(dia, mes, anio):
            break
        else:
            print("ERROR - La fecha que usted ingresó es inválida.")
    
    return dia, mes, anio

def pedir_dias() -> int:
    """
    Pide y valida que la cantidad de días sea mayor a 0

    Pre: No requiere de parámetros
    Post: Devuelve el entero que ingresó el usuario luego de pasar la validación
    """
    while True:
        cant_dias = int(input("Ingrese la cantidad de días a sumar: "))
        if cant_dias > 0:
            break
        else:
            print("ERROR - La cantidad de días debe ser 1 o más")
    
    return cant_dias

def pedir_dos_fechas() -> tuple[List[int]]:
    """
    Se piden dos fechas, validando que la primera sea anterior a la segunda

    Pre: No requiere de parámetros
    Post: Retorna dos listas, correspondientes a las dos fechas validadas previamente
    """

    print("---Fecha de inicio---")
    dia1, mes1, anio1 = pedir_fecha()
    
    print("---Fecha final---")
    while True: # Una vez que se tiene la primera fecha, se puede validar la segunda
        dia2, mes2, anio2 = pedir_fecha()
        if (dia1 > dia2 and mes1 == mes2 and anio1 == anio2) or (mes1 > mes2 and anio1 == anio2) or (anio1 > anio2):
            print("ERROR - La primer fecha no puede ser mayor a la segunda.")
        else:
            break
    
    fecha1 = [dia1, mes1, anio1]
    fecha2 = [dia2, mes2, anio2]

    return fecha1, fecha2
        

def dia_siguiente(dia: int, mes: int, anio: int) -> List[int]:
    """
    Calcula el día siguiente de acuerdo al día, mes y año ingresados como parámetros

    Pre: Los parámetros deben constituir una fecha válida y deben ser enteros
    Post: Se devuelve una lista con tres enteros correspondientes al día, mes y año siguientes a la fecha que ingresó
    """
    dia += 1

    # Si el día supera al máximo del mes, pasa a ser el primero del mes siguiente
    if (dia > 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12)) or (dia > 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11)) or ((dia > 29 and mes == 2 and es_bisiesto(anio)) or (dia > 28 and mes == 2 and es_bisiesto(anio) == False)):
        dia = 1
        mes += 1
    if mes > 12: # Si el mes siguiente es 13, pasa a ser el primero de enero del año siguiente
        mes = 1
        anio += 1

    fecha_siguiente = [dia, mes, anio]
    return fecha_siguiente

def sumar_dias(dia: int, mes: int, anio: int, cant_dias: int) -> List[int]:
    """
    Calcula la fecha que será dentro de cierta cantidad de días respecto a la fecha ingresada como parámetro

    Pre: La fecha debe ser válida y la cantidad de días debe ser mayor a 0
    Post: Devuelve una lista con 3 enteros, correspondientes a la fecha que será dentro de N días
    """
    for i in range(cant_dias): # Se usa la función dia_siguiente() las veces que sean la cantidad de días a sumar
        fecha_resultado = dia_siguiente(dia, mes, anio)
        dia, mes, anio = fecha_resultado[0], fecha_resultado[1], fecha_resultado[2]
    
    return fecha_resultado

def calcular_entre_fechas(fecha1: List[int], fecha2: List[int]) -> int:
    """
    Devuelve la cantidad de días que existen entre fecha1 y fecha2

    Pre: Ingresan dos listas con fechas que deben ser validadas previamente, fecha1 debe ser anterior a fecha2
    Post: Devuelve un entero que corresponde a la cantidad de días entre una fecha y otra
    """
    total_dias = 0
    while fecha1 != fecha2: # Hasta que la primera fecha llegue a la segunda, se usa la función dia_siguiente()
        dia, mes, anio = fecha1[0], fecha1[1], fecha1[2]
        fecha1 = dia_siguiente(dia, mes, anio)

        total_dias += 1
    
    return total_dias

def opciones() -> None:
    op = ["Salir del programa", "Mostrar el día siguiente a una fecha",
           "Sumar N días a una fecha", "Calcular cantidad de días entre dos fechas"]
    
    print("Las opciones disponibles son:")
    for num, opcion in enumerate(op):
        print(f"{num}- {opcion}")

def menu():
    op = ""
    while op != "0":
        opciones()
        op = input("Ingrese una de las opciones disponibles: ")

        print()
        if op == "1":
            dia, mes, anio = pedir_fecha()
            fecha_resultado = dia_siguiente(dia, mes, anio)

            dia_sigue, mes_sigue, anio_sigue = fecha_resultado[0], fecha_resultado[1], fecha_resultado[2] # Separa la lista en tres variables para que sea más legible, pero se puede mostrar con los índices directamente
            print(f"El día siguiente a la fecha {dia}/{mes}/{anio} es: {dia_sigue}/{mes_sigue}/{anio_sigue}")

        elif op == "2":
            dia, mes, anio = pedir_fecha()
            cant_dias = pedir_dias()
            fecha_resultado = sumar_dias(dia, mes, anio, cant_dias)

            dia_result, mes_result, anio_result = fecha_resultado[0], fecha_resultado[1], fecha_resultado[2]
            print(f"Luego de sumar {cant_dias} a la fecha {dia}/{mes}/{anio}, sería el día {dia_result}/{mes_result}/{anio_result}")

        elif op == "3":
            fecha1, fecha2 = pedir_dos_fechas()
            total_dias = calcular_entre_fechas(fecha1, fecha2)

            dia1, mes1, anio1 = fecha1[0], fecha1[1], fecha1[2]
            dia2, mes2, anio2 = fecha2[0], fecha2[1], fecha2[2]
            print(f"Entre la fecha {dia1}/{mes1}/{anio1} y la fecha {dia2}/{mes2}/{anio2} hay un total de {total_dias} días transcurridos.")

        elif op == "0":
            print("El programa ha finalizado.")
        
        else:
            print("ERROR - Opción inválida.")
        print()

menu()