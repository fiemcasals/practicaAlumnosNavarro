import random

# Para tirar el dado...
def tirar_dado():
    return random.randint(1, 6)

# Para mostrar la posición actual de los jugadores...
def mostrar_posiciones(j1, j2):
    print("-" * 40)
    print(f"Jugador 1: {j1} 🧍" + " ➡ " * j1)
    print(f"Jugador 2: {j2} 🧍" + " ➡ " * j2)
    print("-" * 40)