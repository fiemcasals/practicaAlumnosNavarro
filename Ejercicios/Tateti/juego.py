import funciones

# Creo el tablero vació...
# El primer for me crea una lista con tres elementos " " (Vector). 
# Y el segundo for me crea 3 listas iguales que la anterior adentro de una lista (Matrix).
# tablero = [[" " for _ in range(3)] for _ in range(3)] 

# print(tablero) 

# Muestro el tablero...
# funciones.mostrar_tablero(tablero)

# FIJARME PORQUE EL JUGADOR 'X' TIENE 2 OPORTUNIDADES DE JUEGO!...

# Lógica básica del juego... 
tablero = [[" " for _ in range(3)] for _ in range(3)]
jugador_actual = "X" 

while True:  # Bucle principal del juego
    funciones.mostrar_tablero(tablero)  # Muestra el tablero
    fila, columna = funciones.pedir_movimiento(tablero, jugador_actual)  # Pide el movimiento al jugador actual
    tablero[fila][columna] = jugador_actual  # Marca el tablero con el símbolo del jugador

    if funciones.verificar_ganador(tablero, jugador_actual):  # Verifica si ganó el jugador
        funciones.mostrar_tablero(tablero)
        print(f"\n🎉 ¡El jugador {jugador_actual} ha ganado!\n")
        break

    if funciones.es_empate(tablero):  # Verifica si hubo empate
        funciones.mostrar_tablero(tablero)
        print("\n🤝 ¡Empate!")
        break

    # Cambiar de jugador
    jugador_actual = "O" if jugador_actual == "X" else "X"  # Alterna entre "X" y "O"