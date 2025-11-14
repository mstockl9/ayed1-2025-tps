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

def transformar_formato1(ruta_archivo: str) -> str:
    """
    Transforma el archivo recibido en formato de campos con longitud fija en otro archivo formato CSV.

    Pre: Recibe como parámetro la ruta del archivo con dicho formato.
    Post: Crea un archivo en formato CSV con los datos del archivo recibido. Retorna la ruta de dicho archivo.
    """
    separador = ","
    titulo_archivo = ruta_archivo.split("/")[-1][:-4]
    ruta_csv = "/".join((ruta_archivo.split("/")[:-1]))
    ruta_csv += f"/{titulo_archivo}_csv.txt"

    try:
        with open(ruta_archivo, "rt", encoding="utf-8-sig") as archivo:
            longitud_campos = (17, 25, 63) # Estas serían las longitudes fijas según los ejemplos
            for linea in archivo:
                lista_datos = []
                principio = 0
                for longitud in longitud_campos:
                    lista_datos.append(linea[principio:longitud].strip())
                    principio = longitud
                
                linea = separador.join(lista_datos)
                guardar_dato(f"{linea}\n", ruta_csv)
            
            return ruta_csv

    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')
    except Exception as msg:
        print(f'Error en los datos: {msg}')
    else:
        print("Datos guardados correctamente.")

def transformar_formato2(ruta_archivo: str) -> str:
    """
    Transforma el archivo recibido en formato de campos precedidos por un número de dos dígitos que indica la
    longitud del campo que sigue a un archivo en formato CSV.

    Pre: Recibe como parámetro la ruta del archivo con dicho formato.
    Post: Crea un archivo en formato CSV con los datos del archivo recibido. Retorna la ruta de dicho archivo.
    """
    separador = ","
    titulo_archivo = ruta_archivo.split("/")[-1][:-4]
    ruta_csv = "/".join((ruta_archivo.split("/")[:-1]))
    ruta_csv += f"/{titulo_archivo}_csv.txt"

    try:
        with open(ruta_archivo, "rt", encoding="utf-8-sig") as archivo:
            for linea in archivo:
                lista_datos = []
                principio = 0
                while True:
                    longitud = linea[principio:principio+2]
                    if longitud.isdigit():
                        longitud = int(longitud)
                    else:
                        break
                    lista_datos.append(linea[principio+2:principio+2+longitud])

                    principio = principio+2+longitud
                
                linea = separador.join(lista_datos)
                guardar_dato(f"{linea}\n", ruta_csv)
            
            return ruta_csv
        
    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')
    except Exception as msg:
        print(f'Error en los datos: {msg}')

def main():
    ruta_formato1 = "AyED1-2025-TPs/TP6/archivos/ej5/formato1.txt"
    ruta_formato2 = "AyED1-2025-TPs/TP6/archivos/ej5/formato2.txt"
    ruta_csv1 = transformar_formato1(ruta_formato1)
    ruta_csv2 = transformar_formato2(ruta_formato2)
    
    print(f"El archivo formato CSV del formato 1 fue generado con éxito en {ruta_csv1}")
    print(f"El archivo formato CSV del formato 2 fue generado con éxito en {ruta_csv2}")

main()