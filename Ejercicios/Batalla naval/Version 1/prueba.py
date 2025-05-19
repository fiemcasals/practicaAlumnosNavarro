import random

# Creo la siguiente matriz para representar el mar del mapa...
mar = [
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
]

cant_barcos = 3  # Guardo la cantidad de barcos que van a aparecer en el mapa.
barco_2y3 = 0  # Creo esta variable para crear 2 barcos que ocupen más espacio.
pa = 1  # Se utiliza como guía para saber las veces que se hacen posiciones aleatorias.

while cant_barcos > 0: # Si la cantidad de barcos es mayor a 0...

    lista = random.randint(0, 4) # Genero un numero aleatorio para indicar luego la lista aleatoria.
    posicion_aleatoria = random.randint(0, len(mar[lista]) - 1) # Genero la posición aleatoria

    # Lo siguientes print se utilizan para saber los datos de cada posición aleatoria que se generan...
    print("\nB", pa, ":", sep="")
    pa += 1 
    print("\n Lista aleatoria:", lista)
    print(" Posición aleatoria:", posicion_aleatoria)

    if mar[lista][posicion_aleatoria] == "B": # Si en la posición aleatoria hay barco...
        print("Ya hay un barco en la lista", lista, "posición", posicion_aleatoria)
        continue  # Volver al inicio del while sin decrementar.

    if barco_2y3 == 0: # Si el tamaño del barco es de 1 posición...
        mar[lista][posicion_aleatoria] = "B1" # Se agrega el barco en esa posición.

    elif barco_2y3 == 1: # Si el barco ocupa 2 posiciones...
        # Si no hay barco en las siguiente posición aleatoria y su valor es mayor a 0 se agregan los barcos...
        if posicion_aleatoria > 0 and mar[lista][posicion_aleatoria - 1] == "~":
            mar[lista][posicion_aleatoria] = "B2"
            mar[lista][posicion_aleatoria - 1] = "B2"
        # Si la posicion aleatoria es menor a 4 y no tiene barco, se agregan.
        elif posicion_aleatoria < 4 and mar[lista][posicion_aleatoria + 1] == "~":
            mar[lista][posicion_aleatoria] = "B2"
            mar[lista][posicion_aleatoria + 1] = "B2"
        else: # De lo contrario no se puede agregar el barco y se vuelve a ejecutar el while.
            print("No se pudo colocar barco de tamaño 2")
            barco_2y3 -= 1
            continue

    elif barco_2y3 == 2: # Si el tamaño del barco es de 3 posiciones...
        # Si los valores de las posiciones aleatorias están entre el siguiente rango y no tienen barco...
        if (
            posicion_aleatoria > 0 and posicion_aleatoria < 4 and # Se agregan los rangos para que no se desfase el barco en la lista.
            mar[lista][posicion_aleatoria - 1] == "~" and
            mar[lista][posicion_aleatoria] == "~" and
            mar[lista][posicion_aleatoria + 1] == "~"
        ):
            mar[lista][posicion_aleatoria - 1] = "B3"
            mar[lista][posicion_aleatoria] = "B3"
            mar[lista][posicion_aleatoria + 1] = "B3"
        else:
            print("\nNo se pudo colocar barco de tamaño 3")
            barco_2y3 -= 1
            continue

    cant_barcos -= 1
    barco_2y3 += 1

# Mostrar el mapa final
print("\n")
for a in mar:
    print(a)
print("\n")