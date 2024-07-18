mascotas = ["perro", 
            "gato", 
            "pez", 
            "perro",
            "Vaca",
            "erizo"]
            
mascotas.insert(1, "Toro") #Va a colocar a nuestro string, "Toro", en el indice que le indiquemos, en este caso, "1"
mascotas.append("Otro erizo") #Append va a agregar el elemento a final de la lista.
mascotas.remove("perro") #Elimina el elemento de la lista
mascotas.pop() #Elimina el utlimo elemento, si se le da un indice, elimina el de ese indice.
del mascotas[0] #Elimina el elemento dependiendo del indice que le demos
mascotas.clear() #Limpia la lista por completo.
print(mascotas)