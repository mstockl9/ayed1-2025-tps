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
    contador_caract = 0
    num_archivo = 1
    ruta_a_mandar = f"AyED1-2025-TPs/TP6/archivos/ej2/{titulo_archivo}{str(num_archivo)}.txt"
    try:
        with open(archivo_ruta, 'rt', encoding='utf-8-sig') as archivo:
            for linea in archivo:
                for caracter in linea:
                    contador_caract += 1
                    if contador_caract >= max_caract:
                        contador_caract = 0
                        num_archivo += 1
                        ruta_a_mandar = f"AyED1-2025-TPs/TP6/archivos/ej2/{titulo_archivo}{str(num_archivo)}.txt"

                    guardar_texto(caracter, ruta_a_mandar)

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
    dividir_archivo(ruta_archivo, 200)

main()