for numero in range(5): #Esta funcion nos dice "Por cada (elemento) en (elemento), luego agregamos las condiciones. Range() es un iterable
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

## ITERABLES ##

for char in "ultimate python": 
   print(char) ## "Por caractere en ultimate python", busca todos los caracteres y va a imprimirlos todos. 

