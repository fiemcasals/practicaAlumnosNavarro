
import random # llama un numero random


def crear_mapa():   # defino la funcion crear_mapa 
  return [["~" for _ in range(5)] for _ in range(5)]  # uso return para 
  
  

print("ingresa una coordenada a la que quieras disparar: " )

coordenada = input("disparo(letra+numero): ")

letra = coordenada[0]

columna = int(coordenada[1])

fila = ubicacion.get(letra, -1)

if fila == -1 or columna < 0 or columna > 4:
  print("error")
elif print("le diste"):
     mapa [fila][columna] = "x"
else:
  print("agua.")
  mapa[fila][columna] = "0"

mapa = [
      [" ","A", "B", "C", "D", "E"],
      ["1","~", "~", "~", "~", "~"],
      ["2","~", "~", "~", "~", "~"],
      ["3","~", "~", "~", "~", "~"],
      ["4","~", "~", "~", "~", "~"],
      ["5","~", "~", "~", "~", "~"],
  ]

for fila in mapa:
    print(fila)
    


for i in range(3) :
mapa: list[list[]] [random.randint(0,4)]
random.choice(tamaño_barcos)

for j in range(3) :
 mapa = [random.randint(0,4)]
random.choice(tamaño_barcos)

if tamaño_barcos[i] == 1:
 mapa[i][j] = 1

elif tamaño_barcos [i] == 2:
  matriz[i][j] = 1
  mapa[i+1][j+1] = 2 
 
print("mapa actual: ") 
for i, fila_m in enumerate(mapa):

 print(f"{list(ubicacion.values)()[0]}{fila_m}")   

   

for i in range(5):
    dic[i] = {
       0 : { "a" : "agua"}, 
       1 : { "b" : "agua"}, 
       2 : { "c" : "agua"}, 
       3 : { "d" : "barco"},
       4 : { "e" : "agua"}

   }



for i in dic:
   for j in dic[i]:
    print(dic[i][j], end=" ")
print()     

