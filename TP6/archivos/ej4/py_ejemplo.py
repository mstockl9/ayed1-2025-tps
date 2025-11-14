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

def eliminar_comentarios(ruta_py: str) -> str:
    """
    Genera una copia sin los comentarios (# y doc string) del archivo python ingresado.

    Pre: Recibe como parámetro la ruta de un archivo .py
    Post: Crea un nuevo archivo en la misma carpeta sin comentarios y retorna un string correspondiente a
    la ruta de dicho archivo.
    """
    titulo_archivo = ruta_py.split("/")[-1][:-3] # Separa la ruta en "/" y agarra el último elemento correspondiente al nombre del archivo, hasta el .py
    ruta_nueva = "/".join((ruta_py.split("/")[:-1])) # Junta todo nuevamente con "/" pero sin el título
    ruta_nueva += f"/{titulo_archivo}_sin_comentarios.py" # Le añade a la ruta el nuevo título

    try:
        with open(ruta_py, "rt", encoding="utf-8-sig") as archivo:
            es_comentario = False
            for linea in archivo:
                es_cadena = False

                if ('"""' in linea or "'''" in linea) and not ('"""' in linea and "'''" in linea): # Si es un doc string va a ser un comentario hasta la próxima vez que se encuentren triple comillas
                    es_comentario = not es_comentario
                    continue
                
                if es_comentario:
                    continue

                for i, caracter in enumerate(linea):
                    if caracter == '"' or caracter == "'": # Si encuentra comillas lo siguiente es una cadena hasta las próximas comillas
                        es_cadena = not es_cadena
                    
                    if caracter == "#" and not es_cadena: # Se asegura que el # no esté dentro de una cadena
                        indice_comentario = i
                        guardar_dato(f"{linea[:indice_comentario]}\n", ruta_nueva) # Se guarda toda la línea excepto el # y todo lo que sigue
                        break
                else:
                    guardar_dato(linea, ruta_nueva) # Si no encuentra ningún comentario guarda la línea como está
            
            return ruta_nueva
    
    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')
    except:
        print('Error en los datos')

def main():
    ruta_py = "AyED1-2025-TPs/TP6/archivos/ej4/py_ejemplo.py"
    py_sin_comentarios = eliminar_comentarios(ruta_py)
    print(f"Comentarios eliminados correctamente en {py_sin_comentarios}")

main()