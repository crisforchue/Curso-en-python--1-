punto = {"X": 25, "y": 50} #Esto es un diccionario.
print(punto) 

print(punto["X"]) #Se debe usar este formato para llegar a los datos, ya que no funcionan como listas. 
punto["Z"] = 45. #Estos nos agrega un elemento a nuestro diccionario. 

print(punto.get("x")) #Nos va a dar el valor que queremos buscar segun la llave. 
print(punto.get("Lala", 0)) #Como este string no existe, se nos va a presentar un valor por defecto (valor en el segundo argumento)

for valor in punto:
    print(valor, punto[valor]) #Nos va a dar valores de los diccionarios en forma de iterable.

for valor in punto.items(): #Nos va a devolver el diccionario a modo de tuplas
    print(valor)

## Practica de usuarios ## 
usuarios = [
    {"id": 1, "nombre": "Heavens"},
    {"id": 2, "nombre": "Jeez"},
    {"id": 3, "nombre": "Weichi"}
]

for usuario in usuarios: 
    print(usuario["nombre"])
