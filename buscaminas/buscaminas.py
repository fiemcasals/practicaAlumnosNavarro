import random

class buscaminas:
    def __init__(self, filas, columnas, cantidad_minas):
        self.filas = filas
        self.columnas = columnas
        self.cantidad_minas = cantidad_minas
        self.tablero = [['0' for _ in range(columnas)] for _ in range(filas)]
        self.visible = [['#' for _ in range(columnas)] for _ in range(filas)]
        self.minas = set() # Usamos un set para evitar duplicados
        self.generar_minas()
        self.calcular_numeros()

    def generar_minas(self):
        while len(self.minas) < self.cantidad_minas:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            self.minas.add(fila, columna) # Aseguramos que no haya duplicados
        for fila, columna in self.minas:
            self.tablero[fila][columna] = '*' # Marcamos las minas en el tablero

    def calcular_numeros(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if self.tablero[fila][columna] == '*':
                    continue
                minas_cerca = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        numero_filas, numero_columnas = fila + i, columna + j
                        if 0 <= numero_filas < self.filas and 0 <= numero_columnas < self.columnas:
                            if self.tablero[numero_filas][numero_columnas] == '*':
                                minas_cerca += 1
                self.tablero[fila][columna] = str(minas_cerca)

    def mostrar_tablero(self):
        pass

