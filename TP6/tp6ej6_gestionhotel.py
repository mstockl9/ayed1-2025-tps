import random as rnd

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


def calcular_entre_fechas(fecha1: tuple[int], fecha2: tuple[int]) -> int:
    """
    Devuelve la cantidad de días que existen entre fecha1 y fecha2

    Pre: Ingresan dos tuplas con fechas que deben ser validadas previamente, fecha1 debe ser anterior a fecha2
    Post: Devuelve un entero que corresponde a la cantidad de días entre una fecha y otra
    """
    total_dias = 0
    while fecha1 != fecha2: # Hasta que la primera fecha llegue a la segunda, se usa la función dia_siguiente()
        dia, mes, anio = fecha1[0], fecha1[1], fecha1[2]
        fecha1 = dia_siguiente(dia, mes, anio)

        total_dias += 1
    
    return total_dias


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


def formatear_fecha_v3(fecha: str) -> tuple[int]:
    """
    Convierte la fecha ingresada en formato DD/MM/AAAA en tres enteros correspondientes al día, mes y año.

    Pre: Recibe como parámetro un string correspondiente a la fecha en dicho formato.
    Post: Retorna una tupla con tres enteros correspondientes al día, mes y año.
    """
    dia, mes, anio = fecha[:2], fecha[2:4], fecha[4:]
    return int(dia), int(mes), int(anio)


def validar_fecha_formato(fecha_formato: str) -> bool:
    """
    Recibe una fecha (DDMMAAAA) y controla que sea una fecha válida.

    Pre: Recibe como parámetros la fecha en formato DDMMAAAA
    Post: Retorna True si la fecha es válida, si no retorna False.
    """
    dia, mes, anio = formatear_fecha_v3(fecha_formato)
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


def validar_piso_habitacion(ruta_pisos: str, piso: int, habitacion: int) -> bool:
    """
    Valida que el piso y la habitación ingresados no estén ya asignados a un huésped.

    Pre: Recibe como parámetros un string correspondiente a la ruta del archivo de pisos, y los enteros correspondientes al piso y a la habitación a validar.
    Post: Retorna True si no está repetido, si no retorna False.
    """
    separador = ","
    try:
        with open(ruta_pisos, "rt", encoding="utf-8-sig") as archivo:
            for linea in archivo:
                linea = linea.strip()
                lista_datos = linea.split(separador)

                piso_validar, habitacion_validar = lista_datos
                if int(piso_validar) == piso and int(habitacion_validar) == habitacion:
                    print(piso, habitacion)
                    print(9)
                    return False
            else:
                return True

    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')
    except Exception as msg:
        print(f'Error en los datos: {msg}')


def asignar_pisos(ruta_pisos: str) -> None:
    """
    Añade un nuevo piso y habitación, validando que no esté ya asignado.

    Pre: Recibe como parámetro un string correspondiente al archivo de pisos.
    Post: No retorna nada, sólo escribe el archivo asignando el número de piso y número de habitación respectivamente
    en otro archivo de pisos y habitaciones.
    """
    cant_pisos = 10
    cant_habitaciones = 6
    
    while True:
        piso_rnd = rnd.randint(1, cant_pisos)
        habitacion_rnd = rnd.randint(1, cant_habitaciones)
        if validar_piso_habitacion(ruta_pisos, piso_rnd, habitacion_rnd):
            break
    
    guardar_dato(f"{piso_rnd},{habitacion_rnd}\n", ruta_pisos)
  

def registrar_ingreso(ruta_hotel: str, ruta_pisos: str) -> str:
    """
    Pide la información de huéspedes (DNI, nombre y apellido, fecha de ingreso y egreso y cantidad de ocupantes)
    y la graba en un archivo formato CSV.

    Pre: Recibe como parámetro dos strings correspondientes a la ruta del archivo con la información de los huéspedes del hotel y la ruta de pisos y habitaciones.
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
            asignar_pisos(ruta_pisos)
            nro_huesped += 1
            print()


def calcular_mayor_habitaciones(ruta_pisos: str) -> None:
    """
    Muestra el piso con mayor cantidad de habitaciones ocupadas.

    Pre: Recibe como parámetro un string correspondiente a la ruta del archivo de pisos y habitaciones.
    Post: No retorna nada, sólo muestra por pantalla el piso con más habitaciones ocupadas.
    """
    separador = ","
    pisos_y_cantidades = {str(piso): 0 for piso in range(1, 10+1)}
    try:
        with open(ruta_pisos, "rt", encoding="utf-8-sig") as archivo:
            for linea in archivo:
                linea = linea.strip()
                lista_datos = linea.split(separador)
                piso = lista_datos[0]

                pisos_y_cantidades[piso] += 1
            
            piso_mas_habitaciones = max([(cant_habitaciones, piso) for piso, cant_habitaciones in pisos_y_cantidades.items()])[1]
            print(f"El piso con mayor cantidad de habitaciones ocupadas es el piso {piso_mas_habitaciones}")
            input("Presione Enter para continuar...")

    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')
    except Exception as msg:
        print(f'Error en los datos: {msg}')


def calcular_habitaciones_vacias(ruta_pisos: str) -> None:
    """
    Muestra cuántas habitaciones vacías hay en todo el hotel.

    Pre: Recibe como parámetro un string correspondiente al archivo de pisos y habitaciones.
    Post: No retorna nada, muestra por pantalla la cantidad de habitaciones vacías en el hotel.
    """
    total_habitaciones = 6*10
    cant_ocupadas = 0
    try:
        with open(ruta_pisos, "rt", encoding="utf-8-sig") as archivo:
            for _ in archivo:
                cant_ocupadas += 1
            
            cant_habitaciones_vacias = total_habitaciones - cant_ocupadas
            print(f"En el hotel hay actualmente {cant_habitaciones_vacias} habitaciones vacías.")
            input("Presione Enter para continuar...")

    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')
    except Exception as msg:
        print(f'Error en los datos: {msg}')


def calcular_mayor_personas(ruta_hotel: str, ruta_pisos: str) -> None:
    """
    Muestra cuál es el piso con mayor cantidad de personas en total.

    Pre: Recibe como parámetro dos strings correspondientes a la ruta del archivo de huéspedes y de pisos.
    Post: No retorna nada, muestra el piso con más personas en total.
    """
    separador = ","
    pisos_personas = {str(piso): 0 for piso in range(1, 10+1)}
    try:
        with open(ruta_hotel, "rt", encoding="utf-8-sig") as archivo_hotel, open(ruta_pisos, "rt", encoding="utf-8-sig") as archivo_pisos:
            for huesped, piso_habitacion in zip(archivo_hotel, archivo_pisos):
                huesped, piso_habitacion = huesped.strip(), piso_habitacion.strip()
                cant_personas = huesped.split(separador)[-1]
                piso = piso_habitacion.split(separador)[0]

                pisos_personas[piso] += int(cant_personas)
            
            piso_mas_personas = max([(cant_personas, piso) for piso, cant_personas in pisos_personas.items()])[1]
            print(f"El piso con mayor cantidad de personas es el piso {piso_mas_personas}")
            input("Presione Enter para continuar...")

    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')
    except Exception as msg:
        print(f'Error en los datos: {msg}')


def formatear_fecha_v2(fecha: str) -> str:
    """
    Convierte la fecha ingresada a formato año, mes, día.

    Pre: Recibe como parámetros un string correspondiente a una fecha formateada en DD/MM/AAAA.
    Post: Retorna un string correspondiente a la fecha formateada.
    """
    dia, mes, anio = fecha[:2], fecha[2:4], fecha[4:]
    fecha_formato = f"{anio}{mes}{dia}"

    return fecha_formato


def proxima_en_desocuparse(ruta_hotel: str, ruta_pisos) -> None:
    """
    Muestra cuál o cuáles (en caso de ser la misma fecha) serán las próximas habitaciones en desocuparse.

    Pre: Recibe como parámetros un string correspondiente al archivo de huéspedes.
    Post: No retorna nada, muestra las próximas habitaciones en desocuparse.
    """
    while True:
        dia_actual = pedir_entero("el día actual", 1, 31)
        mes_actual = pedir_entero("el mes actual", 1, 12)
        anio_actual = pedir_entero("el año actual", 1000, 9999)

        if validar_fecha(dia_actual, mes_actual, anio_actual):
            break
    fecha_actual = formatear_fecha(str(dia_actual), str(mes_actual), str(anio_actual))
    fecha_actual = formatear_fecha_v2(fecha_actual)

    lista_fechas_y_piso = []
    separador = ","
    try:
        with open(ruta_hotel, "rt", encoding="utf-8-sig") as archivo_hotel, open(ruta_pisos, "rt", encoding="utf-8-sig") as archivo_pisos:
            for huesped, piso_habitacion in zip(archivo_hotel, archivo_pisos):
                huesped, piso_habitacion = huesped.strip(), piso_habitacion.strip()
                fecha_egreso = huesped.split(separador)[-2]
                fecha_egreso = formatear_fecha_v2(fecha_egreso)
                piso_habitacion = tuple(piso_habitacion.split(separador))

                if fecha_egreso >= fecha_actual:
                    lista_fechas_y_piso.append((fecha_egreso, piso_habitacion))
            
            lista_fechas_y_piso = sorted(lista_fechas_y_piso)
            solo_fechas = [habitacion[0] for habitacion in lista_fechas_y_piso]
            cant_proximas = solo_fechas.count(solo_fechas[0])
            habitaciones_proximas = lista_fechas_y_piso[0] if cant_proximas == 1 else lista_fechas_y_piso[:cant_proximas]

            print()
            if isinstance(habitaciones_proximas, tuple):
                piso, habitacion = habitaciones_proximas[1]
                print(f"La proxima habitación en desocuparse será la habitación {habitacion} del piso {piso}")
            else:
                print("Las próximas habitaciones a desocuparse son las siguientes:")
                for dato in habitaciones_proximas:
                    piso, habitacion = dato[1]
                    print(f"Piso {piso}, Habitación {habitacion}")
            input("Presione Enter para continuar...")

    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')
    except Exception as msg:
        print(f'Error en los datos: {msg}')


def ordenar_dias_alojamiento(ruta_hotel: str) -> None:
    """
    Muestra un listado de todos los huéspedes ordenados por cantidad de días de alojamiento.

    Pre: Recibe como parámetro un string correspondiente a la ruta del archivo de huéspedes.
    Post: No retorna nada, muestra el listado ordenado.
    """
    separador = ","
    huespedes_alojamiento = []
    try:
        with open(ruta_hotel, "rt", encoding="utf-8-sig") as archivo_hotel:
            for huesped in archivo_hotel:
                huesped = huesped.strip()
                datos_huesped = huesped.split(separador)

                nombre_huesped = datos_huesped[1]
                fecha_ingreso, fecha_egreso = datos_huesped[-3], datos_huesped[-2]

                fecha_ingreso = formatear_fecha_v3(fecha_ingreso)
                fecha_egreso = formatear_fecha_v3(fecha_egreso)

                cant_alojamiento = calcular_entre_fechas(fecha_ingreso, fecha_egreso)
                huespedes_alojamiento.append((cant_alojamiento, nombre_huesped))
            
            alojamiento_ordenados = sorted(huespedes_alojamiento)
            print("La lista de huéspedes ordenados por días de alojamiento de menor a mayor es la siguiente:")
            for cant_dias, nombre in alojamiento_ordenados:
                print(f"{nombre}: {cant_dias} días")
            input("Presione Enter para continuar...")

    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')
    except Exception as msg:
        print(f'Error en los datos: {msg}')


def inicializar_archivo(ruta_hotel: str, ruta_pisos: str) -> None:
    """
    Crea los archivos vacío en caso de no existir.

    Pre: Recibe como parámetros dos strings correspondientes a la ruta del archivo de huéspedes y de pisos.
    Post: No retorna nada, crea los archivos si no existe.
    """
    try:
        archivo_hotel = open(ruta_hotel, "at")
        archivo_pisos = open(ruta_pisos, "at")
        archivo_hotel.close()
        archivo_pisos.close()
    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede grabar el archivo: {msg}')
    except Exception as msg:
        print(f'Error en los datos: {msg}')


def validar_hay_datos(ruta_hotel: str) -> bool:
    """
    Comprueba si hay algún dato en el archivo de huéspedes.

    Pre: Recibe como parámetros un string correspondiente a la ruta del archivo de huéspedes.
    Post: Retorna True si hay datos, False si no.
    """
    try:
        with open(ruta_hotel, "rt", encoding="utf-8-sig") as archivo_hotel:
            linea = archivo_hotel.readline()
            return bool(linea)
                    
    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')
    except Exception as msg:
        print(f'Error en los datos: {msg}')


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
    ruta_pisos = "AyED1-2025-TPs/TP6/archivos/ej6/info_pisos.txt"
    inicializar_archivo(ruta_hotel, ruta_pisos)
    
    opciones_hotel = (
        "Salir del programa",
        "Registrar ingresos", 
        "Mostrar el piso con más habitaciones ocupadas", 
        "Mostrar cantidad de habitaciones vacías",
        "Mostrar el piso con más personas", 
        "Mostrar cuál será la próxima habitación en desocuparse", 
        "Listar los huéspedes por cantidad de días de alojamiento"
        )
    
    while True:
        hay_datos = validar_hay_datos(ruta_hotel)
        opciones(opciones_hotel)
        op = input("Ingrese una de las opciones disponibles: ")

        print()
        if op == "1":
            registrar_ingreso(ruta_hotel, ruta_pisos)
        elif op != "1" and hay_datos:
            if op == "2":
                calcular_mayor_habitaciones(ruta_pisos)
            elif op == "3":
                calcular_habitaciones_vacias(ruta_pisos)
            elif op == "4":
                calcular_mayor_personas(ruta_hotel, ruta_pisos)
            elif op == "5":
                proxima_en_desocuparse(ruta_hotel, ruta_pisos)
            elif op == "6":
                ordenar_dias_alojamiento(ruta_hotel)
            elif op == "0":
                print("El programa ha finalizado.")
                break
            else:
                print("ERROR - Opción inválida")
                input("Presione Enter para continuar...")
        else:
            print("ERROR - No hay datos cargados aún.")
            input("Presione Enter para continuar...")
        print()
   
menu()