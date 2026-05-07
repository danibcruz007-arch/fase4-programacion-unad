# ============================================================
# Archivo: logger_sistema.py
# Descripción: Registra eventos y errores en un archivo de logs.
# ============================================================

from datetime import datetime


class LoggerSistema:
    """Clase encargada de escribir eventos y errores en logs.txt."""

    def __init__(self, archivo="logs.txt"):
        self.archivo = archivo

    def registrar_evento(self, mensaje):
        """Registra una acción normal del sistema."""
        self._escribir_log("EVENTO", mensaje)

    def registrar_error(self, mensaje):
        """Registra errores controlados del sistema."""
        self._escribir_log("ERROR", mensaje)

    def _escribir_log(self, tipo, mensaje):
        """Escribe el mensaje en el archivo con fecha y hora."""
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.archivo, "a", encoding="utf-8") as log:
            log.write(f"[{fecha}] [{tipo}] {mensaje}\n")