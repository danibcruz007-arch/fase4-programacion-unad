# ============================================================
# Archivo: main.py
# Proyecto: Sistema Integral de Gestión de Clientes, Servicios y Reservas
# Empresa: Software FJ
# Descripción:
# Este archivo simula operaciones válidas e inválidas para demostrar
# programación orientada a objetos y manejo de excepciones.
# ============================================================

from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from logger_sistema import LoggerSistema
from excepciones import (
    ClienteInvalidoError,
    ServicioInvalidoError,
    ServicioNoDisponibleError,
    ReservaInvalidaError,
    CalculoInconsistenteError
)


logger = LoggerSistema()


def ejecutar_operacion(numero, descripcion, funcion):
    """
    Ejecuta una operación del sistema de forma segura.
    Permite que el programa continúe funcionando aunque una operación falle.
    """

    print(f"\nOperación {numero}: {descripcion}")
    logger.registrar_evento(f"Inicio de operación {numero}: {descripcion}")

    try:
        resultado = funcion()

    except (
        ClienteInvalidoError,
        ServicioInvalidoError,
        ServicioNoDisponibleError,
        ReservaInvalidaError,
        CalculoInconsistenteError
    ) as error:
        print(f"Error controlado: {error}")
        logger.registrar_error(f"Operación {numero} fallida: {error}")

    except Exception as error:
        # Encadenamiento de excepciones:
        # Se captura un error inesperado y se genera una nueva excepción
        # usando "raise ... from error", que es la forma correcta en Python.
        try:
            raise RuntimeError(
                "Se presentó un error inesperado en el sistema."
            ) from error

        except RuntimeError as nuevo_error:
            print(f"Error inesperado: {nuevo_error}")
            logger.registrar_error(
                f"Operación {numero} con error inesperado: {nuevo_error}"
            )

    else:
        print("Operación realizada correctamente.")
        if resultado is not None:
            print(resultado)
        logger.registrar_evento(f"Operación {numero} ejecutada correctamente.")

    finally:
        print("Finalización de la operación.")
        logger.registrar_evento(f"Fin de operación {numero}.")


# Listas internas para simular almacenamiento sin base de datos
clientes = []
servicios = []
reservas = []


# ============================================================
# Operaciones simuladas
# ============================================================

def operacion_1_cliente_valido():
    cliente = Cliente("Daniel Barrera", "1070981816", "daniel.barrera@email.com")
    clientes.append(cliente)
    return cliente.mostrar_informacion()


def operacion_2_cliente_documento_invalido():
    cliente = Cliente("Laura Blanco", "ABC123", "laura@email.com")
    clientes.append(cliente)


def operacion_3_cliente_correo_invalido():
    cliente = Cliente("Carlos Ruiz", "123456789", "correo_invalido")
    clientes.append(cliente)


def operacion_4_crear_reserva_sala():
    servicio = ReservaSala("Sala Ejecutiva", 25000)
    servicios.append(servicio)
    return servicio.describir_servicio()


def operacion_5_crear_alquiler_equipo():
    servicio = AlquilerEquipo("Video Beam", 18000)
    servicios.append(servicio)
    return servicio.describir_servicio()


def operacion_6_crear_asesoria():
    servicio = AsesoriaEspecializada("Asesoría en Python", 40000)
    servicios.append(servicio)
    return servicio.describir_servicio()


def operacion_7_servicio_tarifa_invalida():
    servicio = ReservaSala("Sala Pequeña", -10000)
    servicios.append(servicio)


def operacion_8_reserva_exitosa():
    cliente = clientes[0]
    servicio = servicios[0]

    reserva = Reserva(cliente, servicio, 3)
    reserva.confirmar()
    costo = reserva.procesar(descuento=5000, impuesto=0.19)

    reservas.append(reserva)

    return f"{reserva.mostrar_resumen()} | Total calculado: ${costo}"


def operacion_9_reserva_duracion_invalida():
    cliente = clientes[0]
    servicio = servicios[1]

    reserva = Reserva(cliente, servicio, -2)
    reservas.append(reserva)


def operacion_10_reserva_sin_confirmar():
    cliente = clientes[0]
    servicio = servicios[1]

    reserva = Reserva(cliente, servicio, 2)
    reservas.append(reserva)

    return reserva.procesar()


def operacion_11_servicio_no_disponible():
    cliente = clientes[0]
    servicio = AsesoriaEspecializada(
        "Asesoría no disponible",
        50000,
        disponible=False
    )

    reserva = Reserva(cliente, servicio, 2)
    reserva.confirmar()

    reservas.append(reserva)

    return reserva.procesar()


def operacion_12_cancelar_reserva_procesada():
    cliente = clientes[0]
    servicio = servicios[2]

    reserva = Reserva(cliente, servicio, 1)
    reserva.confirmar()
    reserva.procesar()
    reserva.cancelar()


def main():
    print("==============================================")
    print(" Sistema Integral de Gestión - Software FJ")
    print(" Clientes, Servicios y Reservas")
    print("==============================================")

    ejecutar_operacion(1, "Registro válido de cliente", operacion_1_cliente_valido)
    ejecutar_operacion(2, "Registro inválido de cliente por documento", operacion_2_cliente_documento_invalido)
    ejecutar_operacion(3, "Registro inválido de cliente por correo", operacion_3_cliente_correo_invalido)
    ejecutar_operacion(4, "Creación válida de servicio Reserva de Sala", operacion_4_crear_reserva_sala)
    ejecutar_operacion(5, "Creación válida de servicio Alquiler de Equipo", operacion_5_crear_alquiler_equipo)
    ejecutar_operacion(6, "Creación válida de servicio Asesoría Especializada", operacion_6_crear_asesoria)
    ejecutar_operacion(7, "Creación inválida de servicio por tarifa negativa", operacion_7_servicio_tarifa_invalida)
    ejecutar_operacion(8, "Reserva exitosa con descuento e impuesto", operacion_8_reserva_exitosa)
    ejecutar_operacion(9, "Reserva fallida por duración inválida", operacion_9_reserva_duracion_invalida)
    ejecutar_operacion(10, "Reserva fallida por procesar sin confirmar", operacion_10_reserva_sin_confirmar)
    ejecutar_operacion(11, "Reserva fallida por servicio no disponible", operacion_11_servicio_no_disponible)
    ejecutar_operacion(12, "Cancelación inválida de reserva procesada", operacion_12_cancelar_reserva_procesada)

    print("\n==============================================")
    print(" Simulación finalizada.")
    print(" Revise el archivo logs.txt para ver eventos y errores.")
    print("==============================================")


if __name__ == "__main__":
    main()