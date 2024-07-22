numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])
menosNumeros = numeros[:2]
# Creamos una nueva tupla que contiene los primeros dos elementos de 'numeros', resultando en (1, 2)
print(menosNumeros)

primero, segundo, *otros = numeros
# Desempaquetamos la tupla 'numeros', asignando el primer elemento a 'primero', el segundo a 'segundo', y el resto a 'otros'
print(primero, segundo, otros)

for n in numeros:
    print(n)

# "Modificar" una tupla
listanumeros = list(numeros) # Convertimos la tupla 'numeros' en una lista para poder modificar sus elementos
listanumeros[0] = "0" # Cambiamos el primer elemento de la lista a "0"
print(listanumeros)
