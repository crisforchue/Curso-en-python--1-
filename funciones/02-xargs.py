def suma(*numeros): #El asterisco siver para indicar que la funcion acepta un numero variable de argumentos.
                    #Lo utilizamos para cuando queramos tener varios argumentos para llamar a la funcion.
    resultado = 0
    for numero in numeros: #Un iterable, donde por cada numero en una lista de numeros, 
                           #Va a sumar eso a nuestro resultado, yay
        resultado += numero
    print(resultado) #Hay que fijarse en la identacion. Si estuviera al nivel del resultado,
                     #Se imprime muchas veces 

suma(3, 5, 6) 
suma(3, 5)
suma(2, 6, 7, 3)