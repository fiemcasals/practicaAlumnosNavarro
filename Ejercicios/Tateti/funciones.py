# Creo la siguiente función para mostrar el tablero...
def mostrar_tablero(tablero):
    print(" ")
    print("  A   B   C") # Los nombres de cada columna.
    for i, fila in enumerate(tablero): # Enumera cada lista de la matrix para poder representar cada fila.
        # El método join convierte la lista de la fila en un string con separadores...
        print(f"{i+1} " + " | ".join(fila)) # Imprime el numero de fila junto con cada separador de columna.
        if i < 2: # Mientras que la numeración de cada fila sea menor a 2 se imprime el separador de cada fila...
            print("  ---------")
    print(" ")

# Creo la siguiente función para pedirle el movimiento al jugador...
def pedir_movimiento(tablero, jugador): 
    while True: # Todo lo que sigue se va a imprimir porque siempre va a ser verdadero...
        entrada = input(f"Turno de {jugador} (ej. A1): ").upper().strip()
        # input: Le pide al jugador que ingrese un valor.
        # f: Permite insertar valores de variables dentro del texto usando {}.
        # upper(): Convierte el valor que ingresa el usuario en mayúsculas.
        # strip(): Se utiliza por si el usuario agrega espacios al valor que ingreso.

        # Si la longitud de lo que ingreso el usuario es lo contrario de 2 no es valida la entrada...
        if len(entrada) != 2: 
            print("Entrada inválida. Usa formato como A1, B2.")
            continue # Vuelve al while True.
        
        # Se guardan los dos primeros caracteres que ingresa el jugador...
        columna = entrada[0] 
        fila = entrada[1]    

        # Si el jugador no ingreso estos valores las coordenadas están fuera de rango...
        if columna not in "ABC" or fila not in "123": 
            # Se niega que el jugador coloque coordenadas de "ABC" en columna y lo mismo con fila que niega valores como "123".
            print("Coordenadas fuera de rango.")
            continue # Vuelve al while True.

        f = int(fila) - 1 # Guardo en esta variable el valor de fila convertida en entero y restada en 1.
        # Se utiliza el siguiente método para agregarle posiciones a cada carácter del string y compararlo con lo que ingreso el jugador...
        c = "ABC".index(columna) 

        # Si lo que esta en esta posición del tablero es lo contrario a una casilla con espacio devuelve que esta ocupada.
        if tablero[f][c] != " ": 
            print("Esa casilla ya está ocupada.")
            continue # Vuelve al while True.

        return f, c # Devuelve la posición de la fila y de la columna.

        # creo la siguiente función para verificar quien fue el ganador...
        def verificar_ganador(tablero, jugador):
              # Filas, columnas y diagonales
               for i in range(3):
                if all(tablero[i][j] == jugador for j in range(3)): return True # all pregunta si el jugador dio en una de las tres (f y c)...
                if all(tablero[j][i] == jugador for j in range(3)): return True # si completo las tres  retorna true.

                if all(tablero[i][i] == jugador for i in range(3)): return True
                if all(tablero[i][2 - i] == jugador for i in range(3)): return True

                return False # vuelve a verificar_ganador

        # creo  una función para verificar el empate...
        def es_empate(tablero): 
          return all(tablero[i][j] != " " for i in range(3) for j in range(3)) # si ninguno de los jugadores  completo las (f y c) se declara empate. 

        # lógica básica del juego... 
        tablero = [[" " for _ in range(3)] for _ in range(3)]
        jugador_actual = "X" 

        while True:  # Todo lo que sigue se va a imprimir porque siempre va a ser verdadero...
         mostrar_tablero(tablero)  # llama a la función tablero.
         fila, columna = pedir_movimiento(tablero, jugador_actual) # pide el movimiento al jugador actual.
         tablero[fila][columna] = jugador_actual 

         if verificar_ganador(tablero, jugador_actual): # verifica si el jugador gano... 
          mostrar_tablero(tablero)
          print(f"\n🎉 ¡El jugador {jugador_actual} ha ganado!")
          break

         if es_empate(tablero): # si hubo un empate
          mostrar_tablero(tablero)
          print("\n🤝 ¡Empate!")
          break

          # Cambiar de jugador
          jugador_actual = "O" if jugador_actual == "X" else "X" # el usuario selecciona que jugador es (0 , X).
