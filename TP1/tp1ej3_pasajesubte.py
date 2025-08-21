import typing

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
    valor_subte = 963.00

    if cant_viajes == 0:
        total_gasto = 0.00
    
    elif cant_viajes >= 1 and cant_viajes <= 20:
        total_gasto = cant_viajes * valor_subte
    
    elif cant_viajes >= 21 and cant_viajes <= 30:
        descuento = 20
        total_gasto = cant_viajes * (valor_subte - (valor_subte * descuento / 100))
    
    elif cant_viajes >= 31 and cant_viajes <= 40:
        descuento = 30
        total_gasto = cant_viajes * (valor_subte - (valor_subte * descuento / 100))
    
    elif cant_viajes > 40:
        descuento = 40
        total_gasto = cant_viajes * (valor_subte - (valor_subte * descuento / 100))
    
    return total_gasto

def main():
    cant_viajes = pedir_viajes()
    total_gasto = calcular_gastos(cant_viajes)

    print(f"\nEl total mensual que usted gastó en viajes subterráneos es de: ${total_gasto: .2f}")

main()