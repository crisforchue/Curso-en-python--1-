people = ["Weichi", "Petal", "Maggie", "Nebs"]
print(people[0]) #Imprime nuestro primer elemento
people[0] = "Karma" #Reemplaza nuestro primer elemento
print(people)
print(people[2:]) #Funciona como los strings.
print(people[-1]) #Los strings negativo van desde el inicio, hacia la izquiera. Como no hay nada a la izquiera, va al final de la lista
print(people[::2]) #Esto toma el primer elemento, lo salta, usa el segundo, salta el tercero, toma el cuerto. 

numeros = list(range(1, 21)) #En este caso, el range comienza en 1.
print(numeros[::2])
print(numeros[1::2])