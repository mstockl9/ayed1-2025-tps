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

def calcular_jugo_y_total(cant_cosechadas: int) -> tuple[int]: # Calcula ambas cosas en la misma función ya que los valores de peso random sólo se pueden evaluar acá
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

        if peso_unidad < 200 or peso_unidad > 300: # Si no se encuentra en el rango de peso se procesa como jugo, pero interpreto que sigue incluyéndose en los cajones
            cant_jugo += 1
        
        total_gramos += peso_unidad
    
    return cant_jugo, total_gramos

def calcular_cajas(cant_naranjas: int) -> int:
    """
    Calcula cuántos cajones llenan la cantidad de naranjas que ingresa como parámetro

    Pre: La cantidad de naranjas debe ser un entero positivo.
    Post: Retorna la cantidad de cajas necesarias para llevar la cantidad de naranjas ingresadas
    """
    max_naranjas_x_cajon = 100

    cant_cajas, sobrante_cajas = divmod(cant_naranjas, max_naranjas_x_cajon)
    if sobrante_cajas:
        cant_cajas += 1

    return cant_cajas

def calcular_camiones(total_gramos: int) -> tuple[int]:
    """
    Calcula cuántos camiones se necesitan para transportar la cosecha, y los gramos sobrantes que no se despacharon

    Pre: El peso total en gramos debe ser un entero positivo
    Post: Retorna la cantidad de camiones necesarios para transportar el total de la cosecha y las naranjas en gramos que sobraron
    """

    max_camion = 500_000
    cant_camiones, sobrante_camion = divmod(total_gramos, max_camion)

    if sobrante_camion >= 400_000: # Si lo que resta es igual o mayor al 80 % de la capacidad total del camión, puede despacharse uno más
        cant_camiones += 1
        sobrante_camion -= 400_000
    
    return cant_camiones, sobrante_camion

def main():
    total_cosecha = pedir_cosecha()

    cant_jugo, total_gramos = calcular_jugo_y_total(total_cosecha)
    cant_cajas = calcular_cajas(total_cosecha)
    cant_camiones, sobrante_camion = calcular_camiones(total_gramos)

    if cant_camiones:
        resultados_str = ["Cajones a llenar:", "Sobrante total de naranjas en gramos:", "Cantidad de naranjas para procesar como jugo:", "Camiones necesarios para transportar la cosecha:"]
        resultados_int = [cant_cajas, sobrante_camion, cant_jugo, cant_camiones]

        print("\nDe los datos recopilados, elaboramos el siguiente informe:")
        print("-"*40)
        for info, cant in zip(resultados_str, resultados_int):
            print(f"{info} {cant}")
    
    else:
        print("No hubo naranjas suficientes para despachar camiones debido al costo.")
        print(f"Naranjas sobrantes en gramos: {sobrante_camion}")

main()