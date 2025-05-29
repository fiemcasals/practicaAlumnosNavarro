import random

def crear_tablero(tamano):
    tablero = []
    for i in range(tamano):
        fila = [] 
        for c in range(tamano):
            fila.append('~')
        tablero.append(fila)
    return tablero

def mostrar_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))
    print()

def colocar_barco_aleatorio(tablero):
    print("Desplegando flota...")
    fila = random.randint(0, 5)
    columna = random.randint(0, 5)
    if tablero[fila][columna] == '~':
        tablero[fila][columna] = 'B'
        return True
    else:
        print("Ya hay un barco en esa posición.")
        return False 
    
def colocar_barco(tablero):
    print("Despliegue su flota")
    fila = int(input("Ingresa la fila (0-5): "))
    columna = int(input("Ingresa la columna (0-5): "))
    if tablero[fila][columna] == '~':
        tablero[fila][columna] = 'B'
        return True
    else:
        print("Ya hay un barco en esa posición.")
        return False 
    
def disparar(tablero, fila, columna):   
    print("Prepáre cañones...")
    if tablero[fila][columna] == 'B':
        tablero[fila][columna] = 'X'
        print("¡PUM!")
        return True
    elif tablero[fila][columna] == '~':
        tablero[fila][columna] = 'O'
        print("Agua:(")
        return False
    else:
        print("Ya has disparado a esa posición.")
        return False
    
def disparar_aleatorio(tablero):
    print("Preparando cañones...")
    fila = random.randint(0, 5)
    columna = random.randint(0, 5)
    if tablero[fila][columna] == 'B':
        tablero[fila][columna] = 'X'
        print("¡PUM!")
        return True
    elif tablero[fila][columna] == '~':
        tablero[fila][columna] = 'O'
        print("Agua:(")
        return False
    else:
        print("Ya has disparado a esa posición.")
        return False
    
def verificar_ganador(tablero):
    for fila in tablero:
        if 'B' in fila:
            return False
    return True

def turno_jugador(tablero_oponente):
    print("Turno del jugador:")
    mostrar_tablero(tablero_oponente)
    fila = int(input("Ingresa la fila (0-5): "))
    columna = int(input("Ingresa la columna (0-5): "))
    disparar(tablero_oponente, fila, columna)

def turno_oponente(tablero_jugador):
    print("Turno del oponente:")
    mostrar_tablero(tablero_jugador)
    fila = int(input("Ingresa la fila (0-5): "))
    columna = int(input("Ingresa la columna (0-5): "))
    disparar(tablero_jugador, fila, columna)

def turno_maquina(tablero_jugador):
    print("Turno del oponente:")
    mostrar_tablero(tablero_jugador)
    fila = random.randint(0, 5)
    columna = random.randint(0, 5)
    disparar(tablero_jugador, fila, columna)

