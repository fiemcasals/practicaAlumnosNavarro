import random # Se llama a la librería.

puntos_jugador = 30 # Se define la variable con su valor.
jugar = "s" # Esta variable se creo para que se ejecute el while.

print("\n________________________________________________________________________")
print("\nBienvenido al juego de operaciones matemáticas.")
print("Empezás con 30 puntos. Si llegás a 50 ganás y si bajás de 0, perdés.")

while puntos_jugador >= 0 and puntos_jugador <= 50 and jugar == "s": # Si estos 3 dan True me ejecuta lo siguiente...

    num1 = random.randint(1, 10) # Declaro una variable para que guarde el primer numero aleatorio.
    num2 = random.randint(1, 10) # Aca utilizo este método para generar un numero aleatorio entre 1 y 10.

    operacion = random.choice(["+", "-", "*", "/"]) # Aca utilizo este método para que devuelva aleatoriamente algunos de esos caracteres.

    if operacion == "+": # Si el carácter aleatorio es igual a este se ejecuta lo siguiente...

        resultado = num1 + num2  # Declaro esta variable para guardar el resultado de la operación realizada.

        print(f"\n  ¿Cuánto es {num1} {operacion} {num2}?\n") # Aca imprime el ejercicio a resolver.
        respuesta = float(input("    Tu respuesta: ")) # Aca en esta variable se guarda la respuesta del jugador en formato flotante.

        if respuesta == resultado: # Si la respuesta del jugador es igual al resultado del ejercicio se ejecuta lo siguiente...
            print("\n      Correcto, sumaste 5 puntos.\n")
            puntos_jugador += 5 # Se incrementan los puntos del jugador.
        elif respuesta != resultado: # Si la respuesta del jugador es contraria al resultado del ejercicio me devuelve lo siguiente...
            print("\n      Es incorrecto, se te restaron 5 puntos.\n")
            puntos_jugador -= 5 # Se le restan los puntos al jugador.
        else:
            print("\n      Error.")

    elif operacion == "-":

        resultado = num1 - num2  

        print(f"\n  ¿Cuánto es {num1} {operacion} {num2}?\n")
        respuesta = float(input("    Tu respuesta: "))

        if respuesta == resultado:
            print("\n      Correcto, sumaste 5 puntos.\n")
            puntos_jugador += 5
        elif respuesta != resultado:
            print("\n      Es incorrecto, se te restaron 5 puntos.\n")
            puntos_jugador -= 5
        else:
            print("\n      Error.")

    elif operacion == "*":

        resultado = num1 * num2  

        print(f"\n  ¿Cuánto es {num1} {operacion} {num2}?\n")
        respuesta = float(input("    Tu respuesta: "))

        if respuesta == resultado:
            print("\n      Correcto, sumaste 5 puntos.\n")
            puntos_jugador += 5
        elif respuesta != resultado:
            print("\n      Es incorrecto, se te restaron 5 puntos.\n")
            puntos_jugador -= 5
        else:
            print("\n      Error.\n")

    elif operacion == "/":

        resultado = num1 / num2  # así la división es exacta

        print(f"\n  ¿Cuánto es {num1} {operacion} {num2}?\n")
        respuesta = float(input("    Tu respuesta: "))

        if respuesta == resultado:
            print("\n      Correcto, sumaste 5 puntos.\n")
            puntos_jugador += 5
        elif respuesta != resultado:
            print("\n      Es incorrecto, se te restaron 5 puntos.\n")
            puntos_jugador -= 5
        else:
            print("\n      Error.\n")                            
    
    if puntos_jugador < 0: # Una vez que termina de resolver el ejercicio se verifica si el jugador tiene menos de 0 puntos.
        print("¡  Perdiste!\n")
    elif puntos_jugador > 50: # Aca verifica si tiene mas de 50 puntos.
        print("  ¡Ganaste!\n")
    else:    
        jugar = input("¿Querés seguir jugando otra ronda? (s/n): ") # Si el jugador no cumple ninguna de las condiciones anteriores se le pregunta si quiere seguir jugando.


print("\nTus puntos son:", puntos_jugador,"\n") # Una vez que termina el while imprime el puntaje final del jugador.
print("\n________________________________________________________________________\n")