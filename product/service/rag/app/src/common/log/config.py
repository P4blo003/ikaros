# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Creación: 06 Octubre 2025
# Última Edición: 06 Octubre 2025
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
from typing import Optional

# Externas:
from pydantic import (BaseModel, Field)


# ------------------------------
# CLASES
# ------------------------------

class FileConfig(BaseModel):
    """
    Configuración del fichero de salida de los loggers.

    Attributes:
        max_bytes (int): Tamaño máximo del fichero en bytes.
        backup_count (int): Número de backups.
    """
    # -- Atributos -- #
    max_bytes:int       = Field(default=1*1024*1024, ge=1024)
    backup_count:int    = Field(default=1, ge=1, le=100)

class LoggerConfig(BaseModel):
    """
    Configuración del logger.

    Attributes:
        level (str): Mínimo nivel de severidad del logger.
        fmt (str): Formato del mensaje.
        date_fmt (str): Formato de la fecha del mensaje.
        file_cfg (FileConfig): Configuración del fichero de salida.
    """
    # -- Atributos -- #
    level:str                       = Field(default='INFO')
    fmt:str                         = Field(default='%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    date_fmt:str                    = Field(default='%Y-%m-%d %H:%M:%S')
    file_cfg:Optional[FileConfig]   = Field(default=None)