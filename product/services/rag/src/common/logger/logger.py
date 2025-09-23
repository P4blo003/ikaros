# ------------------------------------------------------------
# Autor: Pablo González García
# Fecha: 23 Septiembre 2025
# Descripción: Contiene las funcionalidades principales
#       del módulo interno de logger.
# ------------------------------------------------------------


# ------------------------------
# IMPORTS
# ------------------------------

# Estándar:
import logging
from logging.handlers import RotatingFileHandler
from typing import Optional

# Internas:
from .model import LoggerConfig


# ------------------------------
# FUNCIONES
# ------------------------------

def create_logger(name:str, logger_config:Optional[LoggerConfig] = None) -> logging.Logger:
    """
    Crea y retorna un logger.

    Args:
        name (str):                             Nombre del logger a crear.
        logger_config (Optional[LoggerConfig]): Configuración del logger. Por defecto
            es None y se inicializa con los valores por defecto.
    """
    # Comprueba si logger_config es nulo.
    if not logger_config:
        # Crea una configuración por defecto.
        logger_config = LoggerConfig()

    # Crea el logger a retornar.
    logger:logging.Logger = logging.getLogger(name=name)
    # Establece el nivel mínimo de severidad del logger.
    logger.setLevel(logger_config.level)
    
    # Crea el formatter para los logs.
    formatter:logging.Formatter = logging.Formatter(logger_config.format,
                                                    datefmt=logger_config.datefmt)

    # Crea el handler de consola.
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logger_config.level)
    console_handler.setFormatter(formatter)
    # Añade el handler.
    logger.addHandler(console_handler)

    # Comprueba si file_path no es nulo.
    if logger_config.file_path:
        # Crea el handler de consola.
        file_handler:RotatingFileHandler = RotatingFileHandler(filename=logger_config.file_path,
                                                               maxBytes=logger_config.max_bytes,
                                                               backupCount=logger_config.backup_count)
        file_handler.setLevel(logger_config.level)
        file_handler.setFormatter(formatter)
        # Añade el handler.
        logger.addHandler(file_handler)

    # Retorna el logger.
    return logger