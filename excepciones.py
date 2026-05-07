# ============================================================
# Archivo: excepciones.py
# Proyecto: Sistema Integral de Gestión - Software FJ
# Descripción: Define excepciones personalizadas del sistema.
# ============================================================


class ErrorSistemaFJ(Exception):
    """Clase base para las excepciones personalizadas del sistema."""
    pass


class ClienteInvalidoError(ErrorSistemaFJ):
    """Se lanza cuando los datos de un cliente no son válidos."""
    pass


class ServicioInvalidoError(ErrorSistemaFJ):
    """Se lanza cuando un servicio tiene datos incorrectos."""
    pass


class ServicioNoDisponibleError(ErrorSistemaFJ):
    """Se lanza cuando se intenta usar un servicio no disponible."""
    pass


class ReservaInvalidaError(ErrorSistemaFJ):
    """Se lanza cuando una reserva no puede procesarse correctamente."""
    pass


class CalculoInconsistenteError(ErrorSistemaFJ):
    """Se lanza cuando un cálculo genera un resultado inválido."""
    pass