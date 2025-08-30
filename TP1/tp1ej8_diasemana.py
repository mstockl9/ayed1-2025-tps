def validar_fecha(mes: int, anio: int) -> bool:
    """
    Verifica si el mes y el año ingresado en los parámetros son válidos

    Pre: Los dos parámetros deben ser enteros positivos
    Post: Devuelve True o False de acuerdo a si es válida o no la fecha
    """
    if (mes < 1 or mes > 12) or (anio < 1000 or anio > 9999):
        return False

    else:
        return True

def pedir_fecha() -> tuple[int]:
    """
    Pide un mes y un año, validando que sea correcto con la función declarada arriba

    Pre: No requiere de parámetros
    Post: Se retornan dos números enteros correspondientes al mes y el año que proporciona el usuario
    """
    while True:
        mes = int(input("Ingrese el mes: "))
        anio = int(input("Ingrese el año: "))

        if validar_fecha(mes, anio):
            break
        else:
            print("ERROR - La fecha que usted ingresó es inválida.")
    
    return mes, anio

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

def dia_semana(dia: int, mes: int, anio: int) -> int:
    """
    Calcula el día de la semana en el que cae la fecha ingresada como parámetros

    Pre: Los parámetros deben ser enteros positivos y representar una fecha válida
    Post: Se devuelve un número del 0 al 6, siendo el 0 domingo, 1 lunes, 2 martes, etc.
    """
    if mes < 3:
        mes += 10
        anio -= 1
    else:
        mes -= 2
    siglo = anio // 100
    anio2 = anio % 100

    dia_sem = (((26 * mes - 2) // 10) + dia + anio2 + (anio2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    if dia_sem < 0:
        dia_sem += 7
    
    return dia_sem

def cant_dias_mes(mes: int, anio: int) -> int:
    """
    Calcula la cantidad de días de un mes de un año cualquiera

    Pre: El mes y año deben ser válidos
    Post: Devuelve un entero correspondiente a la cantidad de días del mes
    """
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        cant_dias = 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        cant_dias = 30
    elif mes == 2 and es_bisiesto(anio):
        cant_dias = 29
    elif mes == 2 and es_bisiesto(anio) == False:
        cant_dias = 28
    
    return cant_dias

def impr_calendario(mes: int, anio: int) -> None:
    """
    Imprime el calendario del mes en el año ingresado, con sus correspondientes días de la semana

    Pre: El mes y el año deben ser válidos.
    Post: No retorna nada, sólo imprime el calendario del mes
    """
    cant_dias = cant_dias_mes(mes, anio) # La cantidad de días que debe imprimir la función
    dia_sem = dia_semana(1, mes, anio) # Sabiendo en que día de semana comienza el mes y el total de días que tiene, se pueden imprimir todos los demás
    dia_sem_str = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"] # Para mostrarlo en pantalla
    
    for dia in range(cant_dias):
        print(dia_sem_str[dia_sem], dia+1)
        dia_sem += 1

        if dia_sem > 6:
            dia_sem = 0
            print("------------")

def main():
    mes, anio = pedir_fecha()

    print(f"\nEl calendario del mes {mes} del año {anio} es el siguiente:\n")
    impr_calendario(mes, anio)

main()