usuarios = [["A", 2], 
            ["B", 3], 
            ["C", 4]]

## COMO SE HARIA NORMALMENTE ##
# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0]) 
# print(nombres)

## FORMA ELEGANTE DE REALIZARLO ##

#nombres = [expresion for item in items] <-- "Expresion" representa lo que le vamos a pedir al codigo.
                                         # "For item" por cada cosa "in items" en cosas.
nombres = [usuario[0] for usuario in usuarios]
nombres = [usuario for usuario in usuarios if usuario[1] > 3] #Esta expresion nos dice "En usuario, busca por cada usuario y agregalo si
                                                              #El id de usuario es mayor a 3."
print(nombres)