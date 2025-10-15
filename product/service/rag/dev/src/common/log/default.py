# ------------------------------------------------------------------------------------------
# Autor: Pablo González García.
# Descripción: Contiene clases, propiedades y métodos por
# defecto para el logging del sistema.
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
from typing import (Any, Dict)


# ------------------------------
# VARIABLES
# ------------------------------

# Configuración por defecto para el logging el sistema.
DEFAULT_LOGGING_CONFIG: Dict[str, Any] = {
    # Versión del esquema de configuración. Siempre usar 1.
    # Garantiza la compatibilidad con versiones futuras.
    "version": 1,

    # Gestiona los loggers previamente creados antes de establecer
    # la configuración.
    "disable_existing_loggers": False,

    # Configuración de los formatos.
    "formatters": {
        # Formato estándar.
        "standard": {
            # Formato del mensaje.
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            # Formato de la fecha del mensaje.
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        # Formato detallado.
        "detailed": {
            # Formato del mensaje.
            "format": "%(asctime)s [%(levelname)s] %(name)s - %(lineno)d: %(message)s",
            # Formato de la fecha del mensaje.
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },

    # Configuración de los handlers.
    "handlers": {
        # Handler básico para consola: Solo INFO y superior.
        "console_info": {
            # Clase del handler.
            "class": "logging.StreamHandler",
            # Mínimo nivel de severidad.
            "level": "INFO",
            # Formato.
            "formatter": "standard",
            # Salida por consola.
            "stream": "ext://sys.stdout"
        },

        # Handler para consola en desarrollo.
        "console_debug": {
            # Clase del handler.
            "class": "logging.StreamHandler",
            # Mínimo nivel de severidad.
            "level": "DEBUG",
            # Formato.
            "formatter": "detailed",
            # Salida por consola.
            "stream": "ext://sys.stdout"
        },

        # Handler para errores en consola.
        "console_error": {
            # Clase del handler.
            "class": "logging.StreamHandler",
            # Mínimo nivel de severidad.
            "level": "ERROR",
            # Formato.
            "formatter": "detailed",
            # Salida por consola.
            "stream": "ext://sys.stderr"
        },

        # Archivo para el servicio gRPC.
        "grpc_file": {
            # Clase del handler.
            "class": "logging.handlers.RotatingFileHandler",
            # Mínimo nivel de severidad.
            "level": "DEBUG",
            # Formato.
            "formatter": "standard",
            # Nombre del fichero.
            "filename": "logs/grpc.log",
            # Tamaño máximo del fichero.
            "maxBytes": 10485760,   # 10MB.
            # Número de backups.
            "backupCount": 3,
            # Codificación.
            "encoding": "utf-8"
        },

        # Archivo para errores.
        "error_file": {
            # Clase del handler.
            "class": "logging.handlers.RotatingFileHandler",
            # Mínimo nivel de severidad.
            "level": "ERROR",
            # Formato.
            "formatter": "detailed",
            # Nombre del fichero.
            "filename": "logs/error.log",
            # Tamaño máximo del fichero.
            "maxBytes": 5242880,   # 5MB.
            # Número de backups.
            "backupCount": 10,
            # Codificación.
            "encoding": "utf-8"
        }
    },

    # Configuración de los loggers.
    "loggers": {
        # Logger raíz: Captura todo lo no especificado.
        "": {
            # Handlers del logger.
            "handlers": ["console_info", "error_file"],
            # Mínimo nivel de severidad.
            "level": "WARNING",
            # Indica si los mensajes se envían o no al padre (en este caso
            # no hay pero es buena práctica).
            "propagate": False
        },

        # Logger principal.
        "app": {
            # Handlers del logger.
            "handlers": ["console_info", "error_file"],
            # Mínimo nivel de severidad.
            "level": "INFO",
            # Indica si los mensajes se envían o no al padre (en este caso
            # no hay pero es buena práctica).
            "propagate": False
        },

        # Logger para el servicio gRPC.
        "grpc_server": {
            # Handlers del logger.
            "handlers": ["console_info", "grpc_file", "error_file"],
            # Mínimo nivel de severidad.
            "level": "DEBUG",
            # Indica si los mensajes se envían o no al padre (en este caso
            # no hay pero es buena práctica).
            "propagate": False
        }
    }
}
