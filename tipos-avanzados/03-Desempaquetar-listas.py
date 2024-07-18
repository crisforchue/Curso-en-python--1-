numeros = [1, 2, 3]

# ## Feo ##
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

primero, segundo, tercero = numeros #Esto se hace para desempaquetar listas.
print(primero, segundo, tercero)

## Para obeter unicamente un elemento ##

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

primero, *otros, ultimo = numeros #Con el asterisco, estamos guardando los otros elementos de la lista, y unicamente se nos imprimira
                          #El primer elemento
print(primero, otros, ultimo)

