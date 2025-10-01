# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Creación: 01/10/2025
# Última Edición: 01/10/2025
#
# Descripción: Implementa los esquemas relacionadas
# con el sistema del programa.
# ------------------------------------------------------------------------------------------

# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:

# Internas:

# Externas:
from pydantic import (
    BaseModel
)


# ------------------------------
# CLASES
# ------------------------------

class ExecInfo(BaseModel):
    """
    Esquema con la información de la ejecución.

    Attributes:
        line_number (int): Línea en la que ocurrió el error.
        file_name (str): Nombre del fichero en el que se encuentra el error.
    """
    # -- Atributos -- #
    line_number:int
    file_name:str