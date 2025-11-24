import random as rnd

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

def validar_fecha_egreso(fecha_ingreso: str, fecha_egreso: str) -> bool:
    """
    Valida que la fecha de egreso sea mayor a la fecha de ingreso.

    Pre: Recibe como parámetros dos strings correspondientes a la fecha de ingreso y egreso, ambas en formato DDMMAAAA.
    Post: Retorna True si la fecha de egreso es mayor a la de ingreso, si no retorna False.
    """
    dia_i, mes_i, anio_i = int(fecha_ingreso[:2]), int(fecha_ingreso[2:4]), int(fecha_ingreso[4:])
    dia_e, mes_e, anio_e = int(fecha_egreso[:2]), int(fecha_egreso[2:4]), int(fecha_egreso[4:])

    return anio_e > anio_i or (anio_e == anio_i and ((mes_e > mes_i) or (mes_e <= mes_i and dia_e > dia_i)))

def pedir_entero(a_pedir: str, minimo: int, maximo: int) -> int:
    """
    Pide un entero al usuario y valida que sea un número y que se encuentre dentro del rango especificado.

    Pre: Recibe como parámetro un string correspondiente al nombre del entero a pedir, y dos enteros que indican el mínimo y máximo aceptados.
    Post: Retorna el entero validado previamente.
    """
    while True:
        entero = input(f"Ingrese {a_pedir.lower()}: ")
        try:
            entero = int(entero)
        except ValueError:
            print(f"ERROR - {a_pedir.capitalize()} debe ser un número entero.")
        else:
            if (entero >= minimo and entero <= maximo) or entero == -1:
                return entero
            else:
                print("ERROR - Rango inválido.")

def formatear_fecha(dia: str, mes: str, anio: str) -> str:
    """
    Convierte la fecha ingresada a formato DDMMAAAA
    
    Pre: Recibe como parámetros tres strings correspondientes a día, mes y año.
    Post: Retorna un string correspondiente a la fecha formateada.
    """
    return "0"*(2-len(dia)) + dia + "0"*(2-len(mes)) + mes + anio

def validar_fecha_formato(fecha_formato: str) -> bool:
    """
    Recibe una fecha (DDMMAAAA) y controla que sea una fecha válida.

    Pre: Recibe como parámetros la fecha en formato DDMMAAAA
    Post: Retorna True si la fecha es válida, si no retorna False.
    """
    dia, mes, anio = int(fecha_formato[:2]), int(fecha_formato[2:4]), int(fecha_formato[4:])
    return validar_fecha(dia, mes, anio)

def validar_dni(dni: str, ruta_hotel: str) -> bool:
    """
    Recibe un DNI y valida que no esté repetido en el registro de huéspedes.

    Pre: Recibe como parámetro un string correspondiente a la ruta del archivo de huéspedes
    y otro string correspondiente al DNI a validar.
    Post: Retorna True si el DNI no está repetido, y False si lo está.
    """
    separador = ","
    if dni == "-1":
        return dni
    try:
        with open(ruta_hotel, "rt", encoding="utf-8-sig") as archivo:
            for linea in archivo:
                lista_datos = linea.split(separador)
                dni_validar = lista_datos[0]
                if dni_validar == dni:
                    return False
            
            else:
                return True
                

    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')
    except Exception as msg:
        print(f'Error en los datos: {msg}')

def guardar_dato(dato: str, ruta: str) -> None:
    """
    Añade el dato recibido en la ruta de archivo que ingresa.

    Pre: Recibe como parámetros, el dato a guardar y un string correspondiente a la ruta del archivo.
    Post: No retorna nada, añade el dato al archivo correspondiente.
    """
    try:
        with open(ruta, "at", encoding="utf-8") as archivo_mandar:
            archivo_mandar.write(dato)
    
    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede grabar el archivo: {msg}')
    except Exception as msg:
        print(f'Error en los datos: {msg}')

def validar_piso_habitacion(ruta_hotel: str, piso: int, habitacion: int) -> bool:
    """
    Valida que el piso y la habitación ingresados no estén ya asignados a un huésped.

    Pre: Recibe como parámetros un string correspondiente a la ruta del archivo de huéspedes, y los enteros correspondientes al piso y a la habitación a validar.
    Post: Retorna True si no está repetido, si no retorna False.
    """
    try:
        with open(ruta_hotel, "rt", encoding="utf-8-sig") as archivo:
            for linea in archivo:
                lista_datos = linea.split(",")
                piso_validar, habitacion_validar = lista_datos[-2], lista_datos[-1]

                if piso_validar == piso or habitacion_validar == habitacion:
                    return False
            else:
                return True

    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')
    except Exception as msg:
        print(f'Error en los datos: {msg}')

def asignar_pisos(ruta_hotel: str) -> None:
    """
    Asigna un piso y habitación a los huéspedes del archivo de huéspedes que no tengan uno asignado, validando que no
    esté ya asignado.

    Pre: Recibe como parámetro un string correspondiente a la ruta del archivo de huéspedes.
    Post: No retorna nada, sólo escribe el archivo asignando el número de piso y número de habitación respectivamente
    en otro archivo de pisos y habitaciones.
    """
    separador = ","
    ruta_pisos = "AyED1-2025-TPs/TP6/archivos/ej6/info_pisos.txt"
    cant_pisos = 10
    cant_habitaciones = 6
    try:
        with open(ruta_hotel, "rt", encoding="utf-8-sig") as archivo_hotel, open(ruta_pisos, "wt", encoding="utf-8") as archivo_pisos:
            for linea in archivo_hotel:
                lista_datos = linea.split(separador)
                if len(lista_datos) <= 5:
                    while True:
                        piso_rnd = rnd.randint(1, cant_pisos)
                        habitacion_rnd = rnd.randint(1, cant_habitaciones)
                        if validar_piso_habitacion(ruta_hotel, piso_rnd, habitacion_rnd):
                            break
                    
                    guardar_dato(f"{piso_rnd},{habitacion_rnd}\n", ruta_pisos)
                    
    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')
    except Exception as msg:
        print(f'Error en los datos: {msg}')


def registrar_ingreso(ruta_hotel: str) -> str:
    """
    Pide la información de huéspedes (DNI, nombre y apellido, fecha de ingreso y egreso y cantidad de ocupantes)
    y la graba en un archivo formato CSV.

    Pre: Recibe como parámetro un string correspondiente a la ruta del archivo con la información de los huéspedes del hotel.
    Post: Graba la información en un archivo formato CSV, retorna la ruta de dicho archivo.
    """
    separador = ","
    nro_huesped = 1
    while True:
        print(f"-------------------Huésped N°{nro_huesped}-------------------")

        # Carga y validación de DNI
        print("---DNI---")
        while True:
            dni = str(pedir_entero("el DNI del cliente", 10000000, 99999999))
            if not validar_dni(dni, ruta_hotel):
                print("ERROR - El DNI que usted ingresó ya se encuentra en el sistema.")
            else:
                break
        
        if dni == "-1":
            break

        # Carga de Nombre y Apellido
        print("\n---Nombre y Apellido---")
        nombre_apellido = input("Ingrese el nombre y apellido del huésped: ")

        # Carga y validación de Fecha de Ingreso y Egreso
        while True:
            while True:
                print("\n---Fecha de Ingreso---")
                dia_ingreso = str(pedir_entero("el día de ingreso", 1, 31))
                mes_ingreso = str(pedir_entero("el mes de ingreso", 1, 12))
                anio_ingreso = str(pedir_entero("el año de ingreso", 1000, 9999))

                ingreso_formateado = formatear_fecha(dia_ingreso, mes_ingreso, anio_ingreso)
                if validar_fecha_formato(ingreso_formateado):
                    break
                else:
                    print("ERROR - La fecha que usted ingresó es inválida.")

            while True:
                print("\n---Fecha de Egreso---")
                dia_egreso = str(pedir_entero("el día de egreso", 1, 31))
                mes_egreso = str(pedir_entero("el mes de egreso", 1, 12))
                anio_egreso = str(pedir_entero("el año de egreso", 1000, 9999))

                egreso_formateado = formatear_fecha(dia_egreso, mes_egreso, anio_egreso)
                if validar_fecha_formato(egreso_formateado):
                    break
                else:
                    print("ERROR - La fecha que usted ingresó es inválida.")
            
            if validar_fecha_egreso(ingreso_formateado, egreso_formateado):
                break
            else:
                print("ERROR - La fecha de ingreso no puede ser mayor a la fecha de egreso.")
        
        # Carga de Cantidad de Ocupantes
        print("\n---Cantidad de Ocupantes---")
        cant_ocupantes = str(pedir_entero("la cantidad de ocupantes", 1, 5))

        if dni != "-1":
            lista_datos = [dni, nombre_apellido, ingreso_formateado, egreso_formateado, cant_ocupantes]
            linea_datos = separador.join(lista_datos)
            guardar_dato(f"{linea_datos}\n", ruta_hotel)
            asignar_pisos(ruta_hotel)
            nro_huesped += 1
            print()

def opciones(tupla_opciones: tuple[str]) -> None:
    """
    Muestra y enumera el listado de las opciones disponibles.

    Pre: Recibe como parámetro una tupla con strings correspondientes a las opciones disponibles. La primera opción debe ser la de 'Salir del programa'.
    Post: No retorna nada, sólo imprime el listado de opciones.
    """
    print("Las opciones disponibles son las siguientes:")
    for i, op in enumerate(tupla_opciones):
        print(f"{i}- {op}")

def menu():
    ruta_hotel = "AyED1-2025-TPs/TP6/archivos/ej6/info_huespedes.txt"
    opciones_hotel = (
        "Salir del Programa",
        "Registrar Ingresos", 
        "Mostrar el piso con más habitaciones ocupadas", 
        "Mostrar cantidad de habitaciones vacías",
        "Mostrar el piso con más personas", 
        "Mostrar cuál será la próxima habitación en desocuparse", 
        "Listar los huéspedes por cantidad de días de alojamiento"
        )
    
    while True:
        opciones(opciones_hotel)
        op = input("Ingrese una de las opciones disponibles: ")

        print()
        if op == "1":
            registrar_ingreso(ruta_hotel)
        elif op == "2":
            pass
        elif op == "3":
            pass
        elif op == "4":
            pass
        elif op == "5":
            pass
        elif op == "6":
            pass
        elif op == "0":
            print("El programa ha finalizado.")
            break
        else:
            print("ERROR - Opción inválida")
            input("Presione Enter para continuar...")
        print()
        
menu()