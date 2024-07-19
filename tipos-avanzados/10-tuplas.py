numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1,2]) ## Los perimeros dos elementos va a darlos como una tupla
menosNumeros = numeros[:2]
print(menosNumeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)
for n in numeros:
    print(n)

## "Modificar" una tupla ##
listanumeros = list(numeros)
listanumeros[0] = "0"
print(listanumeros)