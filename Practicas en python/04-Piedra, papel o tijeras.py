import random

def jugar():
    usuario = input("Escoger una opcion. 'pi' para piedra, 'pa' para papel, 'ti' para tijera. \n").lower()

    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora: 
        return "Empate"
    
    if UsuarioGana(usuario, computadora):
        return 'Ganaste'
    
    return 'Perdiste'


    
def UsuarioGana(usuario, oponente):
   ## Casos a considerar ##
   # Piedra gana tijera (pi > ti)
   # Tijera gana papel  (ti > pa)
   # Papel gana piedra (pa > pi)

   if ((usuario == 'pi' and oponente == 'ti') or (usuario == 'ti' and oponente == 'pa') or (usuario == 'pa' and oponente == 'pi')):
       return True
   else:
      return False
   
print(jugar())