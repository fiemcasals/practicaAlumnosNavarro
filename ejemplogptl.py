
import random

# Crear un mapa vacío de 5x5
def crear_mapa():
    return [["~" for _ in range(5)] for _ in range(5)]

# Mostrar el mapa al jugador
def mostrar_mapa(mapa):
    print("  1 2 3 4 5")
    letras = ["A", "B", "C", "D", "E"]
    for i in range(5):
        fila = letras[i] + " " + " ".join(mapa[i])
        print(fila)

# Convertir coordenadas como "A3" en posiciones [0][2]
def convertir_coordenada(coordenada):
    letras = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
    fila = letras.get(coordenada[0].upper(), -1)
    try:
        columna = int(coordenada[1]) - 1
    except:
        columna = -1
    return fila, columna

# Colocar 3 barcos aleatoriamente en el mapa
def colocar_barcos():
    barcos = []
    while len(barcos) < 3:
        fila = random.randint(0, 4)
        columna = random.randint(0, 4)
        if (fila, columna) not in barcos:
            barcos.append((fila, columna))
    return barcos

# Juego principal
def jugar():
    mapa = crear_mapa()
    barcos = colocar_barcos()
    intentos = 0
    aciertos = 0
    print("¡Bienvenido a Batalla Naval!")
    print("Tienes que encontrar 3 barcos escondidos en un mapa de 5x5 (A-E, 1-5).")

    while aciertos < 3:
        mostrar_mapa(mapa)
        entrada = input("Ingresa una coordenada (Ej: A3): ")
        fila, columna = convertir_coordenada(entrada)

        if fila == -1 or columna < 0 or columna > 4:
            print(" Coordenada inválida. Intenta de nuevo.")
            continue

        if mapa[fila][columna] != "~":
            print(" Ya tiraste ahí. Intenta en otro lugar.")
            continue

        intentos += 1

        if (fila, columna) in barcos:
            print(" ¡Le diste a un barco!")
            mapa[fila][columna] = "X"
            aciertos += 1
        else:
            print(" Agua...")
            mapa[fila][columna] = "O"

    print("¡Ganaste! Hundiste los 3 barcos en", intentos, "intentos.")
    mostrar_mapa(mapa)

# Ejecutar el juego
jugar()

            


    






