
# Crear el tablero
tablero = {}
for fila in range(5):             # 5 filas
    for columna in range(5):      # 5 columnas
        tablero[(fila, columna)] = "-"  # "-" es el agua


def mostrar_tablero():
    print("0 1 2 3 4")  # Encabezado
    for fila in range(5):
        print(fila, end=" ")  # Número de fila al inicio de la línea
        for columna in range(5):
            print(tablero[(fila, columna)], end=" ")
        print()

mostrar_tablero()