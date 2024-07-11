# and, or, not. 
# and = Cuando tengamos 2 condiciones. Cuandos ambos son True, la expresion completa es True. 
# Or = cuando tengamos 2 condiciones, Cuando una es true, la expresion completa es True.
# Not = negacion del resultado de la operacion. 

gas1 = True 
encendido2 = True 
edad3 = 18

if (not gas1 and encendido2) or edad3 > 17: #Debemos usar () para poder indicar cual de las condiciones van a avanzar primero.
    print("Puedes avanzar.")

## OPERACIONES CORTO CIRCUITO ##

#Las evaluaciones se ejecutan de izquierda a derecha.

gas = True 
encendido = True 
edad = 18

if not gas or encendido or edad > 17: #Debemos usar () para poder indicar cual de las condiciones van a avanzar primero.
    print("Puedes avanzar.")

# Se va a evaluar primeramente la operacion de gas, que al ser falsa, va a pasar a encendido, que es verdadera.
# Esto significa que las evaluaciones son de corto circuito