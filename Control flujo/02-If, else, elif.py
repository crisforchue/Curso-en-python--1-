edad = 70
if edad > 65:
    print("Puedes ver la pelicula con super descuento.")
elif edad > 54: #Operadores logico para condicionar el codigo.
    print("Puede ver la pelicula, con descuento")
elif edad > 17:
    print("Puede ver la pelicula") #Se utiliza de intermediario para if, else; evitando la constante repeticion de else/ifs
else: 
    print("No puede entrar") #Asegurarse que todo este tabulado a la derecha.
    print("Ve a otro lado")
print("Acabado")

## Los if, else se evaluan en orden, se debe tener un orde logico. 
## Se puede utilizar el if, elif sin necesariamente usar el else.