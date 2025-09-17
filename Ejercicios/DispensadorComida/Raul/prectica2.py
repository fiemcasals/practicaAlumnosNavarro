
"""
Enunciados de los 4 ejercicios recursivos que se desarrollan mas abajo script:



1. 🔢 Suma de elementos de una lista

Enunciado:
Implementar una función recursiva que reciba una lista de números y devuelva la suma total de sus elementos.
No se permite el uso de funciones iterativas ni funciones auxiliares como sum().

Ejemplo esperado:
suma_lista([1, 2, 3, 4]) → 10



2. 🧮 Contar elementos en una lista

Enunciado:
Definir una función recursiva que reciba una lista y devuelva la cantidad de elementos que contiene.
No se permite usar la función len() para contar elementos.

Ejemplo esperado:
contar_elementos([10, 20, 30, 40]) → 4



3. 🔁 Invertir una lista

Enunciado:
Escribir una función recursiva que reciba una lista y retorne una nueva lista con los mismos elementos en orden inverso.
No se permite utilizar ciclos ni funciones como reversed().

Ejemplo esperado:
invertir_lista([1, 2, 3]) → [3, 2, 1]



4. 🔤 Verificar si una palabra es palíndromo

Enunciado:
Crear una función recursiva que determine si una cadena de texto es un palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda).
No se permite invertir la cadena con slicing ni usar funciones auxiliares.

Ejemplos esperados:
es_palindromo("reconocer") → True
es_palindromo("hola") → False

"""


#1...

def suma_lista(lista):
    # Caso base: si la lista está vacía, su suma es 0
    if not lista:
        return 0
    # Paso recursivo: sumar el primer elemento y llamar recursivamente con el resto
    return lista[0] + suma_lista(lista[1:])

suma_lista([1, 2, 3, 4])
1 + suma_lista([2, 3, 4])
1 + 2 + suma_lista([3, 4])
1 + 2 + 3 + suma_lista([4])
1 + 2 + 3 + 4 + suma_lista([])
print(suma_lista([1, 2, 4, 2]))

#2...

def contar_elementos(lista):
    # Caso base: lista vacía tiene 0 elementos
    if not lista:
        return 0
    # Paso recursivo: contar 1 y seguir con el resto
    return 1 + contar_elementos(lista[1:])


contar_elementos([10, 20, 30, 40])
1 + contar_elementos([20, 30, 40])
1 + 1 + contar_elementos([30, 40])
1 + 1 + 1 + contar_elementos([40])
1 + 1 + 1 + 1 + contar_elementos([])
4

#3...

def invertir_lista(lista):
    # Caso base: lista vacía o de un solo elemento ya está invertida
    if len(lista) <= 1:
        return lista
    # Paso recursivo: poner el primer elemento al final de la inversión del resto
    return invertir_lista(lista[1:]) + [lista[0]]


invertir_lista([1, 2, 3])
invertir_lista([2, 3]) + [1]
(invertir_lista([3]) + [2]) + [1]
print(invertir_lista)

#4...

def es_palindromo(palabra):
    if len(palabra) <= 1:  # Caso base: una letra o palabra vacía
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

es_palindromo("reconocer")
palabra[0] = 'r', palabra[-1] = 'r' 
llamada con "econoce"
palabra[0] = 'e', palabra[-1] = 'e' 


es_palindromo("hola")
palabra[0] = 'h', palabra[-1] = 'a' 