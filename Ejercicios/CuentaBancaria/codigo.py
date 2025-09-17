from __future__ import annotations # Permite referirse a clases no definidas. Ej usar el objeto Nodo en la clase Nodo.
from abc import ABC, abstractmethod # Para definir clases y métodos abstractos (interfaces).
from typing import List, Dict # Tipado de listas y diccionarios #List[Dict]:

# ===========================================
# 1) Cuenta bancaria con @property + setter
# ===========================================

class CuentaBancaria:
    """
    Cuenta bancaria simple con balance protegido, deposito y extracción.
    """
    def __init__(self,titular_cuenta: str, saldo_inicial: float = 0.0) -> None:
        self._titular = titular_cuenta # Atributo protegido.
        self._saldo = 0.0 # Inicializa saldo en cero.
        self.saldo = saldo_inicial # Usa el setter para validar saldo.

        @property
        def titular(self) -> str:
            return self._titular # Getter del titular
        
        @property
        def saldo(self) -> float:
            """Saldo disponible. No puede ser negativo."""
            return self._saldo # Getter del saldo.