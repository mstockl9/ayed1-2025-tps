def pedir_viajes() -> int:
    """
    Pide la cantidad de viajes y valida que no sea un número negativo

    Pre: No necesita parámetros
    Post: Devuelve el entero que ingresó el usuario
    """

    while True:
        cant_viajes = int(input("Ingrese la cantidad de viajes realizados en el mes: "))
        if cant_viajes >= 0:
            break
        else:
            print("ERROR - La cantidad de viajes no puede ser negativa.")
    
    return cant_viajes

def calcular_gastos(cant_viajes: int) -> float:
    """
    Calcula el total mensual de gastos en el subte según la cantidad de viajes realizados en el mes

    Pre: La cantidad de viajes no debe ser un número negativo
    Post: Devuelve el total mensual de gastos según la cantidad de viajes en el mes y su respectivo descuento
    """
    total_gasto = 0.00
    valor_subte = 963.00
    
    if cant_viajes >= 1 and cant_viajes <= 20:
        total_gasto = cant_viajes * valor_subte
    
    elif cant_viajes >= 21 and cant_viajes <= 30:
        total_gasto = (20 * valor_subte) + ((cant_viajes - 20) * (valor_subte - (valor_subte * 0.2))) # Los primeros 20 viajes se hacen sin descuento, y el resto con un descuento del 20%
    
    elif cant_viajes >= 31 and cant_viajes <= 40:
        total_gasto = (20 * valor_subte) + (10 * (valor_subte - (valor_subte * 0.2))) + ((cant_viajes - 30) * (valor_subte - (valor_subte * 0.3))) # Los primeros 20 sin descuento, 10 con descuento del 20% y el resto con 30%
    
    elif cant_viajes > 40:
        total_gasto = (20 * valor_subte) + (10 * (valor_subte - (valor_subte * 0.2))) + (10 * (valor_subte - (valor_subte * 0.3))) + ((cant_viajes - 40) * ((valor_subte) - (valor_subte * 0.4))) # 20 sin descuento, 10 con descuento de 20%, 10 con 30% y el resto con 40%
    
    return total_gasto

def main():
    cant_viajes = pedir_viajes()
    total_gasto = calcular_gastos(cant_viajes)

    print(f"\nEl total mensual que usted gastó en viajes subterráneos es de: ${total_gasto: .2f}")

main()