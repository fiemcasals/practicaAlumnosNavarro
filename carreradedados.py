
import random

puntos_usuario = 0
puntos_computadora = 0
turno = 1

def tirar_dado():
    # Simula el lanzamiento de un dado de 6 caras
    return random.randint(1, 6)

def juego_carrera_dados():
    print(" Bienvenido al juego de carrera de dados")
    objetivo = int(input("🏁 Ingresa la puntuación objetivo para ganar: "))

    

    while puntos_usuario < objetivo and puntos_computadora < objetivo:
        print(f"\n Turno {turno}")
        input("Presiona Enter para lanzar tu dado...")

        # Turno del usuario
        dado_usuario = tirar_dado()
        puntos_usuario += dado_usuario
        print(f" Tiraste un {dado_usuario}. Tu total: {puntos_usuario}")

        if puntos_usuario >= objetivo:
            print(" ¡Felicidades! ¡Ganaste la carrera de dados! ")
            break

        # Turno de la computadora
        print("\nAhora le toca a la computadora...")
        dado_computadora = tirar_dado()
        puntos_computadora += dado_computadora
        print(f" La computadora tiró un {dado_computadora}. Total: {puntos_computadora}")

        if puntos_computadora >= objetivo:
            print("\nLa computadora ganó la carrera. ¡Suerte la próxima vez!")
            break

        turno += 1

    print("\n Fin del juego ")

# Ejecutar el juego
juego_carrera_dados()
