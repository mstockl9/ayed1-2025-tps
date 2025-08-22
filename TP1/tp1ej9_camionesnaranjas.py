import typing
import random as rnd

def pedir_cosecha() -> int:
    """
    Pide al usuario el total de naranjas cosechadas validando que sea mayor a 0

    Pre: No entran parámetros a la función
    Post: Retorna el entero validado que ingresó el usuario
    """
    while True:
        cosecha = int(input("Ingrese el total de naranjas cosechadas: "))
        if cosecha > 0:
            break
        else:
            print("ERROR - Cantidad inválida")
    
    return cosecha

def calcular_jugo_y_total(cant_cosechadas: int) -> int: # Calcula ambas cosas en la misma función ya que los valores de peso random sólo se pueden evaluar acá
    """
    Calcula cuántas naranjas se procesan como jugo de acuerdo a su peso y el total en gramos de la cosecha

    Pre: La cantidad de naranjas cosechadas debe ser un entero mayor a 0
    Post: Retorna dos enteros, correspondientes a la cantidad de naranjas que se procesan para jugo y el peso total de naranjas en gramos
    """
    cant_jugo = 0
    total_gramos = 0

    for i in range(cant_cosechadas):
        peso_unidad = rnd.randint(150, 350)
        total_gramos += peso_unidad

        if peso_unidad < 200 or peso_unidad > 300: # Si no se encuentra en el rango de peso se procesa como jugo
            cant_jugo += 1
        
        total_gramos += peso_unidad
    
    print(total_gramos)
    
    return cant_jugo, total_gramos

def calcular_cajas_y_sobrante(cant_naranjas: int) -> int:
    """
    Calcula cuántos cajones llenan la cantidad de naranjas que ingresa como parámetro y cuántas
    naranjas sobrantes quedan

    Pre: La cantidad de naranjas debe ser un entero positivo.
    Post: Retorna dos enteros, la cantidad de cajas y la cantidad de naranjas sobrantes
    """
    max_naranjas_x_cajon = 100

    cant_cajas = cant_naranjas // max_naranjas_x_cajon
    sobran_naranjas = cant_naranjas % max_naranjas_x_cajon

    return cant_cajas, sobran_naranjas

def calcular_camiones(total_gramos: int) -> int:
    """
    Calcula cuántos camiones se necesitan para transportar la cosecha

    Pre: El peso total en gramos debe ser un entero positivo
    Post: Retorna la cantidad de camiones necesarios para transportar el total de la cosecha
    """

    max_camion = 500_000
    cant_camiones = total_gramos // max_camion

    if total_gramos % max_camion >= 400_000: # Si lo que resta es igual o mayor al 80 % de la capacidad total del camión, puede despacharse uno más
        cant_camiones += 1
    
    return cant_camiones

def main():
    total_cosecha = pedir_cosecha()

    cant_jugo, total_gramos = calcular_jugo_y_total(total_cosecha)
    cant_cajas, sobran_naranjas = calcular_cajas_y_sobrante(total_cosecha)
    cant_camiones = calcular_camiones(total_gramos)

    print()
    print("De los datos recopilados, elaboramos el siguiente informe:")
    print("-" * 40)
    print(f"Cajones a llenar: {cant_cajas}")
    print(f"Sobrante total de naranjas: {sobran_naranjas}")
    print(f"Cantidad de naranjas para procesar como jugo: {cant_jugo}")
    print(f"Camiones necesarios para transportar la cosecha: {cant_camiones}")

main()