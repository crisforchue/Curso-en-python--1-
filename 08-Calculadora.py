n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))

print(n1, n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

#Para que las variables entre {} funcionen es necesario agregar "f"
#Para indicar el uso de funciones.

mensaje = f""" 
Para los numeros {n1} y {n2},
El resultado de la suma es {suma}
El resultado de la resta es {resta}
El resultado de la multiplicacion es {multiplicacion} 
El resultado de la division es {division}
"""
print(mensaje)