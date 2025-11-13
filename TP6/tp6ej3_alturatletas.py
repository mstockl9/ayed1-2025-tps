def guardar_dato(dato: str, ruta: str) -> None:
    """
    Añade el dato recibido en la ruta de archivo que ingresa.

    Pre: Recibe como parámetros, el dato a guardar y un string correspondiente a la ruta del archivo.
    Post: No retorna nada, añade el dato al archivo correspondiente.
    """
    try:
        with open(ruta, "at", encoding="utf-8-sig") as archivo_mandar:
            archivo_mandar.write(dato)
    
    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede grabar el archivo: {msg}')
    except Exception as e:
        print(f'Error en los datos: {e}')

def pedir_altura(num: int) -> float:
    """
    Pide al usuario un flotante que corresponde a la altura del atleta en metros y valida que sea un número mayor a 0.

    Pre: Recibe como parámetro la altura del atleta a ingresar.
    Post: Retorna el flotante que ingresó el usuario, validado previamente.
    """
    while True:
        altura = input(f"Ingrese la altura del atleta N°{num} en metros (-1 para salir): ")
        try:
            altura = float(altura)
        except ValueError:
            print("ERROR - La altura debe ser un número.")
        else:
            if altura > 0 or altura == -1.0:
                return altura
            else:
                print("ERROR - La altura debe ser mayor a 0.")

def grabar_promedio(ruta_alturas: str, ruta_promedios: str) -> None:
    """
    Graba en un archivo el promedio de alturas de todos los atletas de cada deporte

    Pre: Recibe como parámetro dos strings correspondientes a la ruta del archivo que contiene las alturas y la ruta del archivo
    donde deben guardarse los promedios.
    Post: No retorna nada, sólo graba los promedios en el archivo.
    """
    cant_atletas = 0
    suma_alturas = 0
    try:
        with open(ruta_alturas, "rt", encoding="utf-8-sig") as archivo:
            while True:
                linea = archivo.readline().strip()

                if not linea or linea.isalpha():
                    if cant_atletas:
                        promedio_altura = suma_alturas / cant_atletas
                        cant_atletas = 0
                        suma_alturas = 0
                        guardar_dato(f"{promedio_altura}\n", ruta_promedios)
                    
                    if linea:
                        guardar_dato(f"{linea}\n", ruta_promedios)
                    else:
                        break
                else:
                    cant_atletas += 1
                    suma_alturas += float(linea)
    
    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')
    else:
        print("Promedios grabados correctamente.")

def calcular_promedio_alturas(ruta_alturas: str) -> float:
    """
    Calcula el promedio general de altura de los atletas de todas las disciplinas.

    Pre: Recibe como parámetro la ruta del archivo con los datos de todos los atletas.
    Post: Retorna un flotante correspondiente al promedio general de alturas.
    """
    cant_atletas = 0
    suma_alturas = 0
    try:
        with open(ruta_alturas, "rt", encoding="utf-8-sig") as archivo:
            while True:
                linea = archivo.readline().strip()

                if not linea:
                    promedio_general = suma_alturas / cant_atletas
                    return promedio_general

                if not linea.isalpha():
                    cant_atletas += 1
                    suma_alturas += float(linea)
    
    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')

def mostrar_mas_altos(ruta_promedios: str, promedio_general: float) -> None:
    """
    Muestra por pantalla los deportes cuyos atletas superan el promedio general en altura.

    Pre: Recibe como parámetros la ruta del archivo con los promedios de cada deporte y un flotante correspondiente al promedio general.
    Post: No retorna nada, muestra por pantalla los datos descriptos.
    """
    try:
        with open(ruta_promedios, "rt", encoding="utf-8-sig") as archivo:
            while True:
                linea = archivo.readline().strip()
                if not linea:
                    break

                if linea.isalpha():
                    deporte = linea
                elif not linea.isalpha() and float(linea) > promedio_general:
                    print(f"{deporte}: {linea}")

    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')

def grabar_rango_alturas(ruta_alturas: str) -> None:
    """
    Pide información de una disciplina y la altura de cada atleta de dicha disciplina. Luego graba
    esos datos en un archivo.

    Pre: Recibe como parámetros la ruta a guardar las alturas
    Post: No retorna nada, pide los datos y los guarda en un archivo.
    """
    while True:
        deporte = input("\nIngrese un deporte (-1 para salir): ")
        if deporte == "-1":
            print("Datos guardados correctamente.")
            break
        else:
            guardar_dato(f"{deporte.title()}\n", ruta_alturas)
            print(f"\n---{deporte.upper()}---")
            
            num_atleta = 1
            while True:
                altura = pedir_altura(num_atleta)

                if altura == -1.0:
                    break

                guardar_dato(f"{altura}\n", ruta_alturas)
                num_atleta += 1

def main():
    ruta_alturas = "AyED1-2025-TPs/TP6/archivos/ej3/altura_atletas.txt"
    ruta_promedios = "AyED1-2025-TPs/TP6/archivos/ej3/altura_promedio.txt"
    grabar_rango_alturas(ruta_alturas)
    grabar_promedio(ruta_alturas, ruta_promedios)

    promedio_general = calcular_promedio_alturas(ruta_alturas)
    print(f"\nDeportes cuyos atletas superan el promedio general ({promedio_general:.2f}):")
    mostrar_mas_altos(ruta_promedios, promedio_general)

main()