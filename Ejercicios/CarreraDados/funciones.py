import random

# Para tirar el dado...
def tirar_dado():
    return random.randint(1, 6) # Retorno el valor del dado.

# Para mostrar la posición actual de los jugadores...
def mostrar_posiciones(j1, j2):
    print("-" * 40) # Separador.
    # Dependiendo del valor de dado que le toque a cada jugador en cada ronda se Iran suman igual que las barras..
    print(f"Jugador 1: {j1} 🧍" + " ➡ " * j1) 
    print(f"Jugador 2: {j2} 🧍" + " ➡ " * j2)
    print("-" * 40) # Separador.