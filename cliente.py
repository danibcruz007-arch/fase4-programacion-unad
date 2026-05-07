# ============================================================
# Archivo: cliente.py
# Descripción: Clase Cliente con encapsulación y validaciones.
# ============================================================

from entidades import EntidadSistema
from excepciones import ClienteInvalidoError


class Cliente(EntidadSistema):
    """Representa un cliente de la empresa Software FJ."""

    def __init__(self, nombre, documento, correo):
        self.__nombre = None
        self.__documento = None
        self.__correo = None

        self.nombre = nombre
        self.documento = documento
        self.correo = correo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ClienteInvalidoError("El nombre del cliente no puede estar vacío.")
        self.__nombre = valor.strip()

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):
        if not str(valor).isdigit():
            raise ClienteInvalidoError("El documento debe contener solo números.")
        self.__documento = str(valor)

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if "@" not in valor or "." not in valor:
            raise ClienteInvalidoError("El correo electrónico no tiene un formato válido.")
        self.__correo = valor.strip()

    def mostrar_informacion(self):
        return f"Cliente: {self.__nombre} | Documento: {self.__documento} | Correo: {self.__correo}"