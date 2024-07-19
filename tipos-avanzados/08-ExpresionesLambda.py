usuarios = [[2, "A"], 
            [6, "D"], 
            [4, "C"]]

usuarios.sort(key=lambda el: el[1]) #El lambda se utiliza como una una funcion anomima, toma "el" de la lista (usuarios) y busca el primer elemento de esa lista. 
                                    #"El" son las sublistas, y "El[1]" es el llamado de la primera lista.
print(usuarios)