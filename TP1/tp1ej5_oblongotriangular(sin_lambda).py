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

def es_oblongo(num: int) -> bool:
    """
    Calcula si el número recibido como parámetro es oblongo o no

    Pre: El número debe ser un entero positivo
    Post: La función devuelve True o False de acuerdo a si es oblongo o no
    """
    a = 0
    b = 1
    oblongo = False

    while a*b < num: # Prueba multiplicando con todos los numeros consecuentes hasta que el resultado supere al número al que se quiere llegar
        a += 1
        b += 1

        if a*b == num:
            oblongo = True
    
    return oblongo

def es_triangular(num: int) -> bool:
    """
    Calcula si el número recibido como parámetro es triangular o no

    Pre: El número debe ser un entero positivo
    Post: La función devuelve True o false de acuerdo a si es triangular o no
    """
    contador = 0
    acumulador = 0
    triangular = False

    while acumulador < num: # Se van sumando los números del 1 en adelante hasta que el resultado llegue al número o lo supere
        contador += 1
        acumulador += contador

        if acumulador == num:
            triangular = True
    
    return triangular

def main():
    num = pedir_positivo()
    
    print()
    if es_oblongo(num):
        print(f"El número {num} es oblongo.")
    else:
        print(f"El número {num} no es oblongo.")
    
    if es_triangular(num):
        print(f"El número {num} es triangular.")
    else:
        print(f"El número {num} no es triangular.")

main()