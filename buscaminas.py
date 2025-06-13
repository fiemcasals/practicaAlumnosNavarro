
import random  # llamamos elementos random.

class Buscaminas:   # defino la clase Buscaminas.
    def __init__(self, filas, columnas, minas):    # constructor el cual tiene sus metodos en ().
        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        self.tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]   # hacemos un tablero con 2 for anidados.
        self.mostrar = [['-' for _ in range(columnas)] for _ in range(filas)]
        self.colocar_minas()
        self.juego_terminado = False   # se declara false, hasta que el jugador pierda el juego.

    def colocar_minas(self):  # con self llamamos el metodo colocar_ minas.
        minas_colocadas = 0
        while minas_colocadas < self.minas:
            fila = random.randint(0, self.filas - 1)   #colocar minas random entre 0 y -1. lo mismo con las columnas.
            columna = random.randint(0, self.columnas - 1)
            if self.tablero[fila][columna] != 'M':   # identifico las minas e el tablero por la letra "M".
                self.tablero[fila][columna] = 'M'
                minas_colocadas += 1 

    def contar_minas_cercanas(self, fila, columna):   # en un perimetro de -1 a +2 se cuentan las minas.
        total = 0
        for i in range(fila - 1, fila + 2):  # el rango de contar_minas_cercanas esta entre esas filas.
            for j in range(columna - 1, columna + 2):  # y esas columnas.
                if 0 <= i < self.filas and 0 <= j < self.columnas: # si el valor de fila y columna es 0, este se le suma un 1. 
                    if self.tablero[i][j] == 'M':   # si no es 0 en ese caso sera una mina.
                        total += 1
        return total

    def descubrir(self, fila, columna):  # al terminar el juego se descubre todo el tablero.
        if self.juego_terminado or self.mostrar[fila][columna] != '-':
            return

        if self.tablero[fila][columna] == 'M':
            self.mostrar[fila][columna] = 'M'
            self.juego_terminado = True     # se declara true, cuando hayas perdido todas tus vidas.
            print(" ¡Pisaste una mina! Fin del juego.")
            self.mostrar_todas()
            return

        minas_cerca = self.contar_minas_cercanas(fila, columna)   # cuenta las minas que hay alrededor 
        self.mostrar[fila][columna] = str(minas_cerca)

        
        if minas_cerca == 0:
            for i in range(fila - 1, fila + 2):   # este seria el rango en el cual cuenta el numero de minas.
                for j in range(columna - 1, columna + 2):  
                    if 0 <= i < self.filas and 0 <= j < self.columnas:
                        self.descubrir(i, j)  #si no hay mias cerca el numero sera 0.

    def mostrar_tablero(self):
        print("   " + " ".join([str(i) for i in range(self.columnas)]))
        for i in range(self.filas):
            print(f"{i:2} " + " ".join(self.mostrar[i]))

    def mostrar_todas(self):
        print("\n--- Tablero completo ---")
        print("   " + " ".join([str(i) for i in range(self.columnas)]))
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                if self.tablero[i][j] == 'M':
                    fila.append('M')
                else:
                    fila.append(str(self.contar_minas_cercanas(i, j)))
            print(f"{i:2} " + " ".join(fila))


# Ejecutar el juego
def jugar():
    juego = Buscaminas(filas=5, columnas=5, minas=5)
    while not juego.juego_terminado:
        juego.mostrar_tablero()
        try:
            fila = int(input("Elige fila: "))
            columna = int(input("Elige columna: "))
            if 0 <= fila < juego.filas and 0 <= columna < juego.columnas:
                juego.descubrir(fila, columna)
            else:
                print("Coordenadas fuera del tablero. Intenta de nuevo.")
        except ValueError:
            print("Por favor ingresa números válidos.")

jugar()
