import random

print("Bienvenido al juego Batalla Naval")

while True:
    tablero = []
    for i in range(5):
        fila = []
        for j in range(5):
            fila.append("🌊")
        tablero.append(fila)

    barcos_restantes = 3
    while barcos_restantes > 0:
        fila = random.randint(0, 4)
        columna = random.randint(0, 4)
        if tablero[fila][columna] != "⛵":
            tablero[fila][columna] = "⛵"
            barcos_restantes -= 1
    visible = []
    for i in range(5):
        visible.append(["🌊"] * 5)

    intentos = 5
    barcos_hundidos = 0

    while intentos > 0 and barcos_hundidos < 3:
        print("\nTablero:")
        for fila in visible:
            print(" ".join(fila))

        try:
            fila = int(input("Ingresa la fila (1-5): ")) - 1
            columna = int(input("Ingresa la columna (1-5): ")) - 1

            if not (0 <= fila < 5 and 0 <= columna < 5):
                print("Coordenadas fuera de rango. Intenta de nuevo.")
                continue
        except ValueError:
            print("Entrada inválida. Ingresa números del 1 al 5.")
            continue

        if visible[fila][columna] != "🌊":
            print("Ya intentaste esa posición. Prueba otra.")
            continue

        if tablero[fila][columna] == "⛵":
            print("¡Hundiste un barco!")
            visible[fila][columna] = "❌"
            barcos_hundidos += 1
        else:
            print("Agua.")
            visible[fila][columna] = "⭕"

        intentos -= 1
    print("\nTablero final:")
    for fila in visible:
        print(" ".join(fila))

    if barcos_hundidos == 3:
        print("🎉 ¡Ganaste! Hundiste todos los barcos.")
    else:
        print("🚫 ¡Se acabaron los intentos PERDISTE!")
    print("\nUbicación de los barcos:")
    for i in range(5):
        fila_mostrada = []
        for j in range(5):
            if tablero[i][j] == "⛵":
                fila_mostrada.append("⛵")
            else:
                fila_mostrada.append("🌊")
        print(" ".join(fila_mostrada))

    jugar = input("\n¿Quieres jugar de nuevo? (si/no): ").lower()
    if jugar != "si":
        break

print("¡Gracias por jugar!")
