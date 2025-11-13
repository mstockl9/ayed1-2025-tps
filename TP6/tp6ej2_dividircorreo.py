def guardar_texto(texto: str, ruta: str) -> None:
    """
    Añade el texto recibido en la ruta de archivo que ingresa.

    Pre: Recibe como parámetros dos strings correspondientes al texto y a la ruta del archivo.
    Post: No retorna nada, añade el texto al archivo correspondiente.
    """
    try:
        with open(ruta, "at", encoding="utf-8-sig") as archivo_mandar:
            archivo_mandar.write(texto)
    
    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede grabar el archivo: {msg}')
    except:
        print('Error en los datos')

def dividir_archivo(archivo_ruta: str, max_caract: int) -> None:
    """
    Divide el archivo de texto ingresado en varios archivos (archivo1, archivo2...) con un tamaño máximo de carácteres
    que debe ser ingresado.

    Pre: Recibe como parámetros una cadena correspondiente a la ruta del archivo completo y un entero correspondiente 
    al máximo de carácteres por archivo.
    Post: No retorna nada, genera varios archivos con el texto del archivo original, pero con un máximo de n caracteres.
    """
    titulo_archivo = archivo_ruta.split("/")[-1][:-4]
    cant_caract = 0
    num_archivo = 1
    try:
        with open(archivo_ruta, 'rt', encoding='utf-8-sig') as archivo:
            while True:
                linea = archivo.readline()
                if cant_caract:
                    a_mandar = linea[:max_caract-cant_caract+1]
                    guardar_texto(a_mandar, ruta_a_mandar)
                    num_archivo += 1

                    linea = linea[max_caract-cant_caract+1:]
                
                cant_caract += len(linea)
                ruta_a_mandar = f"AyED1-2025-TPs/TP6/archivos/ej2/{titulo_archivo}{str(num_archivo)}.txt"

                division, resto = divmod(len(linea), max_caract)
                for i in range(division):
                    a_mandar = linea[max_caract*i:max_caract*(i+1)]
                    guardar_texto(a_mandar, ruta_a_mandar)
                    num_archivo += 1
                    ruta_a_mandar = f"AyED1-2025-TPs/TP6/archivos/ej2/{titulo_archivo}{str(num_archivo)}.txt"
                
                if resto:
                    a_mandar = linea[-resto:]
                    guardar_texto(a_mandar, ruta_a_mandar)
                    cant_caract = len(a_mandar)
                else:
                    cant_caract = 0
                                
                if not linea:
                    break
    
    except FileNotFoundError as msg:
        print(f"No se encuentra el archivo: {msg}")
    except OSError as msg:
        print(f"No se puede leer el archivo: {msg}")
    except Exception as msg:
        print(f"Error en los datos: {msg}")
    else:
        print("Los archivos se crearon correctamente.")

def main():
    ruta_archivo = "AyED1-2025-TPs/TP6/archivos/ej2/consigna.txt"
    dividir_archivo(ruta_archivo, 60)

main()