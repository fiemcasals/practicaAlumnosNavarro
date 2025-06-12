# importar funciones de funcionesBatallaNaval.py
from funciones_batalla_naval import crear_tablero, mostrar_tablero, colocar_barco_aleatorio, colocar_barco, disparar, verificar_ganador, disparar_aleatorio

while True:
    print("Bienvenido a la Batalla Naval")
    print("1. Jugar contra otro jugador")
    print("2. Jugar contra la máquina")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")
    if opcion == '1':
        print("Jugador 1, coloca tus barcos.")
        print("Si desea colocar su barco manualmente presione 1")
        print("Si desea colocar su barco aleatoriamente presione 2")
        opcionJugador1 = int(input("Selecciona una opción: "))
        if opcionJugador1 == 1:
            tableroJugador1 = crear_tablero(5)
            colocar_barco(tableroJugador1)
        elif opcionJugador1 == 2:
            tableroJugador1 = crear_tablero(5)
            colocar_barco_aleatorio(tableroJugador1)
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            continue
        print("Jugador 2, coloca tus barcos.")
        print("Si desea colocar su barco manualmente presione 1")
        print("Si desea colocar su barco aleatoriamente presione 2")
        opcionJugador2 = int(input("Selecciona una opción: "))
        if opcionJugador1 == 1:
            tableroJugador2 = crear_tablero(5)
            colocar_barco(tableroJugador2)
        elif opcionJugador2 == 2:
            tableroJugador2 = crear_tablero(5)
            colocar_barco_aleatorio(tableroJugador2)
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            continue
        
        while True:
            print("Turno del Jugador 1:")
            mostrar_tablero(tableroJugador1)
            fila = int(input("Ingresa la fila (0-5): "))
            columna = int(input("Ingresa la columna (0-5): "))
            disparar(tableroJugador2, fila, columna)
            if verificar_ganador(tableroJugador2):
                print("¡Jugador 1 ha ganado!")
                break
            
            print("Turno del Jugador 2:")
            mostrar_tablero(tableroJugador2)
            fila = int(input("Ingresa la fila (0-5): "))
            columna = int(input("Ingresa la columna (0-5): "))
            disparar(tableroJugador1, fila, columna)
            if verificar_ganador(tableroJugador1):
                print("¡Jugador 2 ha ganado!")
                break

    elif opcion == '2':
        print("Jugador 1, coloca tus barcos.")
        print("Si desea colocar su barco manualmente presione 1")
        print("Si desea colocar su barco aleatoriamente presione 2")
        opcionJugador1 = int(input("Selecciona una opción: "))
        if opcionJugador1 == 1:
            tableroJugador1 = crear_tablero(5)
            colocar_barco(tableroJugador1)
        elif opcionJugador1 == 2:
            tableroJugador1 = crear_tablero(5)
            colocar_barco_aleatorio(tableroJugador1)
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            continue
        print("La Máquina va a colocar sus barcos...")
        tableroMaquina = crear_tablero(5)
        colocar_barco_aleatorio(tableroMaquina)

        while True:
            print("Turno del Jugador :")
            mostrar_tablero(tableroMaquina)
            fila = int(input("Ingresa la fila (0-5): "))
            columna = int(input("Ingresa la columna (0-5): "))
            disparar(tableroMaquina, fila, columna)
            if verificar_ganador(tableroMaquina):
                print("¡Jugador 1 ha ganado!")
                break
            
            print("Turno de la Máquina:")
            disparar_aleatorio(tableroJugador1)
            if verificar_ganador(tableroJugador1):
                print("¡La Máquina ha ganado!")
                break

    else:
        print("Saliendo del juego. ¡Hasta luego!")
        break
   


  


    
    