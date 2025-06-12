import random

numeroSecreto = random.randrange(0,50)

intentos=5

print("Usted deberá adivinar un número del 0 al 50, para ello tendrá 5 intentos")

while True:
    numeroUsuario = int(input("Ingrese un número del 1 al 50:"))
    if numeroUsuario<numeroSecreto:
        intentos = intentos - 1
        print("El número ingresado es menor al número secreto. Intente nuevamente. \n"f"Le quedan {intentos} intentos.")
        #numeroUsuario = int(input("Ingrese un número del 1 al 50:"))
        if intentos==0:
            print("Usted se ha quedado sin intentos.\n""EL JUEGO HA FINALIZADO.")
            break
    elif numeroUsuario>numeroSecreto:
        intentos = intentos - 1
        print("El número ingresado es mayor al número secreto. Intente nuevamente. \n"f"Le quedan {intentos} intentos.")
        #numeroUsuario = int(input("Ingrese un número del 1 al 50:"))
        if intentos==0:
            print("Usted se ha quedado sin intentos.\n""EL JUEGO HA FINALIZADO.")
            break
    else:
        print(f"Felicidades, el número era {numeroSecreto}, ha ganado el juego" )
        break

