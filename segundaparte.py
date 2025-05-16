
import random # llama un numero random


def crear_mapa():   # defino la funcion crear_mapa 
  return [["-" for _ in range(5)]  # uso return para retornar a la funcion crear_mapa
          for _ in range(5)]  
  
def mostrar_mapa(mapa):   #  llamo a la funcion mostrar mapa.
     print("1 2 3 4 5")   #  imprimo los numeros. 
     letras = ["A", "B", "C", "D", "E"]    #  variable de letras de la A a E.
     for i in range(5):   # llamo valores del 0 al 5.  
        fila = letras[i] + " " + " ".join(mapa[i])   # creo la variable de fila y con la i muestra el indice de mapa.
        print(fila) # Imprime la fila.


def convertir_coordenada(coordenada):    # convierte las coordenadas en posiciones para los barcos.
    letras = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}    #  posibles coordenadas desde A0 hasta E4.
    fila = letras.get(coordenada[0].upper(), -1)    # letras.get llama el valor de letras y coordenada, luego resta 1 para que las posiciones sean 5.
    try:
        columna = int(coordenada[1]) - 1
    except:
        columna = -1
    return fila, columna


