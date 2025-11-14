def guardar_dato(dato: str, ruta: str) -> None:
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
    titulo_archivo = ruta_py.split("/")[-1][:-3] 
    ruta_nueva = "/".join((ruta_py.split("/")[:-1])) 
    ruta_nueva += f"/{titulo_archivo}_sin_comentarios.py" 

    try:
        with open(ruta_py, "rt", encoding="utf-8-sig") as archivo:
            es_comentario = False
            for linea in archivo:
                es_cadena = False

                if ('"""' in linea or "'''" in linea) and not ('"""' in linea and "'''" in linea): 
                    es_comentario = not es_comentario
                    continue
                
                if es_comentario:
                    continue

                for i, caracter in enumerate(linea):
                    if caracter == '"' or caracter == "'": 
                        es_cadena = not es_cadena
                    
                    if caracter == "#" and not es_cadena: 
                        indice_comentario = i
                        guardar_dato(f"{linea[:indice_comentario]}\n", ruta_nueva) 
                        break
                else:
                    guardar_dato(linea, ruta_nueva) 
            
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