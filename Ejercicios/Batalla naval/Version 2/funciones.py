import random

def posiciones_aleatorias(): 

  # Creo la siguiente matriz para representar el mar del mapa...
  mar = [
      ["~", "~", "~", "~", "~"],
      ["~", "~", "~", "~", "~"],
      ["~", "~", "~", "~", "~"],
      ["~", "~", "~", "~", "~"],
      ["~", "~", "~", "~", "~"],
  ]

  cant_barcos = 3  # Guardo la cantidad de barcos que van a aparecer en el mapa.
  barco_2y3 = 0  # Creo esta variable para crear 2 barcos que ocupen más espacio.
  pa = 1  # Se utiliza como guía para saber las veces que se hacen posiciones aleatorias.

  while cant_barcos > 0:  # Mientras haya barcos por colocar...

      lista = random.randint(0, 4)  # Fila aleatoria
      posicion_aleatoria = random.randint(0, len(mar[lista]) - 1)  # Columna aleatoria

      print(f"\nB{pa}:") # Para ver la cantidad de veces que se genera una posición aleatoria.
      pa += 1 # Incremento el valor.
      print(" Lista aleatoria:", lista) # Para ver la lista que se eligió aleatoriamente.
      print(" Posición aleatoria:", posicion_aleatoria) # Para ver que posición le toco al barco.

      if mar[lista][posicion_aleatoria] != "~":
          print("\nYa hay un barco en la lista", lista, "posición", posicion_aleatoria)
          continue

      if barco_2y3 == 0:
          mar[lista][posicion_aleatoria] = "B1"
          cant_barcos -= 1
          barco_2y3 += 1

      elif barco_2y3 == 1:
          if posicion_aleatoria > 0 and mar[lista][posicion_aleatoria - 1] == "~":
             mar[lista][posicion_aleatoria] = "B2"
             mar[lista][posicion_aleatoria - 1] = "B2"
             cant_barcos -= 1
             barco_2y3 += 1
          elif posicion_aleatoria < 4 and mar[lista][posicion_aleatoria + 1] == "~":
             mar[lista][posicion_aleatoria] = "B2"
             mar[lista][posicion_aleatoria + 1] = "B2"
             cant_barcos -= 1
             barco_2y3 += 1
          else:
             print("\nNo se pudo colocar barco de tamaño 2")
             continue

      elif barco_2y3 == 2:
          if (
              0 < posicion_aleatoria < 4 and
              mar[lista][posicion_aleatoria - 1] == "~" and
              mar[lista][posicion_aleatoria] == "~" and
              mar[lista][posicion_aleatoria + 1] == "~"
          ):
              mar[lista][posicion_aleatoria - 1] = "B3"
              mar[lista][posicion_aleatoria] = "B3"
              mar[lista][posicion_aleatoria + 1] = "B3"
              cant_barcos -= 1
              barco_2y3 += 1
          else:
              print("\nNo se pudo colocar barco de tamaño 3")
              continue

  # Mostrar el mapa final
  print("\nMapa final:\n")
  for fila in mar:
      print(fila)    

  return mar  # Devuelvo el mapa con los barcos para usarlo en el juego

mar_usuario = [
        [" ","A", "B", "C", "D", "E"],
        ["1","~", "~", "~", "~", "~"],
        ["2","~", "~", "~", "~", "~"],
        ["3","~", "~", "~", "~", "~"],
        ["4","~", "~", "~", "~", "~"],
        ["5","~", "~", "~", "~", "~"],
    ]

# Mostrar el tablero visible al jugador
def mostrar_tablero():
    for fila in mar_usuario:
        print(fila)

# Para convertir las letras A-E en número de columna...
def letra_a_col(letra):
    letras = {"A":0, "B":1, "C":2, "D":3, "E":4}
    return letras.get(letra.upper(), -1)  