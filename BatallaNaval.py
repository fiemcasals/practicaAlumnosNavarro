import random  # Importamos para poder usar números aleatorios

# Crear el tablero
tablero = {}
for fila in range(5):             # 5 filas
    for columna in range(5):      # 5 columnas
        tablero[(fila, columna)] = "-"  # "-" es el agua

#posicion random del barco
barco = (random.randint(0, 4), random.randint(0, 4))

#Tablero dibujo
def mostrar_tablero():
    print("0 1 2 3 4")  # Encabezado
    for fila in range(5):
        print(fila, end=" ")  # Número de fila al inicio de la línea
        for columna in range(5):
            print(tablero[(fila, columna)], end=" ")
        print()  # salto al final de cada linea, sin esto quedaba horrible

# 5 intentos
intentos = 5
for intento in range(intentos):
    print(f"\nIntento {intento + 1} de {intentos}")
    mostrar_tablero()

    # Pedimos al jugador que ingrese fila y columna
    try:
        fila = int(input("Elige una fila del 0 al 4: "))
        columna = int(input("Elige una columna del 0 al 4: "))
        tiro = (fila, columna)  #El tiro, fila y columna 

        # Verificamos si acertó
        if tiro == barco: #compara tiro con la posicion del barco, si son iguales entonces acerto
            print("¡Hundido!")
            tablero[tiro] = "X"  # Marca el barco hundido
            break
        else:
            print("Agua...")
            tablero[tiro] = "O"  # Marca que disparó al agua
    except ValueError:
        print("Error, escriba numeros.")
else:
    print(f"\n¡Perdiste! El barco estaba en {barco}")

#Mostrar tablero final
(mostrar_tablero())	
