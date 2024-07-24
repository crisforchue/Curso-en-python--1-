import random

def AdivinaNumero(x):

    print("Bienvenido al juego")
    print(f"Selecciona un numero entre 1, {x} para comenzar.")

    limiteInf = 1
    LimiteSup = x

    respuesta = " "
    while respuesta != "r": 
        if limiteInf != LimiteSup: 
            prediccion = random.randint(limiteInf, LimiteSup)
        else: 
            prediccion = limiteInf #Puede ser el limite superior igual, cualquiera funciona.

        #Obtener respuesta# 
        respuesta = input(f"La prediccion es {prediccion}. Si es alta, ingresa A, si es baja, ingresa B, si es correcta, ingresa R: ").lower()

        if respuesta == "a":
            LimiteSup = prediccion - 1
        elif respuesta == "b":
            limiteInf = prediccion + 1
        elif respuesta == "r":    
         print(f"Si, la computadora adivino tu numero. Tu numero es {prediccion}")
    


AdivinaNumero(10)