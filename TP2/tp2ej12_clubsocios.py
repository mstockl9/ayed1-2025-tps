from typing import List

def pedir_socio() -> int:
    """
    Pide el número de socio y valida que contenga 5 dígitos (excepto si es 0 para dejar de ingresar socios).

    Pre: No recibe parámetros.
    Post: Retorna el número de socio validado previamente.
    """
    while True:
        nro_socio = int(input("Ingrese el número de socio: "))
        if nro_socio != 0 and (nro_socio < 10000 or nro_socio > 99999):
            print("ERROR - El número de socio debe contener 5 dígitos.")
        else:
            break
    
    return nro_socio

def listar_ingresos(lista_ingresos: List[int]) -> tuple[List[int]]:
    """
    Lista cada socio y su respectiva cantidad de ingresos al club.

    Pre: Recibe como parámetro la lista de ingresos a recorrer.
    Post: Retorna una tupla con dos listas, correspondientes a cada socio y la cantidad de ingresos registrada.
    """
    lista_socios = []

    # Lista socios se llena sin contener socios repetidos
    for ingreso in lista_ingresos:
        if ingreso not in lista_socios: # Si ya está en lista_socios no se agrega
            lista_socios.append(ingreso)
    
    lista_ingresos = [lista_ingresos.count(socio) for socio in lista_socios] # Para cada socio en la lista generada de socios cuenta cuántas veces aparece

    return lista_socios, lista_ingresos

def eliminar_socio(nro_socio: int, lista_ingresos: List[int]) -> int:
    """
    Elimina del registro de ingresos todas las apariciones de el socio que se ingrese como parámetro y calcula la cantidad
    de ingresos eliminados.
    Modifica la lista original.

    Pre: Ingresan como parámetros el número del socio a eliminar y la lista de ingresos.
    Post: Modifica la lista eliminando al socio y retorna la cantidad de ingresos eliminados.
    """
    cant_ingresos = lista_ingresos.count(nro_socio)
    ingresos_eliminados = 0

    for i in range(cant_ingresos):
        lista_ingresos.remove(nro_socio)
        ingresos_eliminados += 1
    
    return ingresos_eliminados

def opciones() -> None:
    op = ["Salir del programa", "Cargar socios al sistema", "Informar para cada socio cuántas veces ingresó al club", "Eliminar todos los ingresos de un socio"]

    print("Las opciones disponibles son las siguientes:")
    for i, opcion in enumerate(op):
        print(f"{i}- {opcion}")

def menu():
    ingresos_socios = [51933, 51933, 58339, 14223, 14223, 94142, 59315, 51933, 94142, 94209, 51933]

    while True:
        opciones()
        if not ingresos_socios:
            print("---AVISO: Faltan cargar socios---")
        op = input("Ingresa una de las opciones disponibles: ")

        print()
        if op == "1":
            while True:
                nro_socio = pedir_socio()
                if nro_socio != 0:
                    ingresos_socios.append(nro_socio)
                else:
                    print("La carga se realizó con éxito.")
                    break
        
        elif op == "0":
            print("El programa ha finalizado.")
            break

        else:
            if ingresos_socios:
                if op == "2":
                    lista_socios, cant_ingresos = listar_ingresos(ingresos_socios)
                    for socio, ingresos in zip(lista_socios, cant_ingresos):
                        print(f"Socio N°{socio}: {ingresos} ingreso/s")

                elif op == "3":
                    while True:
                        nro_socio = pedir_socio()
                        if not ingresos_socios.count(nro_socio):
                            print("ERROR - El socio que usted ingresó no se encuentra en el sistema.")
                        else:
                            break
                    
                    print(f"\nLos registros de entrada al club antes de entrada al club antes de eliminar al socio son los siguientes:\n{ingresos_socios}")
                    cant_eliminados = eliminar_socio(nro_socio, ingresos_socios)
                    print(f"\nLos registros de ingreso luego de eliminado el socio son los siguientes\n{ingresos_socios}")
                    print(f"\nIngresos eliminados: {cant_eliminados}")
                
                else:
                    print("ERROR - Opción inválida.")

            else:
                print("ERROR - Faltan cargar socios.")
            print()

menu()