import random as rnd

def main():
    numero_secreto = rnd.randint(1, 500)
    intentos = 0
    
    print("Se generó un número aleatorio para adivinar, comienza el juego...")
    while True:
        adivina = input("Ingrese un número: ")
        try:
            adivina = int(adivina)
        except ValueError:
            print("ERROR - Debe ingresar un número entero.")
        
        else:
            if adivina < numero_secreto:
                print("El número secreto es mayor...")
            elif adivina > numero_secreto:
                print("El número secreto es menor...")
            else:
                print(f"¡Felicitaciones! El número secreto era: {numero_secreto}")
                print(f"Cantidad de intentos: {intentos}")
                break
        
        intentos += 1
        print()

main()