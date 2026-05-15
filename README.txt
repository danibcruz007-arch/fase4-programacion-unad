Hola, gracias por pasar por aquí.

Este proyecto nace como parte de la Fase 4 del curso Programación (213023) de la Universidad Nacional Abierta y a Distancia - UNAD, pero más allá de los requisitos, es una pequeña muestra de lo que se puede construir aplicando programación orientada a objetos y manejo inteligente de errores en Python.

Se trata de un sistema que simula la operación de una empresa ficticia llamada Software FJ, permitiendo gestionar clientes, ofrecer servicios y procesar reservas. Todo pensado para ser modular, robusto y fácil de extender.

¿Qué busca este proyecto?

Más que cumplir con una lista de temas vistos en clase, el sistema intenta mostrar cómo se organiza un software real aplicando conceptos como:

Concepto	Cómo se aplica
Abstracción	Clases base que definen el "contrato" de lo que debe hacer un servicio
Herencia	Servicios especializados que crecen desde una idea común
Polimorfismo	Cada servicio calcula su costo a su manera, pero todos responden al mismo mensaje
Encapsulación	Proteger los datos del cliente y controlar cómo se modifican
Excepciones personalizadas	Errores que hablan el mismo idioma del negocio
Logs	Porque hasta los errores dejan huella y eso está bien
Simulación de operaciones	Aprender también es equivocarse con estilo
¿Cómo está organizado el proyecto?

Te dejo la estructura de archivos para que te ubiques rápidamente:

software_fj/
│
├── main.py                 # ejecuta la simulación paso a paso
├── entidades.py            # La idea abstracta de lo que es una "entidad"
├── cliente.py              # Cliente con nombre, documento y correo validados
├── servicios.py            # Servicios: sala, equipo, asesoría
├── reserva.py              # Reservas que pasan por estados: creada, confirmada, procesada...
├── excepciones.py          # Errores que hablan del dominio del problema
├── logger_sistema.py       # Registro de eventos y errores en logs.txt
├── logs.txt                # Bitácora automática del sistema
└── README.md               # Esto que estás leyendo
¿Cómo ejecutar el proyecto?
Descargar o clonar el repositorio desde GitHub.
Abrir la carpeta software_fj en Visual Studio Code.
Abrir una terminal dentro del proyecto.
Ejecutar el siguiente comando:
python main.py
El sistema comenzará a ejecutar automáticamente las operaciones simuladas.
Al finalizar, se podrá revisar el archivo logs.txt, donde quedan registrados eventos, errores y operaciones realizadas por el sistema.
¿Qué hace el sistema?

Durante la ejecución se realizan diferentes pruebas para validar el comportamiento del programa. Algunas operaciones son exitosas y otras generan errores controlados para demostrar el manejo de excepciones.

Entre las operaciones simuladas se encuentran:

Registro de clientes válidos
Registro de clientes con errores
Creación de servicios
Procesamiento de reservas
Reservas inválidas
Servicios no disponibles
Validaciones de datos
Cancelaciones inválidas
Registro automático de logs

El objetivo es que el sistema continúe funcionando incluso cuando ocurren errores durante la ejecución.

Tecnologías utilizadas
Python 3.13
Programación Orientada a Objetos
Manejo avanzado de excepciones
GitHub
Archivos de texto para logs
