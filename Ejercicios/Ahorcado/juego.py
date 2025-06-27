import random
import funciones

# _________________________    

palabras = ["python", "ahorcado", "programacion", "computadora", "juego"]

palabra_secreta = random.choice(palabras)

estado_actual = ["_" for _ in palabra_secreta]

letras_adivinadas = []
intentos_restantes = 6  # clásico en ahorcado

while intentos_restantes > 0 and not funciones.palabra_completa(estado_actual):
    funciones.mostrar_estado(estado_actual)
    print("Letras adivinadas:", ", ".join(letras_adivinadas))
    print("Intentos restantes:", intentos_restantes)
    
    letra = funciones.pedir_letra()
    
    if letra in letras_adivinadas:
        print("Ya intentaste con esa letra.")
        continue

    letras_adivinadas.append(letra)

    if not funciones.actualizar_estado(palabra_secreta, estado_actual, letra):
        intentos_restantes -= 1
        print("Letra incorrecta.")

if funciones.palabra_completa(estado_actual):
    print("\n🎉 ¡Ganaste! La palabra era:", palabra_secreta)
else:
    print("\n💀 ¡Perdiste! La palabra era:", palabra_secreta)