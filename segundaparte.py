
import random # llama un numero random


def crear_mapa():   # defino la funcion crear_mapa 
  return [["-" for _ in range(5)]  # uso return para retornar a la funcion crear_mapa
          for _ in range(5)]  
  
def mostrar_mapa(mapa):   #  llamo a la funcion mostrar mapa.
     print("1 2 3 4 5")   #  imprimo los numeros. 
     letras = ["A", "B", "C", "D", "E"]    #  variable de letras de la A a E.
     for i in range(5):   # llamo valores del 0 al 5.  
        fila = letras[i] + " " + " ".join(mapa[i])   # creo la variable de fila y con la i muestra el indice de mapa.
        print(fila) # Imprime la fila.


def convertir_coordenada(coordenada):    # convierte las coordenadas en posiciones para los barcos.
    letras = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}    #  posibles coordenadas desde A0 hasta E4.
    fila = letras.get(coordenada[0].upper(), -1)    # letras.get llama el valor de letras y coordenada.
    try:                                            # si hay un error, el programa continua.
        columna = int(coordenada[1]) - 1            # se resta 1 para que las posiciones sean 5.
    except:                                         # mientras except maneja el error para evitar el fallo del programa.
        columna = -1
    return fila, columna                            # ante un error retornamos a la fila o columna.


def colocar_barcos():       # colocamos los barcos de forma aleatoria.
    barcos = []                 # variable de barcos.
    while len(barcos) < 3:          # con len contamos la cantidad de barcos.
        fila = random.randint(0, 4)   # selecciona una fila random del 0 al 4.
        columna = random.randint(0, 4)   # selecciona una columna random del 0 al 4.
        if (fila, columna) not in barcos:     #  fila y columna,les decimos  que no estan en barcos.
            barcos.append((fila, columna))     # se agrega a barcos en la lista (fila,columnas).
    return barcos       # retornamos a barcos. 

# menu principal del juego 
def jugar():     # defino la variable jugar.
    mapa = crear_mapa()   # el mapa es la función crear_mapa.
    barcos = colocar_barcos()   # se muestra la ubicacion de sus barcos. 
    intentos = 0    # numero de intentos restantes.
    aciertos = 0    # cantidad de aciertos en barcos.
    print("¡Bienvenido a Batalla Naval!")   # bienvenida.
    print("Tienes que encontrar 3 barcos escondidos en un mapa de 5x5 (A-E, 1-5).")   # info del juego.

while aciertos < 3:  # cantidad de aciertos, menor a 3.
        mostrar_mapa(mapa)    # muestra mapa al usuario. 
        entrada = input("Ingresa una coordenada (Ej: A3): ")    # le dice al usuario que ingrese una coordenada para tirar a uno de los barcos.
        fila, columna = convertir_coordenada(entrada)     # llama a la funcion convertir_coordenada, para leer la seleccion del usuario.



        if fila == -1 or columna < 0 or columna > 4:    # que el numero seleccionado no sea mayor a 4 o igual a 0.
            print(" Coordenada inválida. Intenta de nuevo.")     
            continue     # si hay un error, vuelve a ejecutar el while. 

        if mapa[fila][columna] != "~":    # muestra el mapa  la posicion en la que tiraste y la marca con "~"
            print(" Ya tiraste ahí. Intenta en otro lugar.")
            continue

        intentos += 1   # defino la variable sumar un intento tras fallar.

        if (fila, columna) in barcos:    # llama a (fila y columna) en barcos.
            print(" ¡Le diste a un barco!")    
            mapa[fila][columna] = "X"   # se marca en el mapa con una x al barco que le diste.
            aciertos += 1      # se suma un acierto al jugador.
        else:         # si le das al agua.
            print(" Agua...")   
            mapa[fila][columna] = "O"   # si le das al agua se marca con un 0.

        print("¡Ganaste! Hundiste los 3 barcos en", intentos, "intentos.")   # al ganar se muestran la cantidad de intentos que utilizaste. 
        mostrar_mapa(mapa)    # muestra el mapa con los resultados del jugador. 


        jugar()            