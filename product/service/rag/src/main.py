# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Descripción: Contiene las funcionalidades principales relacionadas
# con gRPC.
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
import sys
from typing import (Optional)

# Internos:
from core.lifecycle import (ApplicationLifeCycle)


# ------------------------------
# FUNCIONES
# ------------------------------

def main() -> int:
    """
    Función principal del programa.

    Returns:
        int: El estado de la ejecución (0 = éxito, >0 = error).
    """
    # -- Lógica -- #

    # Try-Except para manejo de errores.
    try:
        # Inicia el ciclo de vida de la aplicación.
        with ApplicationLifeCycle().managed_context() as (app):
            
            while not app.shutdown_requested:

                pass
        
        # Retorna éxito.
        return 0

    # Si ocurre algún error.
    except Exception as e:
        # Retorna error.
        return 1


# ------------------------------
# LÓGICA
# ------------------------------

# Comprueba como si se esta ejecutando como script.
if __name__ == "__main__":


    # Try-Except para manejo de errores.
    try:
        # Ejecuta la función principal.
        status:int = main()

        # Finaliza el programa.
        sys.exit(status)

    # Si ocurre algún error.
    except Exception as e:
        # Imprime el error.
        print(f"Fatal Error: {e}")

        # Finaliza el programa.
        sys.exit(2)