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
"""matriz = [
    [1, 2, 3], [4, 5, 6],[7, 8, 9]
    
]"""

# Recorremos la matriz con dos for anidados
"""for fila in matriz:
    for elemento in fila:
        print(elemento)
"""

#n! = n × (n-1) × (n-2) × ... × 1



"""def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado"""

# Ejemplo
"""print(factorial_iterativo(3))  # Resultado: 120

def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

# Ejemplo
print(factorial_recursivo(3))  # Resultado: 120
"""

"""class CalculadoraFactorial:
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        resultado = 1
        for i in range(1, self.numero + 1):
            resultado *= i
        return resultado"""

for numero in range(5):
    print(numero)