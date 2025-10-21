import random as rnd

def pedir_entero(a_pedir: str) -> int:
    """
    Pide un entero al usuario y valida que sea un número.

    Pre: Recibe como parámetro un string correspondiente al nombre del entero a pedir.
    Post: Retorna el entero validado previamente.
    """
    while True:
        entero = input(f"Ingrese {a_pedir.lower()}: ")
        try:
            entero = int(entero)
        except ValueError:
            print(f"ERROR - {a_pedir.capitalize()} debe ser un número entero.")
        else:
            return entero

def generar_diccionario_libreria() -> dict:
    """
    Genera o simula un diccionario con productos de una librería y precios generados aleatoriamente.

    Pre: No recibe parámetros.
    Post: Retorna un diccionario que simula productos en una librería.
    """
    lista_productos = ["cuadernos", "fibrones", "hojalillos", "lapiceras", "hojas", "lapices", "tijeras", "resaltadores", "portafolios", "carpetas"]
    diccionario_libreria = {producto: float(rnd.randint(80, 460)*10) for producto in lista_productos}
    
    return diccionario_libreria

def aumentar_precio(producto: str, aumento: int, diccionario_libreria: dict) -> dict:
    """
    Aumenta los precios de el producto ingresado en el porcentaje recibido.

    Pre: Recibe como parámetros el nombre del producto, el porcentaje a aumentar y el diccionario de los productos y precios.
    Post: Retorna el diccionario modificado, con el precio del producto aumentado. Si no existe el producto, retorna un diccionario vacío.
    """
    try:
        diccionario_libreria[producto] += diccionario_libreria[producto] * aumento / 100
    except KeyError:
        return {}
    else:
        return diccionario_libreria

def listar_productos(diccionario_libreria: dict) -> None:
    """
    Lista todos los productos y los precios dentro del diccionario recibido.

    Pre: Recibe como parámetro el diccionario, cuyas claves son los nombres de los productos y los valores son los precios.
    Post: No retorna nada. Sólo imprime el listado.
    """
    mayor_longitud = max([len(producto) for producto in diccionario_libreria.keys()])

    print("PRODUCTO", " "*14, "PRECIO")
    for producto, precio in diccionario_libreria.items():
        print("-"*30)
        print(producto.title(), " "*(10-(len(producto)-mayor_longitud)), precio)

def item_mas_costoso(diccionario_libreria: dict) -> tuple[str, int]:
    """
    Calcula el ítem más costoso del diccionario recibido.

    Pre: Recibe como parámetro el diccionario con productos y precios.
    Post: Retorna una tupla cuyos elementos corresponden al nombre y al precio del producto más costoso.
    """
    lista_libreria = [(precio, producto) for producto, precio in diccionario_libreria.items()]
    mas_costoso = max(lista_libreria)
    precio, producto = mas_costoso

    return producto, precio

def mostrar_opciones(op: tuple[str]) -> None:
    """
    Imprime y enumera las opciones que recibe como parámetro. La primera opción debe ser la de salir del programa.

    Pre: Recibe como parámetro una tupla con strings correspondientes a las opciones.
    Post: No retorna nada, imprime y enumera las opciones.
    """
    print("Las opciones disponibles son las siguientes:")
    for i, opcion in enumerate(op):
        print(f"{i}- {opcion}")

def main():
    diccionario_libreria = generar_diccionario_libreria()
    opciones = ("Salir del programa.", "Aumentar los precios de un producto.", "Listar todos los productos.", "Calcular el ítem más costoso.")
    
    while True:
        mostrar_opciones(opciones)
        op = input("Ingrese una de las opciones disponibles: ").strip()

        print()
        if op == "1":
            producto = input("Ingrese el producto a aumentar: ").lower().strip()
            porcentaje_aumento = pedir_entero("el porcentaje a aumentar")
            diccionario_mod = aumentar_precio(producto, porcentaje_aumento, diccionario_libreria)

            if diccionario_mod:
                diccionario_libreria = diccionario_mod
                print("Aumento realizado con éxito.")
            else:
                print("ERROR - No se encontró el producto.")
        
        elif op == "2":
            print("La lista de productos almacenados en el diccionario es la siguiente:\n")
            listar_productos(diccionario_libreria)
        
        elif op == "3":
            producto_mas_costoso, precio_mas_costoso = item_mas_costoso(diccionario_libreria)
            print(f"El producto más costoso es: {producto_mas_costoso.title()}, con un precio de ${precio_mas_costoso: .2f}")
        
        elif op == "0":
            print("El programa ha finalizado.")
            break

        else:
            print("ERROR - Opción inválida.")
        print()

main()