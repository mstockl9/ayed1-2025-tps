import random as rnd

def main():
    lista_rnd = [rnd.randint(1, 100) for i in range(20)]
    lista_impares = (list(filter(lambda x: x % 2, lista_rnd)))

    print(f"\nLa lista aleatoria es la siguiente:\n{lista_rnd}")
    print(f"La lista aleatoria sólo con los números impares es la siguiente:\n{lista_impares}")

main()