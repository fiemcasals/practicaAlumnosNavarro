import random

# _________________________ Funciones...

def mostrar_estado(estado): # creo una función para mostrar el estado de la palabra.
    print(" ".join(estado))  # 

def pedir_letra():  #pido al jugador que ingrese una letra...
    while True: # lo sigue siempre sera true.
        letra = input("Ingresa una letra: ").lower()   # con lower paso todo a minuscula para evitar 
        if len(letra) != 1 or not letra.isalpha():
            print("Debes ingresar solo una letra.")
        else:
            return letra

def actualizar_estado(palabra, estado, letra):
    acierto = False
    for i, l in enumerate(palabra):
        if l == letra:
            estado[i] = letra
            acierto = True
    return acierto

def palabra_completa(estado):
    return "_" not in estado

# _________________________    

palabras = ["python", "ahorcado", "programacion", "computadora", "juego"]

palabra_secreta = random.choice(palabras)

estado_actual = ["_" for _ in palabra_secreta]

letras_adivinadas = []
intentos_restantes = 6  # clásico en ahorcado

while intentos_restantes > 0 and not palabra_completa(estado_actual):
    mostrar_estado(estado_actual)
    print("Letras adivinadas:", ", ".join(letras_adivinadas))
    print("Intentos restantes:", intentos_restantes)
    
    letra = pedir_letra()
    
    if letra in letras_adivinadas:
        print("Ya intentaste con esa letra.")
        continue

    letras_adivinadas.append(letra)

    if not actualizar_estado(palabra_secreta, estado_actual, letra):
        intentos_restantes -= 1
        print("Letra incorrecta.")

if palabra_completa(estado_actual):
    print("\n🎉 ¡Ganaste! La palabra era:", palabra_secreta)
else:
    print("\n💀 ¡Perdiste! La palabra era:", palabra_secreta)