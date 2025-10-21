def generar_diccionario_cuadr(minimo: int, maximo: int) -> dict:
    """
    Genera un diccionario con claves desde los números ingresados de mínimo a máximo, cuyos valores corresponden
    al cuadrado de las claves.

    Pre: Recibe como parámetros dos enteros correspondientes al mínimo y máximo del rango de claves.
    Post: Retorna un diccionario con claves desde el mínimo al máximo, cuyos valores son el cuadrado de las claves.
    """
    return {num: num**2 for num in range(minimo, maximo+1)}


def main():
    diccionario_cuadrados = generar_diccionario_cuadr(1, 20)
    print(f"El diccionario de números y sus cuadrados del 1 al 20 es el siguiente:\n{diccionario_cuadrados}")

main()