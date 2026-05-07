# Software FJ — Sistema de Gestión Integral

Hola, gracias por pasar por aquí.
 
Este proyecto nace como parte de la **Fase 4 del curso Programación (213023)** de la **Universidad Nacional Abierta y a Distancia - UNAD**, pero más allá de los requisitos, es una pequeña muestra de lo que se puede construir aplicando **programación orientada a objetos** y manejo inteligente de errores en Python.

Se trata de un sistema que simula la operación de una empresa ficticia llamada **Software FJ**, permitiendo gestionar clientes, ofrecer servicios y procesar reservas. Todo pensado para ser **modular, robusto y fácil de extender**.

---

## ¿Qué busca este proyecto?

Más que cumplir con una lista de temas vistos en clase, el sistema intenta mostrar cómo se organiza un software real aplicando conceptos como:

| Concepto | Cómo se aplica |
|----------|----------------|
| **Abstracción** | Clases base que definen el "contrato" de lo que debe hacer un servicio |
| **Herencia** | Servicios especializados que crecen desde una idea común |
| **Polimorfismo** | Cada servicio calcula su costo a su manera, pero todos responden al mismo mensaje |
| **Encapsulación** | Proteger los datos del cliente y controlar cómo se modifican |
| **Excepciones personalizadas** | Errores que hablan el mismo idioma del negocio |
| **Logs** | Porque hasta los errores dejan huella y eso está bien |
| **Simulación de operaciones** | Aprender también es equivocarse con estilo |

---

## ¿Cómo está organizado el proyecto?

Te dejo la estructura de archivos para que te ubiques rápidamente:

```text
software_fj/
│
├── main.py                 # El corazón: ejecuta la simulación paso a paso
├── entidades.py            # La idea abstracta de lo que es una "entidad"
├── cliente.py              # Cliente con nombre, documento y correo validados
├── servicios.py            # Servicios: sala, equipo, asesoría
├── reserva.py              # Reservas que pasan por estados: creada, confirmada, procesada...
├── excepciones.py          # Errores que hablan del dominio del problema
├── logger_sistema.py       # Registro de eventos y errores en logs.txt
├── logs.txt                # Bitácora automática del sistema
└── README.md               # Esto que estás leyendo