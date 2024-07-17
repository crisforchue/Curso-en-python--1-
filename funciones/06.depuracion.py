def largo(texto):
    resultado = 0
    for _ in texto: #Podemos poner un _ para quitar el error de no usar una variable
        resultado += 1
    return resultado


print("Heavens")    
l = largo("Hola mundo")
print(l)