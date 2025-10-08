def sumar_reales(a: str, b: str) -> float:
    """
    Suma los dos números ingresados como parámetro como strings, validando si alguno no contiene un
    número válido.

    Pre: Recibe dos números reales, en formato string.
    Post: Retorna un flotante correspondiente a la suma de los dos números, o -1 si no se ingresaron números válidos.
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return -1.0 # Para que la función no retorne dos tipos de dato
    else:
        return a + b

def main():
    a = input("Ingrese el valor del primer número: ")
    b = input("Ingrese el valor del segundo número: ")
    suma = sumar_reales(a, b)

    if suma == int(suma): # Lo castea a entero si se termina en .0
        suma = int(suma)
    if suma != -1.0:
        print(f"El resultado de sumar {a} y {b} es: {suma}")
    else:
        print("ERROR - Se ingresaron valores no válidos.")

main()