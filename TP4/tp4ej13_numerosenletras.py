import random as rnd

def pedir_num() -> int:
    """
    Pide un número al usuario y valida que esté entre 0 y 999.999.999.999.999.

    Pre: No recibe parámetros.
    Post: Retorna el número ingresado por el usuario, validado previamente.
    """
    while True:
        num = input("Ingrese un número: ")
        try:
            num = int(num)
        except ValueError:
            print("ERROR - Debe ingresarse un número entero.")
        else:
            if num >= 0 and num <= 999_999_999_999_999:
                return num
            else:
                print("ERROR - El número debe ser entre 0 y 999.999.999.999.999")

def numero_a_letras(num: int) -> str:
    """
    Convierte el número entero ingresado a su expresión en letras.

    Pre: Recibe como parámetro un número entero entre 0 y 999.999.999.999.999.
    Post: Retorna una cadena con la expresión del número entero ingresado a letras.
    """
    diccionario_miles = {5: "billón", 4: "mil millón", 3: "millón", 2: "mil"}
    diccionario_num = {900: "novecientos", 800: "ochocientos", 700: "setecientos", 600: "seiscientos", 500: "quinientos", 400: "cuatrocientos",
                       300: "trescientos", 200: "doscientos", 100: "cien", 90: "noventa", 80: "ochenta", 70: "setenta", 60: "sesenta", 50: "cincuenta",
                       40: "cuarenta", 30: "treinta", 20: "veinte", 15: "quince", 14: "catorce", 13: "trece", 12: "doce", 11: "once", 10: "diez", 9: "nueve", 8: "ocho", 
                       7: "siete", 6: "seis", 5: "cinco", 4: "cuatro", 3: "tres", 2: "dos", 1: "uno", 0: "cero"}
    
    # Acá se fragmenta el entero en una lista de strings, separando elementos por donde estarían las puntuaciones que separan los miles
    num_str_inv = str(num)[-1: :-1]
    lista_numero = [num_str_inv[inicio:inicio+3] for inicio in range(0, len(num_str_inv), 3)]
    lista_numero.reverse()
    lista_numero = [num[-1: :-1] for num in lista_numero]

    nombre_numero = ""
    dato_mil = len(lista_numero)
    for x in lista_numero:
        x_entero = int(x)
        
        multiplicador = 10**(len(x)-1) # Tiene tantos ceros como digitos en el elemento de la lista, luego se va dividiendo por 10 para encontrar su expresión en el diccionario
        for digito in x:
            digito_entero = int(digito)
             # Si el digito en el que se está es 0 (y no es el único digito ingresado), o está en los miles y el elemento de la lista es uno continúa el multiplicador y continúa sin expresar valor en letras (para evitar imprimir ceros o 'un mil')
            if not digito_entero and len(x) != 1 or x_entero == 1 and dato_mil == 2:
                multiplicador //= 10
                continue

            if x_entero <= 10 or x_entero >= 30 or x_entero == 20: # Trabaja sólo con números distintos a dieci... y veinti...
                digito_multip = digito_entero * multiplicador
                agregar_digito = diccionario_num[digito_multip]

                if digito_multip == 1 and dato_mil > 1: # Si está en los miles para arriba, si termina en uno lo expresa como "un" en lugar de "uno"
                    agregar_digito = "un"
                if digito_multip == 100 and x_entero > 100: # Si está por expresar 'cien' y el elemento de la lista no es cien solo, lo expresa como 'ciento'
                    agregar_digito += "to"
                
                nombre_numero += agregar_digito + " " # Acá se agrega a la cadena
                if len(str(digito_multip)) == 2 and x[-1] != "0": # Si está trabajando con dos digitos y el último no es cero, se continúa con un 'y'
                    nombre_numero += "y" + " "
                multiplicador //= 10
            
            # Esta parte está dedicada a trabajar con los dieci y veintitantos, tomando los dos últimos números del elemento de la lista, o el elemento entero si sólo tiene dos dígitos.
            ultimos_dos_num = int(x[1:]) if len(x) == 3 else x_entero
            if ultimos_dos_num > 10 and ultimos_dos_num < 30 and ultimos_dos_num != 20:
                ultimo_digito = int(x[-1])
                if ultimos_dos_num > 20:
                    agregar_digito = diccionario_num[20][ :5]+"i"+diccionario_num[ultimo_digito] # 'veinti' + el número con el que se esté trabajando
                elif ultimos_dos_num < 20 and ultimos_dos_num > 15:
                    agregar_digito = diccionario_num[10][ :3]+"ci"+diccionario_num[ultimo_digito] # 'dieci' + el número con el que se esté trabajando
                elif ultimos_dos_num > 10 and ultimos_dos_num <= 15:
                    agregar_digito = diccionario_num[ultimos_dos_num] # Para once, doce, etc... agrega ese número del diccionario directamente
                if ultimo_digito == 6: # Si es veintiséis o dieciséis le agrega la tilde
                    agregar_digito = agregar_digito.replace("e", "é") # Se reemplazan todas las "e" por "é" quedando, por ejemplo, 'diéciséis'
                    agregar_digito = agregar_digito.replace("é", "e", 1) # Se reemplaza la primera aparición de una "é" por "e", 'dieciséis'
                
                nombre_numero += agregar_digito + " "
                break # No hace falta seguir con el bucle

        if dato_mil > 1 and x_entero: # Si está trabajando de mil para arriba al final de calcular el número suma la expresión en miles.
            nombre_mil = diccionario_miles[dato_mil]
            if x_entero > 1 and dato_mil > 2: # Si el elemento de la lista es mayor a uno y no se está trabajando con mil, por ejemplo, pasa de 'millón' a 'millones'
                nombre_mil += "es"
                nombre_mil = nombre_mil.replace("ó", "o") # Reemplaza la 'ó' con tilde para expresarlo en plural
            nombre_numero += nombre_mil + " " # Acá se agrega la expresión en miles
        
        dato_mil -= 1 # Se va restando, por ejemplo, de mil millón, a millón, a mil
    
    return nombre_numero.capitalize()

def main():
    num = pedir_num()
    num_en_letras = numero_a_letras(num)
    print(f"El número {num} expresado en letras es el siguiente:\n{num_en_letras}")

main()