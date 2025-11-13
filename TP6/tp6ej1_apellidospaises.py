def guardar_nombre_apellido(apellido: str, nombre: str, ruta: str) -> None:
    """
    Añade el nombre y el apellido en formato 'Apellido, Nombre' en la ruta ingresada.

    Pre: Recibe como parámetros dos cadenas correspondientes al nombre y el apellido de la persona, junto con una cadena correspondiente a la ruta.
    Post: No retorna nada, sólo añade el nombre y apellido a la ruta.
    """
    try:
        with open(ruta, "at", encoding="utf-8-sig") as archivo_mandar:
            archivo_mandar.write(f"{apellido}, {nombre}\n".title())
    
    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede grabar el archivo: {msg}')
    except:
        print('Error en los datos')

def main():
    separador = ", "
    diccionario_apellidos = {"ian": "ARMENIA", "ini": "ITALIA", "ez": "ESPAÑA"}
    
    try:
        with open("AyED1-2025-TPs/TP6/archivos/ej1/nombres_apellidos.txt", "rt", encoding="utf-8-sig") as archivo:
            while True:
                nombre_apellido = archivo.readline().lower()
                if not nombre_apellido:
                    break

                apellido, nombre = nombre_apellido.strip().split(separador)
                a_mandar = diccionario_apellidos.get(apellido[-3:], "") or diccionario_apellidos.get(apellido[-2:], "") # Guarda el caso que sea verdadero, sino no guarda nada

                if a_mandar:
                    a_mandar_ruta = f"AyED1-2025-TPs/TP6/archivos/ej1/{a_mandar}.txt"
                    guardar_nombre_apellido(apellido, nombre, a_mandar_ruta)
    
    except FileNotFoundError as msg:
        print(f'No se encuentra el archivo: {msg}')
    except OSError as msg:
        print(f'No se puede leer el archivo: {msg}')
    except:
        print('Error en los datos')
    else:
        print("Datos guardados correctamente.")

main()