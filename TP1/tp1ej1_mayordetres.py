from typing import List

def pedir_numeros() -> List[int]:
    """
    Pide 3 números validando que sean positivos

    Pre: No se reciben parámetros
    Post: Devuelve una lista con los 3 números que ingresó el usuario
    """
    lista_3_numeros = []
    
    for i in range(3):
        while True:
            num = int(input(f"Ingrese el número {i+1}: "))
            if num > 0:
                break
            else:
                print("ERROR - El número debe ser un entero positivo.")
        
        lista_3_numeros.append(num)
    
    return lista_3_numeros

def mayor_de_tres(a: int, b: int, c: int) -> int:
    """
    Calcula el mayor de los tres números ingresados

    Pre: Los tres parámetros deben ser enteros positivos
    Post: Devuelve el mayor de los tres números, o -1 si no hay un único mayor
    """

    lista_numeros = [a, b, c]
    lista_numeros.sort() # Usa el sort en lugar del sorted() ya que la lista original no se utiliza luego

    if lista_numeros[1] != lista_numeros[2]:
        return lista_numeros[2] 
    else:
        return -1

def main():
    lista_3_num = pedir_numeros()
    num1, num2, num3 = lista_3_num[0], lista_3_num[1], lista_3_num[2] # Los declaré como variables para que quede más legible, también se podía: mayor_de_tres(lista_3_num[0], lista_3_num[1], lista_3_num[2])
    mayor = mayor_de_tres(num1, num2, num3)

    print()
    if mayor != -1:
        print(f"El mayor de los tres números que usted ingresó es el {mayor}")
    else:
        print("No hay un único mayor número entre los que usted ingresó.")

main()