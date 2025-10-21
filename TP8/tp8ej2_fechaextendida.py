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


def fecha_extendida(dia: int, mes: int, anio: int) -> str:
    """
    Transforma la fecha recibida en formato extendido "<Día> de <Mes> de <Año>". Si el año se ingresa en
    dos dígitos y el mismo es mayor a 30, se expresa como el siglo pasado (1900).

    Pre: Recibe como parámetros tres enteros correspondientes al día, el mes y el año.
    Post: Retorna una cadena de caracteres correspondiente a la fecha ingresada en formato extendido. Si la fecha es inválida, retorna un string vacío.
    """
    meses_str = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    dia_str, anio_str = str(dia), str(anio)
    try:
        mes_str = meses_str[mes-1]
    except IndexError:
        return ""
    
    cant_digitos_anio = len(anio_str)
    if cant_digitos_anio <= 2 and anio > 30:
        anio_str = "19" + "0" * (2 - cant_digitos_anio) + anio_str
    elif cant_digitos_anio <= 2 and anio <= 30:
        anio_str = "20" + "0" * (2 - cant_digitos_anio) + anio_str
    
    if validar_fecha(dia, mes, int(anio_str)):
        fecha_extendida = dia_str + " de " + mes_str + " de " + anio_str
        return fecha_extendida
    else:
        return ""


def main():
    dia = pedir_entero("el día")
    mes = pedir_entero("el mes")
    anio = pedir_entero("el año")

    fecha_ext = fecha_extendida(dia, mes, anio)
    print()
    if fecha_ext:
        print(f"La fecha que usted ingresó en formato extendido es la siguiente: {fecha_ext}")
    else:
        print("La fecha que usted ingresó es inválida.")

main()