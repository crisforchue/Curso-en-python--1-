saludo = "Hola Global" #Esto se conoce como variables globales, son malas practicas, 
                       #Hay que usar variables especificas

def saludar():
    global saludo #Esto nos da una variable global
    saludo = "Hola Mundo"
    print(saludo)

def saludaHeavens():
    saludo = "Hola Heavens"
    print(saludo)

saludar()
print(saludo)