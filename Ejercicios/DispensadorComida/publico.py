# paso1_publicos.py

class Dispensador:
    def __init__(self, capacidad_total, racion):
        # Atributos PÚBLICOS
        self.capacidad_total = capacidad_total   # capacidad máxima del depósito (g)
        self.cantidad_actual = capacidad_total   # empieza lleno
        self.racion = racion                     # gramos por dispensado

    def dispensar(self):
        if self.cantidad_actual >= self.racion:
            self.cantidad_actual -= self.racion
            print(f"\nServido {self.racion}g. Quedan {self.cantidad_actual}g.\n")
        else:
            print("No alcanza la comida para servir.")

    def recargar(self, cantidad):
        self.cantidad_actual += cantidad
        print(f"Recargado {cantidad}g. Ahora hay {self.cantidad_actual}g.\n")

    def estado(self):
        print(f"{self.cantidad_actual}/{self.capacidad_total}g disponibles.\n")

dispensar1 = Dispensador(1000,120) # Le indico que la capacidad maxima va a ser de 1000 gramos y que la ración va a ser de 120g.

dispensar1.dispensar()
dispensar1.recargar(100)
dispensar1.estado()

# --- Prueba rápida ---
#if __name__ == "__main__":
    #d = Dispensador(1000, 120)
    #d.estado()          # 1000/1000 g
    #d.dispensar()       # 120 g -> 880 g
    #d.racion = 500      # 👈 cambiás la ración desde fuera (público)
    #d.dispensar()       # 500 g -> 380 g
    #d.capacidad_total = 200  # 👈 incluso podés romper la capacidad (público)
    #d.estado()          # 380/200 g (inconsistente, pero permitido en este paso)
