print("Bienvenido a la calculadora")
print("Para salir, escribe \"SALIR\"")

print("Las operaciones disponibles son suma, resta, multiplicacion, division.")
print("Que operacion quiere realizar?")

resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese numero: ")
        if resultado.upper() == "salir":
            break
        resultado = int(resultado)
    op = input("ingresa operacion: ")
    if op.upper() == "salir": 
        break

    n2 = input("Ingresa siguiente numero: ")
    if n2.upper() == "salir": 
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multiplicacion":
        resultado *= n2
    elif op.lower() == "division":
        resultado /= n2
    else: 
        print("Operacion no valida")
        break

print(f'El resultado es {resultado}')