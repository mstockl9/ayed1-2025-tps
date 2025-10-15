def uno_al_cienmil() -> None:
    """
    Imprime por pantalla todos los números del 1 al 100.000, deteniéndose cuando se termina de imprimir o
    cuando el usuario preciona Ctrl-C.

    Pre: No recibe parámetros.
    Post: No retorna nada, solo imprime los números hasta que el usuario presione Ctrl-C
    """
    for nro in range(1, 100_000+1):
        try:
            print(nro)
        except KeyboardInterrupt:
            op = input("¿Desea interrumpir la generación de números? (1- Si, 0 u otra cosa- No): ")
            if op == "1":
                break

def main():
    input("A continuación se imprimen todos los números del 1 al 100.000, si quiere detener el proceso presione Ctrl-C (Presione Enter)")
    uno_al_cienmil()
    print("Proceso finalizado.")

main()