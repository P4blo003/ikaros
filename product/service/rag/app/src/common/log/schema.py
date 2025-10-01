# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Creación: 01/10/2025
# Última Edición: 01/10/2025
#
# Descripción: Implementa los esquemas relacionados con los
# logs del programa.
# ------------------------------------------------------------------------------------------

# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
from typing import Dict

# Internas:

# Externas:
from pydantic import (
    BaseModel,
    Field
)


# ------------------------------
# CLASES
# ------------------------------

class LoggerSchema(BaseModel):
    """
    Esquema con la configuración del logger.

    Attributes:
        level (str): Nivel mínimo de severidad.
        fmt (str): Formato del mensaje.
        date_fmt (str): Formato de la fecha del mensaje.
        max_bytes (int): Tamaño máximo del fichero de logs en bytes.
        backup_count (int): Número de backups.
    """
    # -- Atributos -- #
    level:str = Field(default='INFO', pattern='INFO|DEBUG', alias='level', description="Nivel mínimo de severidad.")
    fmt:str = Field(default='%(asctime)s | %(levelname)s | %(name)s - %(message)s', alias='format', description="Formato del mensaje.")
    date_fmt:str = Field(default='%Y-%m-%d %H:%M:%S', alias='datefmt', description="Formato de la fecha del mensaje.")
    max_bytes:int = Field(default=1024, alias='maxBytes', description="Tamaño máximo del fichero de logs en bytes.", ge=1024, le=1024*1024*1024)
    backup_count:int = Field(default=1, alias='backupCount', description="Número de backups.", ge=1, le=10)