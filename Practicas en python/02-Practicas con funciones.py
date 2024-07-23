import random

def AdivinaNumero(x):

    print("Bienvenido al juego")
    print("Debes adivinar el numero generado por la computadora")

    numeroAleatorio = random.randint(1, x) # X es el parametro que le vamos a dar a x. 
    prediccion = 0 # Variable base que no se encuentra en el intervalo. 

    while prediccion != numeroAleatorio:
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: "))    
        
        if prediccion < numeroAleatorio: 
            print("El numero es muy menor")
        elif prediccion > numeroAleatorio:
            print("El numero es muy mayor.")

    print("Felicidades, adivinaste")    

AdivinaNumero(10)
