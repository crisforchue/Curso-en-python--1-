numeros = [22, 42, 4, 6, 5, 63, 61, 46]

#numeros.sort() #Ordena los numeros.
#numeros.sort(reverse=True) #Con el argumento, lo hace de manera descendiente.

numeros2 = sorted(numeros) #sorted nos va a dar una nueva lista ordenada, en vez de ordernar la lista ya establecida.

print(numeros)
print(numeros2)

usuarios = [[2, "A"], 
            [3, "B"], 
            [4, "C"]]

def ordena(elemento):
    return elemento[1]

usuarios.sort(key=ordena, reverse=True) #Se le pone "key" ya que este parametro no toma argumentos posicionales.
print(usuarios) #Se poner elementos ordenables en la lista para que se pueda poner en el orden correspondiente.

