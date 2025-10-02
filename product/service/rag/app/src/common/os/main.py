# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Creación: 01/10/2025
# Última Edición: 01/10/2025
#
# Descripción: Implementa las funcionalidades principales relacionadas
# con el sistema del programa.
# ------------------------------------------------------------------------------------------

# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
import sys
from typing import Optional

# Internas:
from .schema import ExecInfo

# Externas:


# ------------------------------
# FUNCIONES
# ------------------------------

def get_exec_info() -> Optional[ExecInfo]:
    """
    Obtiene la información sobre la ejecución del programa.
    """
    # Obtiene la información del traceback.
    _, _, exc_traceback = sys.exc_info()

    # Comprueba si se ha obtenido un traceback.
    if exc_traceback:
        # Retorna la información.
        return ExecInfo(
            line_number=exc_traceback.tb_lineno,
            file_name=exc_traceback.tb_frame.f_code.co_filename
        )
    # En caso de que no se haya obtenido.
    return None