import random

class Buscaminas:

    def __init__(self, filas=5, columnas=5): # Defino en el constructor los valores por defecto de las filas y columnas.
        self.filas = filas
        self.columnas = columnas
        self.tablero_real = [["0" for _ in range(self.columnas)] for _ in range(self.filas)] # Crear tablero real con "0"
        self.tablero_visible = [["#" for _ in range(self.columnas)] for _ in range(self.filas)] # Creo el tablero
        self.colocar_minas()  # <<--- Colocar minas al inicializar
        self.calcular_numeros()

    def mostrar_tablero(self):

        '''Lo siguiente me imprime una filas con los nombres de cada columna utilizando el método chr()
        para ir aumentando su valor con el for y me vaya agregando cada carácter correspondiente y luego
        utilizo el join() para separar entre espacios cada carácter.
        '''
        print("    " + "  ".join([chr(65 + i) for i in range(self.columnas)]))  # A B C D E
        for i, fila in enumerate(self.tablero_visible):
            print(f"{i+1} | " + "  ".join(fila))

    def colocar_minas(self, cantidad_minas=5):

      # Colocar minas aleatoriamente
      minas_colocadas = 0
      while minas_colocadas < cantidad_minas:
          
          fila = random.randint(0, self.filas - 1)
          columna = random.randint(0, self.columnas - 1)

          if self.tablero_real[fila][columna] != "*":
              self.tablero_real[fila][columna] = "*"
              minas_colocadas += 1

    def mostrar_tablero_real(self):
      print("    " + "  ".join([chr(65 + i) for i in range(self.columnas)]))
      for i, fila in enumerate(self.tablero_real):
        print(f"{i+1} | " + "  ".join(fila))

    def calcular_numeros(self):
      for fila in range(self.filas):               # Recorre todas las filas
          for col in range(self.columnas):         # Recorre todas las columnas
              if self.tablero_real[fila][col] == "*":  # Si la casilla actual es una mina
                  continue                            # No se hace nada, se salta
              # Contar minas alrededor
              minas_alrededor = 0  # Inicializa contador de minas cercanas
              for i in range(-1, 2):       # Recorre filas vecinas: -1, 0, 1
                 for j in range(-1, 2):   # Recorre columnas vecinas: -1, 0, 1
                   if i == 0 and j == 0:
                      continue  # Salta la casilla central (la actual)
                   nf, nc = fila + i, col + j  # Calculamos la posición vecina

                   # Verificamos que la posición vecina esté dentro de los límites del tablero
                   if 0 <= nf < self.filas and 0 <= nc < self.columnas:
                      if self.tablero_real[nf][nc] == "*":
                          minas_alrededor += 1  # Si hay una mina en la vecina, sumamos al contador

              # Guardamos el número total de minas vecinas en la casilla actual (como string)
              self.tablero_real[fila][col] = str(minas_alrededor)

    def descubrir(self, fila, columna):
      # Si la casilla contiene una mina
      if self.tablero_real[fila][columna] == "*":
        self.tablero_visible[fila][columna] = "*"
        self.mostrar_tablero()
        print("\n💥 ¡BOOM! Pisaste una mina. Juego terminado.\n")
      else:
        # Mostrar el valor en el tablero visible (un número)
        self.tablero_visible[fila][columna] = self.tablero_real[fila][columna]
          
buscaminas1 = Buscaminas()

print("\nTablero visible:\n")
buscaminas1.mostrar_tablero()

print("\nTablero real con minas:\n")
buscaminas1.mostrar_tablero_real()

print("\nTablero visible descubierto:\n")
buscaminas1.descubrir(2,3)
buscaminas1.mostrar_tablero()

# ()