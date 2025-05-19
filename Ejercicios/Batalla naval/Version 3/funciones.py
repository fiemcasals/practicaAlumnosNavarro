
# ______________________________________________________ CREAR MAPA ______________________________________________________

mapa = {} # Defino el mapa fuera de la función para utilizar el mapa en las siguientes funciones...
indices = ["Columnas","A","B","C","D","E"]

# Se crea el mapa de juego...
def crear_mapa():
  
  # Le digo que voy a modificar o utilizar el global de las siguientes variables.
  global indices
  global mapa
  mapa = {} # Defino el diccionario del mapa vació.

  # El siguiente for lo utilizo para ir agregando listas vacías a cada clave del diccionario.
  for i in indices:
    mapa[i] = []
  
  # El siguiente for se utiliza para ir cambiando de claves.
  for a in range(1,6):
    # Este for se utiliza para ir agregando los 5 símbolos de "~" a cada clave.
    for b in range(1,6):
     mapa[indices[a]].append("~")

    mapa["Columnas"].append(a) # Aca le agrego a esta lista los números de cada columna.
  
crear_mapa() # Muestro el mapa.

# ______________________________________________________ REPRESENTAR MAPA ______________________________________________________

def representar_mapa(mapa):

  global indices
  
  print("\n")
  # Lo siguiente se hace para representar mejor los números de cada columna...
  print("   ", mapa["Columnas"][0], "  ", mapa["Columnas"][1], "  ", mapa["Columnas"][2], "  ", mapa["Columnas"][3], "  ", mapa["Columnas"][4]) 

  # El siguiente for se utiliza para representar las letras de cada fila con sus listas.
  indice = 1 
  for c in indices[1:]:
    print(indices[indice], ":", mapa[c],sep = "")
    indice += 1

  print("\n")  

representar_mapa(mapa)    

# ______________________________________________________ DISPARAR ______________________________________________________

def disparar():

  global mapa # Utilizo el mapa global

  posicion_usuario = input("  Ingrese una posición (Por ejemplo 'C4'):") # Le pido al usuario que ingrese un valor...

  clave = posicion_usuario[0]
  valor = int(posicion_usuario[1])

  if (clave == "A" or clave == "B" or clave == "C" or clave == "D" or clave == "E") and (valor > 0 and valor < 6):
    mapa[clave][valor-1] = "X"
    representar_mapa(mapa)
  else:
    print("\n")
    print("    Agrego algo incorrecto, vuelva a indicar entra A y E, y entre 1 y 5 (Por ejemplo 'C4').")
    print("\n")
    disparar()

disparar()    