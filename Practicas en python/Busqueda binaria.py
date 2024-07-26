import random
import time

def busquedaIngenua(lista, objetivo): 
    for i in range (len(lista)):
        if lista[i] == objetivo:
            return i 
    return -1

list = [1, 2, 3, 4, 5, 6]
print(busquedaIngenua(list, 5)) #Imprime el indice 

def busquedaBinaria(lista, objetivo, lim_inferior=None,lim_superior=None):
    if lim_inferior is None:
        lim_inferior = 0
    if lim_superior is None:
        lim_superior = len(lista) - 1

    if lim_superior < lim_inferior: 
        return -1
    
    punto_medio = (lim_inferior + lim_superior) // 2

    if lista[punto_medio] == objetivo: 
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busquedaBinaria(lista, objetivo, lim_inferior, punto_medio-1)
    else: 
        return busquedaBinaria(lista, objetivo, punto_medio+1,)