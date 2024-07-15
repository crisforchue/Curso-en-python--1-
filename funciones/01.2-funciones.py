def holis(nombre, apellido="Hartfelt"): # Estos son parametros opcionales
    print("Hola mundo")
    print(f"bienvenido, {nombre} {apellido}")

holis("Alex", "brightman") 
holis("Alastor")

#Si se le da un argumento como en la primera funcion, se va a imprimir ese argumento.
#Si no se le da un argumento como en la segunda funcion, se imprime el parametro por defecto,
#en este caso, siendo "Hartfelt"'

## ARGUMENTOS NOMBRADOS ##

holis(apellido="brightman", nombre="Alex") 

# Si indicamos en el argumento que variable pertenece a cada posicion, se nos va a
# poner en la forma en que queramos. (un poco tedioso, en mi parecer)