def es_bisiesto(anio: int) -> bool:
    """
    Calcula si el año ingresado es bisiesto o no

    Pre: El año debe ser un entero positivo
    Post: Se devuelve True o False depende si el año es bisiesto o no
    """
    return not ((anio % 4 != 0) or (anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0))


def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """
    Recibe tres enteros correspondientes a un día, mes y año y determina si la fecha que representan
    es válida o no.

    Pre: Recibe como parámetros tres enteros correspondientes a un día, mes y anio.
    Post: Retorna True si representa una fecha válida, de lo contrario retorna False.
    """
    meses_31_dias = (1, 3, 5, 7, 8, 10, 12)
    meses_30_dias = (4, 6, 9, 11)

    if (mes < 1 or mes > 12) or (dia < 1) or (anio < 1000 or anio > 9999): # Sólo se pueden años de 4 cifras
        return False
    elif (dia > 31 and mes in meses_31_dias) or (dia > 30 and mes in meses_30_dias) or (dia > 29 and mes == 2):
        return False
    elif (dia == 29 and mes == 2) and not es_bisiesto(anio):
        return False
    
    return True


def dia_siguiente(dia: int, mes: int, anio: int) -> tuple[int]:
    """
    Calcula el día siguiente de acuerdo al día, mes y año ingresados como parámetros

    Pre: Los parámetros deben constituir una fecha válida y deben ser enteros
    Post: Se devuelve una tupla con tres enteros correspondientes al día, mes y año siguientes a la fecha que ingresó
    """
    meses_31_dias = (1, 3, 5, 7, 8, 10, 12)
    meses_30_dias = (4, 6, 9, 11)
    dia += 1

    # Si el día supera al máximo del mes, pasa a ser el primero del mes siguiente
    if (dia > 31 and mes in meses_31_dias) or (dia > 30 and mes in meses_30_dias) or ((dia > 29 and mes == 2 and es_bisiesto(anio)) or (dia > 28 and mes == 2 and not es_bisiesto(anio))):
        dia = 1
        mes += 1
    if mes > 12: # Si el mes siguiente es 13, pasa a ser el primero de enero del año siguiente
        mes = 1
        anio += 1

    return dia, mes, anio


def sumar_dias(dia: int, mes: int, anio: int, cant_dias: int) -> tuple[int]:
    """
    Calcula la fecha que será dentro de cierta cantidad de días respecto a la fecha ingresada como parámetro

    Pre: La fecha debe ser válida y la cantidad de días debe ser mayor a 0
    Post: Devuelve una tupla con 3 enteros, correspondientes a la fecha que será dentro de N días
    """
    for _ in range(cant_dias): # Se usa la función dia_siguiente() las veces que sean la cantidad de días a sumar
        dia, mes, anio = dia_siguiente(dia, mes, anio)
    
    return dia, mes, anio


def validar_horario(hora: int, minutos: int, segundos: int) -> bool:
    """
    Recibe tres enteros correspondientes a la hora, los minutos y los segundos y determina si representan
    o no un horario válido.

    Pre: Recibe como parámetros tres enteros correspondientes a la hora, minutos y segundos.
    Post: Retorna True si es un horario válido, de lo contrario retorna False.
    """
    return (hora >= 0 and hora <= 23) and (minutos >= 0 and minutos <= 59) and (segundos >= 0 and segundos <= 59)


def dif_entre_horarios(horario1: tuple[int], horario2: tuple[int]) -> tuple[int]:
    """
    Calcula la diferencia entre los dos horarios ingresados. Si el primer horario es mayor al segundo se considera
    que el primero corresponde al día anterior.

    Pre: Recibe como parámetros dos tuplas de tres enteros, correspondientes a la hora, minutos y segundos de los dos días.
    Post: Retorna una tupla con tres enteros, correspondientes a las horas, minutos y segundos de diferencia entre los dos horarios.
    """
    hora1, minutos1, segundos1 = horario1
    hora2, minutos2, segundos2 = horario2

    if hora1 <= hora2:
        hora_dif = hora2 - hora1
    else:
        hora_dif = 24 - abs(hora2 - hora1)
    
    if minutos1 <= minutos2:
        minutos_dif = minutos2 - minutos1
    else:
        minutos_dif = 60 - abs(minutos2 - minutos1)
        hora_dif = hora_dif - 1 if hora_dif > 0 else 24
    
    if segundos1 <= segundos2:
        segundos_dif = segundos2 - segundos1
    else:
        segundos_dif = 60 - abs(segundos2 - segundos1)
        if minutos_dif > 0:
            minutos_dif -= 1
        else:
            minutos_dif = 0
            hora_dif = 24
    
    return hora_dif, minutos_dif, segundos_dif


def pedir_entero(a_pedir: str) -> int:
    """
    Pide un entero al usuario y valida que sea un número.

    Pre: Recibe como parámetro un string correspondiente al nombre del entero a pedir.
    Post: Retorna el entero validado previamente.
    """
    while True:
        entero = input(f"Ingrese {a_pedir.lower()}: ")
        try:
            entero = int(entero)
        except ValueError:
            print(f"ERROR - {a_pedir.capitalize()} debe ser un número entero.")
        else:
            return entero


def pedir_fecha() -> tuple[int]:
    """
    Pide una fecha al usuario, exigiendo que sea válida utilizando otra función.

    Pre: No recibe parámetros.
    Post: Retorna una tupla con enteros correspondientes al día, mes y el año, validadas previamente con otra función.
    """
    while True:
        dia = pedir_entero("el día")
        mes = pedir_entero("el mes")
        anio = pedir_entero("el año")
        
        if validar_fecha(dia, mes, anio):
            return dia, mes, anio
        else:
            print("ERROR - Fecha inválida.")


def pedir_horario() -> tuple[int]:
    """
    Pide un horario al usuario, exigiendo que sea válido utilizando otra función.

    Pre: No recibe parámetros.
    Post: Retorna una tupla con enteros correspondientes a la hora, minutos y segundos, validadas previamente con otra función.
    """
    while True:
        hora = pedir_entero("la hora")
        minutos = pedir_entero("los minutos")
        segundos = pedir_entero("los segundos")

        if validar_horario(hora, minutos, segundos):
            return hora, minutos, segundos
        else:
            print("ERROR - Horario inválido.")


def mostrar_opciones(op: tuple[str]) -> None:
    """
    Imprime y enumera las opciones que recibe como parámetro. La primera opción debe ser la de salir del programa.

    Pre: Recibe como parámetro una tupla con strings correspondientes a las opciones.
    Post: No retorna nada, imprime y enumera las opciones.
    """
    print("Las opciones disponibles son las siguientes:")
    for i, opcion in enumerate(op):
        print(f"{i}- {opcion}")


def menu():
    opciones = ("Salir del programa", "Sumar N días a una fecha.", "Calcular la diferencia entre dos horarios.")
    while True:
        mostrar_opciones(opciones)
        op = input("Ingrese una de las opciones disponibles: ").strip()

        print()
        if op == "1":
            dia, mes, anio = pedir_fecha()
            n = pedir_entero("el valor de días a sumar")

            dia_result, mes_result, anio_result = sumar_dias(dia, mes, anio, n)
            print(f"\nEl resultado de sumar {n} días a la fecha {dia}/{mes}/{anio} es el siguiente:\n{dia_result}/{mes_result}/{anio_result}")
        
        elif op == "2":
            print("---Ingrese los datos del primer horario---")
            primer_horario = pedir_horario()
            print("\n---Ingrese los datos del segundo horario---")
            segundo_horario = pedir_horario()

            hora_dif, minutos_dif, segundos_dif = dif_entre_horarios(primer_horario, segundo_horario)
            print(f"\nEntre el primer horario y el segundo horario hay {hora_dif} hora/s, {minutos_dif} minuto/s y {segundos_dif} segundo/s de diferencia.")
        
        elif op == "0":
            print("El programa ha finalizado.")
            break

        else:
            print("ERROR - Opción inválida.")
        print()

menu()