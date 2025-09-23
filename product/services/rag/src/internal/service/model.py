# ------------------------------------------------------------
# Autor: Pablo González García
# Fecha: 23 Septiembre 2025
# Descripción: Contiene todas las clases relacionadas con
#       los servicios.
# ------------------------------------------------------------


# ------------------------------
# IMPORTS
# ------------------------------

# Externas:
from pydantic import (
    BaseModel,
    Field
)


# ------------------------------
# CLASES
# ------------------------------

class ServiceConfig(BaseModel):
    """
    Contiene la configuración del servicio.

    Attributes:
        host (str): Host en el que se lanza el servicio.
        port (int): Puerto en el que se lanza el servicio.
        max_workers (int): Número máximo de trabajadores.
    """
    # -- Atributos -- #
    host:str        = Field(default='localhost')
    port:int        = Field(default=50051, ge=9000, le=65535)
    max_workers:int = Field(default=1, ge=1, le=100)