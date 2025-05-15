
import random

disparar = - 1 
tamaño = 5   # cantidad de barcos
mapa = map(5)  # Crea un mapa de tamaño 5x5
(mapa)


def crear_mapa (tamaño):     # crear el mapa de juego
  return[["~" for _ in range(tamaño)] for _ in range(tamaño)]
  


def mostrar_mapa(mapa):   
  print("  " + " ".join(str(i) for i in range(len(mapa[0]))))
  for idx, fila in enumerate(mapa):
        print(str(idx) + " " + " ".join("~" if celda == "b" else celda for celda in fila))
            


    






