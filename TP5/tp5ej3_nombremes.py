def pedir_numero_mes() -> int:
    """
    Pide el número del mes y valida que sea un número entero.

    Pre: No recibe parámetros.
    Post: Retorna el número ingresado validado previamente.
    """
    while True:
        numero_mes = input("Ingrese el número de un mes: ")
        try:
            numero_mes = int(numero_mes)
        except ValueError:
            print("ERROR - Debe ingresar un número entero.")
        else:
            return numero_mes

def numero_a_mes(nro_mes: int) -> str:
    """
    Calcula el nombre del mes que corresponde al número ingresado.

    Pre: Recibe un entero correspondiente al número del mes.
    Post: Retorna una cadena correspondiente al nombre del més recibido, o una cadena vacía si el número es inválido.
    """
    meses_str = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    try:
        nombre_mes = meses_str[nro_mes-1]
    except IndexError:
        return ""
    else:
        return nombre_mes

def main():
    numero_mes = pedir_numero_mes()
    nombre_mes = numero_a_mes(numero_mes)

    if nombre_mes:
        print(f"El mes con número {numero_mes} es: {nombre_mes}")
    else:
        print("ERROR - Número inválido.")

main()