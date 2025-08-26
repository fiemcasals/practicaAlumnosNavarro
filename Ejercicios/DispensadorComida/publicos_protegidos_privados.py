class DispensadorComida:
    def __init__(self, capacidad, nombre_mascota):
        # Atributos
        self.nombre_mascota = nombre_mascota   # Atributo público (accesible desde fuera)
        self._nivel_comida = capacidad         # Atributo protegido (solo debería usarse dentro o subclases)
        self.__clave_seguridad = "1234"        # Atributo privado (no accesible directamente desde fuera)
    
    # Método público
    def servir_comida(self, cantidad):
        if cantidad <= self._nivel_comida:
            self._nivel_comida -= cantidad
            print(f"Sirviendo {cantidad}g de comida a {self.nombre_mascota}.")
        else:
            print("No hay suficiente comida. Recargar.")
    
    # Método público
    def recargar(self, cantidad, clave):
        if clave == self.__clave_seguridad:  # accede al atributo privado
            self._nivel_comida += cantidad
            print(f"Recargado con {cantidad}g de comida. Nivel actual: {self._nivel_comida}g.")
        else:
            print("Clave incorrecta. No se puede recargar.")

    # Método protegido (normalmente para uso interno o subclases)
    def _estado(self):
        return f"Nivel de comida: {self._nivel_comida}g"

dispensador = DispensadorComida(1000, 120)

dispensador._estado()     # muestra la cantidad actual

dispensador.servir_comida()  # dispensar otra ración
dispensador.recargar(200) # recargar 200g
dispensador.estado()     # mostrar estado final