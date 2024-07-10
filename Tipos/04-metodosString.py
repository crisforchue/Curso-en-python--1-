animal = "  Perrito FEliz  "

#Metodos que cambian nuestro formato dependiendo de lo que se pida.
#Los metodos se pueden encadenar
print(animal.upper())
print(animal.lower()) 
print(animal.capitalize())
print(animal.title())
print(animal.strip())
print(animal.lstrip())
print(animal.rstrip())
print(animal.strip().capitalize()) #encadenado
print(animal.find("z")) #Nos devuelve la poscision
print(animal.replace("Pe", "j"))
print("Pe" in animal)
print("Pe" not in animal)