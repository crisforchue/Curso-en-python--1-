## INTENTO HECHO ##

print("Bienvenido a la calculadora")
print("Para salir, escribe \"SALIR\"")

print("Las operaciones disponibles son suma, resta, multiplicacion, division.")
print("Que operacion quiere realizar?")


Primer_Numero = int(input("Ingrese un numero: "))
Segundo_Numero = int(input("Ingrese otro numero: "))

suma = Primer_Numero + Segundo_Numero
resta = Primer_Numero - Segundo_Numero
multiplicacion = Primer_Numero * Segundo_Numero
division = Primer_Numero / Segundo_Numero

print(f"El resultado de la suma es {suma}")
print(f"El resultado de la resta es {resta}")
print(f"El resultado de la multiplicacion es {multiplicacion}")
print(f"El resultado de la division es {division}")