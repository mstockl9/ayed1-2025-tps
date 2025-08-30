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
    
    elif (dia == 29 and mes == 2) and ((anio % 4 != 0) or (anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0)): # Valida si el año es bisiesto
        return False
    
    else:
        return True

def main():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    print()
    if validar_fecha(dia, mes, anio):
        print(f"La fecha {dia}/{mes}/{anio} es válida.")
    else:
        print(f"La fecha que usted ingresó no es válida.")

main()