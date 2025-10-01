# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Creación: 01/10/2025
# Última Edición: 01/10/2025
#
# Descripción: Implementa las funcionalidades principales relacionadas
# con los logs del programa.
# ------------------------------------------------------------------------------------------

# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import (
    Optional,
    Dict
)

# Internas:
from .schema import LoggerSchema

# Externas:


# ------------------------------
# CLASES
# ------------------------------

class LoggerFactory:
    """
    Factoría para la construcción de loggers.
    """
    # -- Default -- #
    
    def __init__(self, sch:LoggerSchema = LoggerSchema()) -> None:
        """
        Inicializa la factoria con la configuración dada.

        Args:
            sch (LoggerSchema): Esquema con la configuración del logger.
        """
        # Inicializa las propiedades.
        self.__schema:LoggerSchema = sch
        self.__created_loggers:Dict[str, logging.Logger] = {}
    

    # -- Métodos -- #

    def get_logger(self, name:str, console_output:bool=True, file:Optional[Path]=None) -> logging.Logger:
        """
        Obtiene un logger con el nombre dado. Permite indicar el tipo de salida para el logger, pudiendo
        ser tanto por consola como en un fichero.

        Args:
            name (str): Nombre del logger.
            console_output (bool): True si se desea salida por consola.
            file (Optiona[Path]): Si se aporta este dato, se creará un fichero de salida.
        Raises:
            ValeueError: En caso de que alguno de los argumentos sea inválido.
        Returns:
            logging.Logger: Logger configurado.
        """
        # Comprueba si los parámetros son correctos.
        if not console_output and not file:
            # Lanza un aexcepción.
            raise ValueError(
                "Configuración del logger inválida: El logger debe tener al menos una salida especificada.\n"
                f"Valores disponibles:\n"
                f"\t- console_output: True si se quiere salida por consola.\n"
                f"\t- file: Path si se quiere salida por fichero.\n"
                f"Valores aportados:\n"
                f"\t- console_output={console_output} | file={file}\n"
            )
        
        # Comprueba que el nombre sea válido.
        if name.strip() == '':
            # Lanza una excepción.
            raise ValueError(
                "Configuración del logger inválida: El nombre del logger no puede estar vacío.\n"
                f"Valor aportado:\n"
                f"\t- name='{name}'\n"
            )

        # Inicializa el logger inicial.
        logger:logging.Logger = logging.getLogger(name=name)
        logger.setLevel(level=self.__schema.level)

        # Evita que haya handlers duplciados.
        if logger.handlers:
            # Limpia los handlers.
            logger.handlers.clear()

        # Crea el formateador.
        formatter:logging.Formatter = logging.Formatter(fmt=self.__schema.fmt, datefmt=self.__schema.date_fmt)

        # Comprueba si se desea un handler de consola.
        if console_output:
            # Crea y configura el handler.
            console_handler:logging.StreamHandler = logging.StreamHandler()
            console_handler.setFormatter(fmt=formatter)
            # Añade el handler.
            logger.addHandler(console_handler)
        
        # Comprueba si se desea un handler de fichero.
        if file:
            # Comprueba si la ruta padre exsite.
            if not file.parent.exists():
                # Lanza una excepción.
                raise FileNotFoundError(
                "Configuración del logger inválida: No se encontró ninguna ruta hasta el Path especifciado.\n"
                f"Valores aportados:\n"
                f"\t- file={file}\n"
            )

            # Crea y configura el handler.
            file_handler:RotatingFileHandler = RotatingFileHandler(filename=file,
                                                                   maxBytes=self.__schema.max_bytes,
                                                                   backupCount=self.__schema.backup_count)
            file_handler.setFormatter(fmt=formatter)
            # Añade el handler.
            logger.addHandler(file_handler)

        # Añade el handler creado al diccionario.
        self.__created_loggers[name] = logger

        # Retorna el logger configurado.
        return logger