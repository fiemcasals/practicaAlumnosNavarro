class DispensadorComida:
    def __init__(self, capacidad, nombre_mascota):
        # Atributos
        self.nombre_mascota = nombre_mascota   # Público (accesible desde fuera)
        self._nivel_comida = capacidad         # Protegido (solo debería usarse dentro o subclases)
        self.__clave_seguridad = "1234"        # Privado (no accesible directamente desde fuera)
    
    # Método público
    def servir_comida(self, cantidad): # Le agrego la cantidad que quiero servirle a la mascota...
        if cantidad <= self._nivel_comida: 
            self._nivel_comida -= cantidad
            print(f"------------------------------------------------------------------------------")
            print(f"\nSirviendo {cantidad}g de comida a {self.nombre_mascota}.\n")
        else:
            print(f"------------------------------------------------------------------------------")
            print("\nNo hay suficiente comida. Recargar!.\n")
    
    # Método privado
    def recargar(self, cantidad, clave):
        if clave == self.__clave_seguridad:  # accede al atributo privado
            self._nivel_comida += cantidad
            print(f"\nRecargado con {cantidad}g de comida. Nivel actual: {self._nivel_comida}g.\n")
            print(f"------------------------------------------------------------------------------")
        else:
            print(f"------------------------------------------------------------------------------")
            print("\nClave incorrecta. No se puede recargar.\n")

    # Método protegido (normalmente para uso interno o subclases)
    def _estado(self):
        print(f"------------------------------------------------------------------------------")
        print(f"\nNivel de comida: {self._nivel_comida}g\n")

dispensador = DispensadorComida(1000, "Doggy")

dispensador._estado()     # muestra la cantidad actual

dispensador.servir_comida(200)  # dispensar otra ración

dispensador._estado()     # muestra la cantidad actual

#dispensador.recargar(200,"1234") # recargar 200g