# ------------------------------------------------------------
# Autor: Pablo González García
# Fecha: 23 Septiembre 2025
# Descripción: Contiene el flujo principal del servicio.
# ------------------------------------------------------------


# ------------------------------
# IMPORTS
# ------------------------------

# Estándar:
import logging
from typing import Optional

# Internas:
from common.logger import create_logger


# ------------------------------
# FLUJO PRINCIPAL
# ------------------------------

# Comprueba si se ejecuta como scropt.
if __name__ == "__main__":

    # Representa el estado del servicio.
    STATUS_CODE:int                 = 0
    # Representa el logger del servicio.
    LOGGER:Optional[logging.Logger] = None

    # Try-except para manejo de errores.
    try:
        # Crea el logger.
        LOGGER = create_logger(name='rag.service')

        # Imprime información de ejecución.
        LOGGER.info("Service started.")

        # Imprime información de finalización.
        LOGGER.info("Service finished.")

    # Si ocurre algún error.
    except Exception as e:
        # Comprueba si el logger no es nulo.
        if LOGGER:
            # Imprime el error.
            LOGGER.error(e)
        # Si no se ha iniciado el logger.
        else:
            pass
        # Establece el estado.
        STATUS_CODE = 1

    # Se ejecuta siempre al final.
    finally:
        exit(code=STATUS_CODE)