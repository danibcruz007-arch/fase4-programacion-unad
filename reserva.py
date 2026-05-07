# ============================================================
# Archivo: reserva.py
# Descripción: Clase Reserva con confirmación, cancelación y proceso.
# ============================================================

from excepciones import ReservaInvalidaError


class Reserva:
    """Integra cliente, servicio, duración y estado de una reserva."""

    def __init__(self, cliente, servicio, duracion):
        if cliente is None:
            raise ReservaInvalidaError("La reserva debe tener un cliente asociado.")

        if servicio is None:
            raise ReservaInvalidaError("La reserva debe tener un servicio asociado.")

        if duracion <= 0:
            raise ReservaInvalidaError("La duración de la reserva debe ser mayor que cero.")

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Creada"
        self.__costo_total = 0

    @property
    def estado(self):
        return self.__estado

    def confirmar(self):
        if self.__estado == "Cancelada":
            raise ReservaInvalidaError("No se puede confirmar una reserva cancelada.")

        self.__estado = "Confirmada"

    def cancelar(self):
        if self.__estado == "Procesada":
            raise ReservaInvalidaError("No se puede cancelar una reserva ya procesada.")

        self.__estado = "Cancelada"

    def procesar(self, descuento=0, impuesto=0):
        if self.__estado != "Confirmada":
            raise ReservaInvalidaError("La reserva debe estar confirmada antes de procesarse.")

        self.__costo_total = self.__servicio.calcular_costo(
            self.__duracion,
            descuento=descuento,
            impuesto=impuesto
        )

        self.__estado = "Procesada"
        return self.__costo_total

    def mostrar_resumen(self):
        return (
            f"Reserva | Cliente: {self.__cliente.nombre} | "
            f"Servicio: {self.__servicio.nombre} | "
            f"Duración: {self.__duracion} horas | "
            f"Estado: {self.__estado} | "
            f"Costo: ${self.__costo_total}"
        )