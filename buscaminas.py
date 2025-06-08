
# buscaminas

import random

matriz = []
for i in range(4):
    vector = []
    for i in range(4):
     vector.append(0)
     matriz.append(vector)

#print(matriz)

# colocando minas pt1.

"""minas = set()
x = random. ((0); cantidad_columnas -1)
y = random. (0; cantidad_filas -1)
minas.append(3,2)
minas.append((3,2))

x = 2
y = 1
append(2;1)
print(minas) """

# creando una clase de minas.

class mapa:
    def __init__( fila, columna):
       

   

# pt2 crear minas.



def generar_minas(self):
   while len(self.minas) < self.cantidad_minas:
      fila = random.randint(0, self.filas -1)
      columna = random.randint(0, self.columnas -1)
      self.minas.add((fila,columna))
      for f, c in self.minas:
       self.tablero[f][c] = "*"

# calculamos el numero de minas cerca del objetivo

def calcular_numeros(self):
  for fila in range(self.filas):
    for columna in range(self.columna):
      if self.tablero[fila][columna] == "*":
        continue
      minas_cerca = 0
      for i in range(-1,2):
        for j in range(-1,2):
          nf, nc = fila + i, columna + j
          if 0  <= nf < self.filas and 0 <= nc < self.columnas:
            if self.tablero[nf][nc] == "*":
              minas_cerca += 1
      self.tablero[fila][columna] = str(minas_cerca) 

def mostrar_tablero(self):
  print(tablero)            
