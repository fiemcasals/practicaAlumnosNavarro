
import random  

intentos = 3        # numero de intentos totales.
respuesta_incorrecta = 1    # cantidad de intentos restantes.
intentos_restantes = intentos

print("bienvenido al juego de matematicas")

numero = random.randint(1,10)     # llamo un numero random.

if intentos_restantes >= 2:
    print("te quedan 2 intentos")    #<>

elif intentos_restantes >= 1:
    print("te queda 1 intento")

elif intentos_restantes >= 3:
    print("tienes todos tus intentos")

else:
    print("perdiste")

seguir_jugando =  input("¿queres jugar otra ronda?: ")
print(seguir_jugando)

problematica = input(f"cuanto es:{numero} + {numero}: ")
mal = input(f"respondiste mal {intentos} - {respuesta_incorrecta}")
 