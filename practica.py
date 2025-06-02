#mesas = 2
#sillas = 3

#Wif mesas in sillas ({sillas}):
      #for mesas in range(3):
        #print(mesas)
#elif sillas in mesas(3 + 2):
     #for sillas in range(2):
        # print (sillas)        


#Actividad práctica: Suma de números introducidos por el usuario
#Ahora, te propongo una actividad para practicar el uso del bucle for:

#Enunciado:

#Escribe un programa que:

#Pregunte cuántos números se van a introducir.

#Pida esos números (que pueden ser decimales) y calcule su suma.

#Pista: Puedes utilizar la función input() para obtener datos del usuario y la función float() para convertir esos datos en números decimales.
#import random

#numero = random.randint(1,10)




#print(sumatoria)

# practiquemos

#saludo = "hola"
#bienvenida = saludo
#print  (bienvenida)

# Creamos una matriz de 3x3 (3 filas, 3 columnas)
matriz = [
    [1, 2, 3], [4, 5, 6],[7, 8, 9]
    
]

# Recorremos la matriz con dos for anidados
for fila in matriz:
    for elemento in fila:
        print(elemento)
