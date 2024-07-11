#Los range comienzan en cero. Nos dara una lista de esos elementos -1.

for numero in range(5): #Esta funcion nos dice "Por cada (elemento) en (elemento), luego agregamos las condiciones.
    print(numero, numero * "hola mundo")

## FOR ELSE ## 

buscar = 3

for numero in range(5):
  print(numero)
  if numero == buscar:
     print("encontrado", buscar) #Esto nos va a crear un bucle.
     break #Esto nos va a romper el bucle.
else: 
    print("No se encuentra el numero :(")
