import random
import time

def busquedaIngenua(lista, objetivo): 
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i 
    return -1

def busquedaBinaria(lista, objetivo, lim_inferior=None, lim_superior=None):
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
        return busquedaBinaria(lista, objetivo, lim_inferior, punto_medio - 1)
    else: 
        return busquedaBinaria(lista, objetivo, punto_medio + 1, lim_superior)
    
if __name__ == '__main__':
    mi_lista = [1, 2, 3, 4, 5, 6]
    print(busquedaIngenua(mi_lista, 5)) # Imprime el índice 
    print(busquedaBinaria(mi_lista, 5))

    # Crear lista ordenada con 1000 números aleatorios.
    tamano = 20000
    conjuntoIncial = set()

    while len(conjuntoIncial) < tamano:
        conjuntoIncial.add(random.randint(-3*tamano, 3*tamano)) # Selecciona números desde -3000 hasta 3000

    lista = sorted(list(conjuntoIncial))

    # Medir el tiempo de búsqueda ingenua
    inicio = time.time()
    for objetivo in lista: 
        busquedaIngenua(lista, objetivo)
    fin = time.time()
    print(f"Tiempo de búsqueda ingenua: {fin - inicio} segundos")

    # Medir el tiempo de búsqueda binaria
    inicio = time.time()
    for objetivo in lista: 
        busquedaBinaria(lista, objetivo)
    fin = time.time()
    print(f"Tiempo de búsqueda binaria: {fin - inicio} segundos")


