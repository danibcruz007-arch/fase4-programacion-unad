# ============================================================
# Archivo: servicios.py
# Descripción: Clase abstracta Servicio y servicios derivados.
# ============================================================

from abc import ABC, abstractmethod
from excepciones import ServicioInvalidoError, ServicioNoDisponibleError, CalculoInconsistenteError


class Servicio(ABC):
    """Clase abstracta para representar servicios ofrecidos por Software FJ."""

    def __init__(self, nombre, tarifa_base, disponible=True):
        if not nombre or not nombre.strip():
            raise ServicioInvalidoError("El nombre del servicio no puede estar vacío.")

        if tarifa_base <= 0:
            raise ServicioInvalidoError("La tarifa base debe ser mayor que cero.")

        self._nombre = nombre
        self._tarifa_base = tarifa_base
        self._disponible = disponible

    @property
    def nombre(self):
        return self._nombre

    @property
    def disponible(self):
        return self._disponible

    def validar_disponibilidad(self):
        if not self._disponible:
            raise ServicioNoDisponibleError(f"El servicio '{self._nombre}' no está disponible.")

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass


class ReservaSala(Servicio):
    """Servicio especializado para reserva de salas."""

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_disponibilidad()

        if duracion <= 0:
            raise CalculoInconsistenteError("La duración de la reserva debe ser mayor que cero.")

        subtotal = self._tarifa_base * duracion
        total = subtotal - descuento + (subtotal * impuesto)

        if total < 0:
            raise CalculoInconsistenteError("El costo total no puede ser negativo.")

        return total

    def describir_servicio(self):
        return f"Reserva de sala: {self._nombre}, tarifa por hora: ${self._tarifa_base}"


class AlquilerEquipo(Servicio):
    """Servicio especializado para alquiler de equipos."""

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_disponibilidad()

        if duracion <= 0:
            raise CalculoInconsistenteError("La duración del alquiler debe ser mayor que cero.")

        cargo_mantenimiento = 15000
        subtotal = (self._tarifa_base * duracion) + cargo_mantenimiento
        total = subtotal - descuento + (subtotal * impuesto)

        if total < 0:
            raise CalculoInconsistenteError("El costo total no puede ser negativo.")

        return total

    def describir_servicio(self):
        return f"Alquiler de equipo: {self._nombre}, tarifa por hora: ${self._tarifa_base}"


class AsesoriaEspecializada(Servicio):
    """Servicio especializado para asesorías profesionales."""

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_disponibilidad()

        if duracion <= 0:
            raise CalculoInconsistenteError("La duración de la asesoría debe ser mayor que cero.")

        tarifa_profesional = self._tarifa_base * 1.25
        subtotal = tarifa_profesional * duracion
        total = subtotal - descuento + (subtotal * impuesto)

        if total < 0:
            raise CalculoInconsistenteError("El costo total no puede ser negativo.")

        return total

    def describir_servicio(self):
        return f"Asesoría especializada: {self._nombre}, tarifa por hora: ${self._tarifa_base}"