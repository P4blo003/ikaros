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
from internal.service import ServiceManager
from common.logger import create_logger


# ------------------------------
# FLUJO PRINCIPAL
# ------------------------------

# Comprueba si se ejecuta como scropt.
if __name__ == "__main__":

    # Representa el estado del servicio.
    STATUS_CODE:int                         = 0
    # Representa el logger del servicio.
    LOGGER:Optional[logging.Logger]         = None
    # Representa el gestor del servicio.
    SERVICE_MNG:Optional[ServiceManager]    = None

    # Try-except para manejo de errores.
    try:
        # Crea el logger.
        LOGGER = create_logger(name='rag')

        # Inicializa el gestor del servicio.
        SERVICE_MNG = ServiceManager()

        # Inicia el servicio.
        SERVICE_MNG.serve()

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
        # Comprueba si el gestor del servicio no es nulo.
        if SERVICE_MNG:
            # Detiene y libera recursos.
            SERVICE_MNG.stop()
        # Finaliza el programa con el código de salida.
        exit(code=STATUS_CODE)