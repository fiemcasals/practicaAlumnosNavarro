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

def rango_numerico(numero_inicial, numero_final):

    divisible7no_5 = []

    for i in range(numero_final):

        if numero_inicial % 7 == 0: # Resto

            if numero_inicial % 5 == 0:
                numero_inicial += 1
                continue
            elif numero_inicial % 5 != 0:
                divisible7no_5.append(numero_inicial)
                numero_inicial += 1
            else:
                 print("Error en el condicional 'Divisible por 5'.")    

        elif numero_inicial % 7 != 0:
               numero_inicial += 1
               continue
        else:
             print("Error en el condicional 'Divisible por 7'.")

    separador_coma = ",".join(str(n) for n in divisible7no_5)          

    print(f"\nLo números divisibles por 7 y no por 5 son: {separador_coma}.\n")

    # for a in divisible7no_5: print("",a) # Imprime linea por linea.

rango_numerico(1, 100)    