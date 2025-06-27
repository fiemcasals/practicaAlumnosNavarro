import funciones

# variables iniciales
meta = 30
posicion_jugador1 = 0
posicion_jugador2 = 0

# Bucle principal del juego
# . Repetir turnos hasta que uno de los dos llegue a la meta.
# . Alternar turnos y sumar el dado a la posición.
while True:
    input("\nTurno Jugador 1 - presiona ENTER para tirar el dado\n")
    dado1 = funciones.tirar_dado()
    posicion_jugador1 += dado1
    print(f"  Jugador 1 sacó un {dado1}\n")

    if posicion_jugador1 >= meta:
        print("🎉 ¡Jugador 1 ha ganado la carrera!\n")
        break

    input("Turno Jugador 2 - presiona ENTER para tirar el dado\n")
    dado2 = funciones.tirar_dado()
    posicion_jugador2 += dado2
    print(f"  Jugador 2 sacó un {dado2}\n")

    if posicion_jugador2 >= meta:
        print("🎉 ¡Jugador 2 ha ganado la carrera!\n")
        break

    funciones.mostrar_posiciones(posicion_jugador1, posicion_jugador2)
