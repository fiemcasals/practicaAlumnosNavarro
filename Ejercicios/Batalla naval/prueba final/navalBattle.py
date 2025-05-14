from funciones import posiciones_aleatorias, mostrar_tablero, letra_a_col, mar_usuario

# Mapa interno (oculto) con los barcos
mar_barcos = posiciones_aleatorias()



# Juego principal
print("\n¡Bienvenido a la Batalla Naval!\n")
mostrar_tablero()

intentos = 10
aciertos = 0
total_barcos = sum(f.count("B1") + f.count("B2") + f.count("B3") for f in mar_barcos)

while intentos > 0 and aciertos < total_barcos:
    pos = input(f"\nIntento {11 - intentos}/10 - Ingrese posición (ej: B3): ").upper()
    if len(pos) != 2 or pos[0] not in "ABCDE" or pos[1] not in "12345":
        print("\nEntrada inválida. Use formato letra+numero (ej: C4)\n")
        continue

    col = letra_a_col(pos[0])
    fila = int(pos[1]) - 1

    if mar_usuario[fila + 1][col + 1] != "~":
        print("\nYa probaste esa posición.\n")
        continue

    if mar_barcos[fila][col] != "~":
        print("\n¡ACIERTO! 🚢\n")
        mar_usuario[fila + 1][col + 1] = "X"
        aciertos += 1
    else:
        print("\nAGUA 🌊\n")
        mar_usuario[fila + 1][col + 1] = "O"

    mostrar_tablero()
    intentos -= 1

# Resultado final
if aciertos == total_barcos:
    print("\n¡FELICIDADES! Hundiste todos los barcos. 🏆\n")
else:
    print("\nJuego terminado. No hundiste todos los barcos.\n")
    print("\nPosiciones reales:")
    for fila in mar_barcos:
        print(fila)
    print("\n")