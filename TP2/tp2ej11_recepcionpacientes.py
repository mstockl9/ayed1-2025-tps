from typing import List

def pedir_paciente() -> int:
    """
    Pide el número de afiliado del paciente y valida que tenga 4 dígitos (excepto si es -1 para detener la carga de pacientes).

    Pre: No recibe parámetros.
    Post: Retorna el número de afiliado del paciente.
    """
    while True:
        nro_afiliado = int(input("Ingrese el número de afiliado del paciente: "))
        if nro_afiliado != -1 and nro_afiliado < 1000 or nro_afiliado > 9999:
            print("ERROR - El número de afiliado debe tener 4 dígitos.")
        else:
            break
    
    return nro_afiliado

def pedir_atencion() -> int:
    """
    Pide y valida el tipo de atención del paciente, siendo 0 por urgencia o 1 con turno.

    Pre: No ingresan parámetros.
    Post: Retorna 0 o 1 según ingrese el usuario.
    """
    while True:
        atencion = int(input("Ingrese el tipo de atención al paciente (0- De urgencia, 1- Con turno): "))
        if atencion != 0 and atencion != 1:
            print("ERROR - Debe ser 0 o 1.")
        else:
            break
    
    return atencion

def listar_pacientes(lista_pacientes: List[int], lista_atencion: List[int]) -> tuple[List[int]]:
    """
    Clasifica la lista de pacientes en atendidos por urgencia y en atendidos por turno en orden de llegada.

    Pre: Se recibe como parámetro la lista de pacientes y la lista de atenciones correspondiente.
    Post: Retorna una tupla con dos listas, la primera con los números de afiliado de pacientes que ingresaron por urgencia, y la segunda
    con los que ingresaron por turno.
    """
    lista_urgencia = [paciente for paciente, turno in zip(lista_pacientes, lista_atencion) if not turno]
    lista_turno = [paciente for paciente, turno in zip(lista_pacientes, lista_atencion) if turno]

    return lista_urgencia, lista_turno

def buscar_afiliado(afiliado: int, lista_pacientes: List[int], lista_atencion: List[int]) -> tuple[int]:
    """
    Recibe un número de afiliado y cuenta cuántas veces fue atendido de urgencia y cuántas veces fue atendido de por turno.

    Pre: Recibe el número del paciente, junto con la lista de pacientes y de números de atención para realizar la búsqueda.
    Post: Retorna una tupla con dos enteros, el primero correspondiente a la cantidad de veces que fue atendido de urgencia
    y el segundo a las veces atendido por turno.
    """
    x_urgencia = 0
    x_turno = 0

    for paciente, turno in zip(lista_pacientes, lista_atencion):
        if paciente == afiliado and turno:
            x_turno += 1
        elif paciente == afiliado and not turno:
            x_urgencia += 1
    
    return x_urgencia, x_turno

def opciones() -> None:
    op = ["Salir del programa", "Cargar pacientes al sistema", "Mostrar listado de pacientes atendidos por urgencia y por turno en orden de llegada", "Búsqueda de un número de afiliado"]

    print("Las opciones disponibles son las siguientes:")
    for i, opcion in enumerate(op):
        print(f"{i}- {opcion}")

def menu():
    pacientes = []
    atencion = []

    while True:
        opciones()
        if not pacientes:
            print("---AVISO: Faltan cargar pacientes---")
        op = input("\nIngrese una de las opciones disponibles: ")

        print()
        if op == "1":
            while True:
                paciente = pedir_paciente()

                if paciente != -1:
                    tipo_atencion = pedir_atencion()
                    pacientes.append(paciente)
                    atencion.append(tipo_atencion)
                else:
                    print("La carga se realizó con éxito.")
                    break
        
        elif op == "0":
            print("El programa ha finalizado.")
            break
                
        else:
            if len(pacientes):
                if op == "2":
                    lista_urgencia, lista_turno = listar_pacientes(pacientes, atencion)

                    print()
                    print("Pacientes atendidos por urgencia:")
                    for paciente in lista_urgencia:
                        print(f"Afiliado N°{paciente}")
                    print("Pacientes atendidos por turno:")
                    for paciente in lista_turno:
                        print(f"Afiliado N°{paciente}")
                    
                elif op == "3":

                    while True:
                        afiliado = pedir_paciente()

                        print()
                        if not pacientes.count(afiliado) and afiliado != -1:
                            print("ERROR - El paciente que usted ingresó no está cargado en el sistema.")
                        elif afiliado != -1:
                            x_urgencia, x_turno = buscar_afiliado(afiliado, pacientes, atencion)
                            print(f"Datos de Afiliado N°{afiliado}:")
                            print(f"Atendido por urgencia: {x_urgencia} veces.")
                            print(f"Atendido por turno: {x_turno} veces.")

                        else:
                            break
                    
                else:
                    print("ERROR - Opción inválida.")
            
            else:
                print("ERROR - No hay pacientes cargados aún.")
            print()

menu()