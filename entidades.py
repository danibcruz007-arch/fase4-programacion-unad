# ============================================================
# Archivo: entidades.py
# Descripción: Clase abstracta base para entidades del sistema.
# ============================================================

from abc import ABC, abstractmethod


class EntidadSistema(ABC):
    """Clase abstracta general para representar entidades del sistema."""

    @abstractmethod
    def mostrar_informacion(self):
        """Método abstracto que debe ser implementado por las clases hijas."""
        pass