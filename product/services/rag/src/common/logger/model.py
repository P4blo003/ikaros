# ------------------------------------------------------------
# Autor: Pablo González García
# Fecha: 23 Septiembre 2025
# Descripción: Contiene todas las clases relacionadas con
#       los logger del programa.
# ------------------------------------------------------------


# ------------------------------
# IMPORTS
# ------------------------------

# Estándar:
from typing import Optional

# Externas:
from pydantic import (
    BaseModel,
    Field
)


# ------------------------------
# CLASES
# ------------------------------

class LoggerConfig(BaseModel):
    """
    Contiene la configuración de un logger.

    Attributes:
        level (str):        Indica el nivel mínimo de severidad de los mensajes.
        format (str):       Formato de los mensajes del log.
        datefmt (str):      Formato de la fecha de los mensajes del log.
        file_path (str):    Ruta a la carpeta de logs.
        max_bytes (int):    Tamaño máximo de bytes del fichero de logs.
        backup_count (int): Controla cuántos archivos de respañdo se conservan
            al hacer rotación de logs.
    """
    # -- Atributos -- #
    level:str =                     Field(default='INFO')
    format:str =                    Field(default='%(asctime)s - %(name)s - %(levelname)-8s - %(message)s')
    datefmt:str =                   Field(default='%Y-%m-%d %H:%M:%S')
    file_path:Optional[str] =       Field(default=None)
    max_bytes:Optional[str] =       Field(default=None)
    backup_count:Optional[str] =    Field(default=None)