print("    " + "  ".join([chr(65 + i) for i in range(self.columnas)]))  # A B C D E
        for i, fila in enumerate(self.tablero_visible):
            print(f"{i+1} | " + "  ".join(fila))