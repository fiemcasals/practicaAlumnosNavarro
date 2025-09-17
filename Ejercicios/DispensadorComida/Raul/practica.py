
""". Escribir  una  función  que  reciba  como  parámetros  el  inicio  y  fin  (inclusive)  de  un  rango  numérico.  La 
función debe: 
a. Imprimir en pantalla todos aquellos números que sean divisibles por 7 pero no sean divisibles 
por 5.  
b. Imprimir el mismo resultado anterior, pero separados por coma. 
 
Resultado Esperado: Por ejemplo, si se invoca con los parámetros 1 y 100 (puntos a y b) 
 7 
14 
21 
28 
42 
49 
56 
63 
77 
84 
91 
98 
 
7,14,21,28,42,49,56,63,77,84,91,98"""

def ingreseNum(mensaje):
    return int(input(mensaje))

def saludoMasReglas():
    print("debe ingresar un rango y el programa le dara numeros segun el enunciado")

saludoMasReglas()
num_menor= ingreseNum("ingrese un numero menor: ")
num_mayor= ingreseNum("ingrese un numero mayor: ")

def funcionDivSieteNoCinco(num_mayor, num_menor):
    """
    Esta función recibe dos números y devuelve una lista de números dentro de ese rango
    que son divisibles por 7 pero no por 5.
    """
    lista = []
    for i in range(num_menor, num_mayor + 1):
        if i % 7 == 0 and i % 5 != 0:
            lista.append(i)
    return lista

vectorDeNumero = funcionDivSieteNoCinco(num_mayor, num_menor)

def imprimirVector(valor):
    """
    Esta función imprime los números de la lista en la consola.
    """
    print("\nLos números divisibles por 7 pero no por 5 son:\n")
    if valor:
        for i in vectorDeNumero:
            print(i)
    else:
        for i in vectorDeNumero:
            print(i, end=" ")
        print("\n")


imprimirVector(int(input("ingrese 1 si lo quiere uno debajo del otro, o 0 si lo quiere uno al lado del otro: ")))







