class DispensadorComida:
    def __init__(self, capacidad, nombre_mascota):
        # Atributos
        self.nombre_mascota = nombre_mascota   # Atributo público
        self._nivel_comida = capacidad         # Atributo protegido
        self.__clave_seguridad = "1234"        # Atributo privado
    
    # Método público
    def servir_comida(self, cantidad):
        if cantidad <= self._nivel_comida:
            self._nivel_comida -= cantidad
            print(f"Sirviendo {cantidad}g de comida a {self.nombre_mascota}.")
        else:
            print("No hay suficiente comida. Recargar.")
    
    # Método público
    def recargar(self, cantidad, clave):
        if clave == self.__clave_seguridad:
            self._nivel_comida += cantidad
            print(f"Recargado con {cantidad}g de comida. Nivel actual: {self._nivel_comida}g.")
        else:
            print("Clave incorrecta. No se puede recargar.")

    # Método protegido
    def _estado(self):
        return f"Nivel de comida: {self._nivel_comida}g"


# --- Uso de la clase correctamente ---
dispensador = DispensadorComida(1000, "Firulais")

# Ver estado actual
print(dispensador._estado())

# Servir comida dos veces
dispensador.servir_comida(150)
dispensador.servir_comida(100)

# Intentar recargar sin clave (esto fallará)
dispensador.recargar(200, "0000")  # Clave incorrecta

# Recargar con clave correcta
dispensador.recargar(200, "1234")  # Clave correcta

# Ver estado final
print(dispensador._estado())

