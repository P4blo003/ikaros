# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Creación: 06 Octubre 2025
# Última Edición: 06 Octubre 2025
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
from typing import (Optional)
from logging import (Logger, Formatter, StreamHandler)
from logging import (getLogger)
from logging.handlers import (RotatingFileHandler)
from pathlib import (Path)

# Internas:
from .config import (LoggerConfig)


# ------------------------------
# CLASES
# ------------------------------

class LoggerFactory:
    """
    Factoría de loggers. Permite la creación de loggers de diferentes tipos y salidas
    """
    # -- Default -- #

    def __init__(self, logger_cfg:LoggerConfig) -> None:
        """
        Inicializa las propiedades.

        Args:
            logger_cfg (LoggerConfig): Configuración del logger.
        """
        # Inicializa las propiedades.
        self.__logger_cfg:LoggerConfig = logger_cfg


    # -- Métodos -- #

    def get_logger(self, name:str, console_output:bool = True, file_output:Optional[Path] = None) -> Logger:
        """
        Genera un logger con la configuración dada.

        Args:
            name (str): Nombre del logger.
            console_output (bool): True si se desea salida por consola (True por defecto).
            file_output (Optional[Path]): Ruta a fichero de salida (None por defecto).
        """
        # Comprueba si los parámetros son correctos.
        if not console_output and not file_output:
            # Lanza una excepción.
            raise ValueError(
                "Invalid logger argument: Logger should have at least one output.\n"
                "Available values:\n" \
                "\t- console_output: True if you want console output.\n" \
                "\t- file_output: Path if you want file output.\n" \
                f"Given: console_output={console_output} | file_output={file_output}\n"
            )
        
        # Comprueba si el nombre es correcto.
        if name.strip() == "":
            # Lanza una excepción.
            raise ValueError(
                "Invalid logger argument: Logger name invalid.\n"
                f"Given: name={name}\n"
            )
        
        # Genera un logger con el nombre.
        logger:Logger = getLogger(name=name)
        logger.setLevel(level=self.__logger_cfg.level)

        # Genera el formateador.
        formatter:Formatter = Formatter(fmt=self.__logger_cfg.fmt, datefmt=self.__logger_cfg.date_fmt)

        # Comprueba si se quiere salida por consola.
        if console_output:
            # Crea  configura el handler de consola.
            console_handler:StreamHandler = StreamHandler()
            console_handler.setFormatter(fmt=formatter)
            # Añade el handler.
            logger.addHandler(hdlr=console_handler)

        # Retorna el logger creado.
        return logger