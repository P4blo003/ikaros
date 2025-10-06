# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Creación: 06 Octubre 2025
# Última Edición: 06 Octubre 2025
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
from typing import (Optional, List)

# Internas:
from .main import (LoggerFactory)
from .config import (LoggerConfig)


# ------------------------------
# VARIABLES
# ------------------------------

# Imports de clases.
__all__:List = ['LoggerFactory', 'LoggerConfig']
# Factoría de loggers.
__loggerFactory:Optional[LoggerFactory] = None


# ------------------------------
# FUNCIONES
# ------------------------------

def init_factory(logger_cfg:LoggerConfig = LoggerConfig()) -> LoggerFactory:
    """
    Inicializa la factoría y la devuelve.

    Args:
        logger_cfg (LoggerConfig): Configuración del logger.
    Returns:
        LoggerFactory: Factoría de loggers.
    """
    # Establece variables globales.
    global __loggerFactory

    # Comprueba si ya está inicializado.
    if not __loggerFactory:
        # Inicializa la factoría.
        __loggerFactory = LoggerFactory(logger_cfg=logger_cfg)

    # Retorna la factoría.
    return __loggerFactory

def get_factory() -> LoggerFactory:
    """
    Obtiene la factoria de loggers. Sigue el patrón singleton, por lo que en caso de
    que no esté inicializada, la inicializa.

    Raises:
        ValueError: En caso de que la factoría no este inicializada.
    Returns:
        LoggerFactory: Factoría de loggers.
    """
    # Comprueba si no está inicializado.
    if not __loggerFactory:
        # Lanza un error.
        raise ValueError(
            "LoggerFactor isn't initialized. Please initialize it with the init_factory() method."
        )

    # Retorna la factoría.
    return __loggerFactory