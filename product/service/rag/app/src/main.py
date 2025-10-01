# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Creación: 01/10/2025
# Última Edición: 01/10/2025
#
# Descripción: Implementa el flujo principal del servicio.
# ------------------------------------------------------------------------------------------

# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
import sys
from pathlib import Path
from typing import Optional

# Internas:
from common.log import LoggerFactory
from common.os import ExecInfo
from common.os import get_exec_info

# Externas:


# ------------------------------
# FUNCIONES
# ------------------------------

def print_error(exception:Exception, info:Optional[ExecInfo]) -> None:
    """
    Imprime el error en un formato dado.

    Args:
        exception (Exception): Excepción a imprimir.
        info (ExecInfo): Información de la ejecución.
    """
    # Inicializa la cadena a mostrar.
    error:str = f"\n{str(exception)}"
    error += f"TYPE: {type(exception).__name__}"

    # Comprueba si se ha dado información de ejecución.
    if info:
        # Añade la información.
        error += f" at {info.file_name} in line {info.line_number}"
    
    # Añade el punto final.
    error += ".\n"

    # Imprime el error.
    print(error)


# ------------------------------
# LÓGICA
# ------------------------------

# Comprueba si se está ejecutando como script.
if __name__ == "__main__":

    # -- Variables -- #
    EXEC_STATUS:int = 0

    # Try-Except para manejo de errores.
    try:
        pass
    
    # Si se detecta Ctrl+C
    except KeyboardInterrupt:
        # Imprime la información.
        print("Ctrl+C detectado. Finalizando programa ...")

    # Si se detecta cualquier error.
    except Exception as e:
        # Establece el estado de ejecución.
        EXEC_STATUS = 1
        # Imprime el error.
        print_error(exception=e, info = get_exec_info())

    # Se ejecuta finalmente.
    finally:
        # Finaliza el programa con el código de estado.
        sys.exit(EXEC_STATUS)