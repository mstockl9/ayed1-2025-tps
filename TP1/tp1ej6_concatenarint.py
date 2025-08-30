def pedir_positivo() -> int:
    """
    Pide y valida que el número sea positivo

    Pre: No se ingresan parámetros
    Post: Devuelve el número que ingresó el usuario
    """
    while True:
        num = int(input("Ingrese un número natural: "))
        if num > 0:
            break
        else:
            print("ERROR - El número debe ser mayor que 0.")
    
    return num

def contar_digitos(num: int) -> int:
    """
    Cuenta los dígitos de el número entero positivo que reciba como parámetro

    Pre: El número debe ser un entero positivo
    Post: Retorna un entero correspondiente a la cantidad de dígitos que tiene el número que ingresó, si ingresa un número negativo retorna -1
    """
    if num >= 0: # Validación previa, ya que si es 0 o menor num nunca es distinto a 0
        cant_digitos = 0
        
        while num:
            num //= 10
            cant_digitos += 1
        
        return cant_digitos
    
    return -1

def concatenar(num1: int, num2: int) -> int:
    """
    Concatena los dos parámetros recibidos en un único número entero

    Pre: Los números recibidos deben ser ambos enteros positivos
    Post: Se devuelve un entero con la concatenación de los dos parámetros
    """
    multiplicador = 10 ** contar_digitos(num2)
    num1_multiplicado = num1 * multiplicador

    concatenacion = num1_multiplicado + num2
    return concatenacion

def main():
    num1 = pedir_positivo()
    num2 = pedir_positivo()

    concatenacion = concatenar(num1, num2)
    print(f"\nLa concatenación de sus dos números es: {concatenacion}")

main()