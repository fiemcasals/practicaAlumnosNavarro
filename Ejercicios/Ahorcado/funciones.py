# _________________________ Funciones...

def mostrar_estado(estado): # creo una función para mostrar el estado de la palabra.
    print("\n"," ".join(estado),"\n")  # 

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