import random

# crear tablero vacio
def crear_tablero():
    # crea un diccionario vacio llamado tablero
    tablero = {}
    # recorre las filas del 1 al 5
    for fila in range(1, 6):
        # recorre las columnas de la A a la E
        for col in "ABCDE":
            # crea una clave en el diccionario tipo "A1" y le asigna como valor un espacio " " que indica que esta vacia
            tablero[f"{col}{fila}"] = " "
    return tablero


# Colocar barcos aleatoriamente
# recibe dos parametros:
# tablero: un diccionario
# cantidad: cuantos barcos queres colocar, puse 3
def colocar_barcos(tablero, cantidad=3):
    # elige al azar cantidad de posiciones del tablero para colocar los barcos
    # tablero.keys() obtiene todas las coordenadas 
    # list() convierte esas claves en una lista
    # random.sample() selecciona sin repetir cantidad de elementos de esa lista
    posiciones = random.sample(list(tablero.keys()), cantidad)
    # recorre cada posicion seleccionada y le asigna "B" en el tablero que es de "barco"
    for pos in posiciones:
        tablero[pos] = "B"  
    return posiciones


# mostrar tablero al jugador (sin mostrar los barcos)
# mostrar_barcos: es un parametro opcional que por defecto es False
# si esta en False, los barcos "B" se ocultan al imprimir el tablero
def mostrar_tablero(tablero, mostrar_barcos=False):  
    # muestra el encabezado de las columnas con letras de la A a la E
    print("  A B C D E")
    # comienza un bucle que recorre las filas del 1 al 5
    for fila in range(1, 6):
        # crea una linea de texto que empieza con el número de la fila actual para alinear los datos visualmente como un tablero
        linea = str(fila) + " "
        # dentro de cada fila, este segundo bucle recorre las columnas A hasta E
        for col in "ABCDE":
            #  calcula la clave del diccionario para esa celda y guarda el valor actual de esa celda (puede ser " ", "B", "X", "O")
            valor = tablero[f"{col}{fila}"]
            # si la celda tiene un barco y mostrar_barcos es False, no lo muestra; en lugar de "B" imprime un espacio vacio " "
            if valor == "B" and not mostrar_barcos:
                linea += " "  # ocultar barco
            # si no hay un barco o si se permite mostrar los barcos, se agrega el valor real de esa celda a la linea
            else:
                linea += valor
                # se añade un espacio para separar las columnas visualmente
            linea += " "
        print(linea)

# Disparo del jugador
def disparar(tablero, posicion):
    # si el jugador escribe una coordenada que no existe en el tablero (por ejemplo "Z9"), devuelve un mensaje diciendo que la coordenada es invalida
    if posicion not in tablero:
        return "¡Coordenada inválida!"
    # si en esa posicion hay un barco ("B"), se marca con una "X" para indicar que fue impactado y se devuelve un mensaje que dice "¡Le diste a un barco!"
    if tablero[posicion] == "B":
        tablero[posicion] = "X"  # X = barco acertado
        return "¡Le diste a un barco!"
    # si en esa posicion no hay nada significa que el disparo fue al agua. Se marca con una "O" y se devuelve el mensaje "Fallaste, solo agua."
    elif tablero[posicion] == " ":
        tablero[posicion] = "O"  # O = agua
        return "Fallaste, solo agua."
    # si en esa posicion ya habia una "X" o una "O", significa que el jugador ya disparo ahi antes, y el juego le avisa con "Ya disparaste aqui."
    elif tablero[posicion] in ["X", "O"]:
        return "Ya disparaste aquí."

# esta funcion se usa para verificar si todavía quedan barcos sin destruir en el tablero
def quedan_barcos(tablero):
    return "B" in tablero.values()

# esta funcion inicia y controla todo el juego
def jugar():
    tablero = crear_tablero()
    barcos = colocar_barcos(tablero)
    intentos = 0
    print("¡Bienvenido a Batalla Naval!")
    print("Debes encontrar los 3 barcos escondidos.\n")

    # Mientras queden barcos vivos, se repite el juego
    while quedan_barcos(tablero):
        # muestra el tablero actualizado, ocultando los barcos (mostrar_barcos=False por defecto)
        mostrar_tablero(tablero)
        # se le pide al usuario una coordenada (como "B2")
        #.upper() convierte todo a mayúsculas (por si el jugador escribe "a1" en minúscula)
        disparo = input("Ingresa una coordenada (ejemplo A3): ").upper()
        #llama a la funcion disparar para ver si fue acierto, agua, ya usado o invalido
        resultado = disparar(tablero, disparo)
        print(resultado)
        # cada disparo cuenta como un intento, aciertes o no
        intentos += 1
        print()

    # muestra un mensaje de victoria y cuantos disparos necesitaste
    print("¡Felicidades, hundiste todos los barcos!")
    print(f"Lo lograste en {intentos} intentos.")
    # se vuelve a imprimir el tablero, pero esta vez mostrando todas las posiciones de los barcos
    print("Así estaba el tablero:")
    mostrar_tablero(tablero, mostrar_barcos=True)

# Ejecutar el juego
jugar()
