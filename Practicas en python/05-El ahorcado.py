import random
import string
from palabrasJuego import palabras
from diagradaAhorcado import vidas_diccionario_visual

def palabraValida(palabras):
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()

def ahorcado():

    print('Bienvenido')

    palabra = palabraValida(palabras)
    
    letras_por_adivinar = set(palabra) #"Set" no permite valores repetidos
    letras_adivinadas = set() #Crea un conjunto vacio
    abecedario = set(string.ascii_uppercase) #Nos trae las letras en mayusculas

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        #mostrar estado de la palabra 

        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        #Mostrar estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        #Mostrar letras separadas x espacio
        print(f"Palabras: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra").upper()
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
        if letra_usuario in letras_por_adivinar:
            letras_por_adivinar.remove(letra_usuario)
            print(' ')
        else:
            vidas = vidas - 1 
            print(f"\nTu letra, {letra_usuario}, no esta en la palabra")