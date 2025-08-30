from typing import List

def pedir_compra_recibido() -> tuple[int]:
    """
    Pide el total de compra y el total recibido, validando que el primero no sea mayor que el segundo

    Pre: No recibe parámetros
    Post: Devuelve el total de la compra y el total recibido
    """
    while True:
        total_compra = int(input("Ingrese el total de la compra: "))
        total_recibido = int(input("Ingrese el total recibido: "))
        
        if total_recibido > total_compra:
            break
        else:
            print("ERROR - El total recibido no puede ser menor que el de compra.")
    
    return total_compra, total_recibido

def cajero_cambio(cambio: int, lista_denom: List[int]) -> List[int]:
    """
    Calcula cuántos billetes de cada denominación se necesitan para satisfacer el cambio minimizando la
    cantidad de billetes

    Pre: El valor de cambio debe ser divisible entre 10, y la lista de denominaciones no debe estar vacía
    Post: Devuelve una lista con la cantidad de billetes necesarios de mayor denominación a menor denominación
    """

    lista_billetes = []

    for denominacion in lista_denom:
        cant_billetes = cambio // denominacion
        cambio %= denominacion

        lista_billetes.append(cant_billetes)
    
    return lista_billetes

def main():
    while True:
        total_compra, total_recibido = pedir_compra_recibido()
        cambio = total_recibido - total_compra
        
        if cambio % 10 != 0: # Si el valor de cambio no termina en 0, no se va a poder representar con billetes, al no haber billetes de $1 por ejemplo
            print("ERROR - No hay suficientes denominaciones de billetes para satisfacer el cambio.")
        else:
            break

    lista_denom = [5000, 1000, 500, 200, 100, 50, 10]
    lista_billetes = cajero_cambio(cambio, lista_denom)

    print(f"\nEl cambio de ${cambio} requiere de los siguientes billetes:")
    for denom, billetes in zip(lista_denom, lista_billetes):
        if billetes:
            print(f"Billetes de {denom}: {billetes}")

main()