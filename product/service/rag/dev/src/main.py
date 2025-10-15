# ------------------------------------------------------------------------------------------
# Autor: Pablo González García.
# Descripción: Archivo principal del programa. Contiene la
# lógica principal.
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estánadar:
import sys
from typing import (List, Optional)

# Internos:
from common.log import LoggerManager
from core.context.lifecycle import LifecycleManager


# ------------------------------
# FUNCIONES
# ------------------------------

def main() -> int:
    """
    Función principal del programa. Ejecuta la lógica de negocio y 
    gestiona posibles errores.

    Returns:
        int: Código de ejecución del programa.
    """
    # -- Lógica -- #

    # Try-Except para manejo de errores.
    try:
        # Inicializa el logging.
        LoggerManager.setup_config()

        # Inicializa el gestor del ciclo de vida.
        with LifecycleManager().managed_context() as context:
            pass
    
        # Retorna éxito.
        return 0

    # Si ocurre algún error.
    except Exception as e:
        # Imprime el error.
        print(f"ERROR: Something ocurred during main execution: {e}")

        # Retorna error.
        return 1


# ------------------------------
# LÓGICA
# ------------------------------

# Entrada principal del programa.
if __name__ == "__main__":
    
    # Try-Except para manejo de errores.
    try:
        # Ejecuta la función principal.
        status:int = main()

        # Finaliza la ejecución con el código de estado.
        sys.exit(status)

    # Si ocurre algún error.
    except Exception as e:
        # Imprime el error.
        print(f"FATAL ERROR: An unhandled exception occurred during main execution: {e}")
        # Finaliza la jecución.
        sys.exit(-1)