# Set signigica grupo o conjunto. Conjunto de dato que no se pueden repetir, y tampoco esta ordenada.

primer = {1, 2, 3, 4, 4, 2, 1}
segundo = [3, 4, 5]
segundo = set(segundo)

print(primer | segundo) #Une ambos sets 
print(primer & segundo) #Interjection. Nos devuelve los elementos que se encuentran en ambos sets.
print(primer - segundo) #Diferencia. Nos muetras los datos el grupo de la izquierda]
print(primer ^ segundo) #Diferencia simetrica. Devuelve los elementos que esten en el primer elemento, en el segundo elemento, pero no 
                        #Los elementos que se encuentren en ambos datos. 

#No se pueden encontrar elementos en los sets. si quisieramos buscar un elemento en concreto deberiamos buscarlo

# print(primer) #Python va a a imprimir todos los elementos pero no va a darnos los elementos duplicados.
# primer.add(5) #Va a agregar el elemento 5.
# primer.remove(1) #Nos va a eliminar los elementos.