import funciones

# Genera posiciones aleatorias para los barcos en el mapa...
print("\n_____________________________ Generando posiciones aleatorias para los barcos en el mapa.... _____________________________")
funciones.posiciones_aleatorias()

print("\n_____________________________ Pidiéndole datos al usuario.... _____________________________\n")

mar_usuario = [
      [" ","A", "B", "C", "D", "E"],
      ["1","~", "~", "~", "~", "~"],
      ["2","~", "~", "~", "~", "~"],
      ["3","~", "~", "~", "~", "~"],
      ["4","~", "~", "~", "~", "~"],
      ["5","~", "~", "~", "~", "~"],
]

for fila in mar_usuario:
    print(fila)

posicion_elegida = input("\nIngrese una posición del mapa que se muestra en pantalla:\n")