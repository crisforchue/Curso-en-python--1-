nombre_curso = "Ultimate python"
descripcion_curso = """
Ultimate python, 
el curso contempla todos los detalles
que se necesita comprender para encontrar trabajo.
"""

print(nombre_curso, descripcion_curso)

print(len(nombre_curso)) #ver cuantos caracteres tiene un string
print(nombre_curso[1]) #ver caracteres especificos, empiezan a contar desde 0.
print(nombre_curso[0:8]) #Corta los caracteres desde donde indicamos.
print(nombre_curso[9:]) #si no ponemos nada en el segundo indice, llega hasta el final. 
print(nombre_curso[:8]) #si no ponemos nada en el segundo indice, asume el valor por defecto.
print(nombre_curso[:]) #solo imprime toda la palabra ya que asume que el valor por defecto, y llega al final