def get_product(**datos): #Estos tienen un proposito como los xargs, pero esto capturan argumentos
                          #Con nombres, por eso se utilizan 2 "*" en vez de uno.
    print(datos)        #Este primer print nos mostrara todo en get_product
    print(datos["name"])#Este segundo print, le indicamos especificamente que buscamos y nos va a imprimir eso

get_product(id="id", 
            name="Iphone", 
            desc="Esto es un iphone") #Se crea un diccionario 