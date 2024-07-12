numero = 1
while numero < 100: #Le damos una condicion inicial, la cual se va a repetir hasta que se deje de cumplir.
    print(numero) #Va a imprimir el resultado con cada iteracion.
    numero *= 2 #El resultado lo va a seguir imprimiendo, hasta que incumpla la condicion inicial.

comando = ""

while comando.lower() != "salir":
    comando = input("$ ")
    print(comando) 


## LOOPS INFINITOS ##

while True:
    comando = input("$ ")
    print(comando) 
    if comando.lower() == "salir": #Agregamos nuestra condicion para que el codigo pueda indentificar cuando acaba
     break #Break para terminarla