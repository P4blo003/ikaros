# ------------------------------------------------------------
# Autor: Pablo González García
# Fecha: 23 Septiembre 2025
# Descripción: Contiene el flujo principal del servicio.
# ------------------------------------------------------------


# ------------------------------
# IMPORTS
# ------------------------------

# Internas:
from common.logger import create_logger


# ------------------------------
# FLUJO PRINCIPAL
# ------------------------------

# Comprueba si se ejecuta como scropt.
if __name__ == "__main__":

    # Crea el logger.
    logger = create_logger(name='rag.service')

    # Imprime información de ejecución.
    logger.info("Service started.")

    # Imprime información de finalización.
    logger.info("Service finished.")