import random


def adivina_el_numero(x): 
    print("=======================")
    print("Bienvenid@ al juego")
    print ("======================")
    print ("Tu meta es adivinar el numero generado por la computadora.")
    numero_aleatorio= random.randint(1,x) #numero aleatorio entre 1 y x
    intentos=5
    prediccion= 0
    while intentos>0:
        #el usuario ingresa un numero
        prediccion= int(input (f"Adivina un numero entre 1 y {x}: "))
        if prediccion==numero_aleatorio:
            print(f"¡Felicitaciones! Avidinaste el numero {numero_aleatorio} correctamente.")
            break
        if prediccion<numero_aleatorio:
            intentos=intentos-1
            print("Intenta otra vez, este numero es muy pequeño.")
        elif prediccion>numero_aleatorio:
            intentos=intentos-1
            print ("Intenta otra vez, este numero es muy grande.")

    if intentos==0:
        print("Lo siento :( has perdido el juego)")

adivina_el_numero(10)