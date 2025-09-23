# ------------------------------------------------------------
# Autor: Pablo González García
# Fecha: 23 Septiembre 2025
# Descripción: Contiene código para importación del 
#       módulo.
# ------------------------------------------------------------


# ------------------------------
# IMPORTS
# ------------------------------

# Internas:
from .logger import create_logger


# ------------------------------
# CONFIGURACIÓN
# ------------------------------

# Permite importar directamente desde el paquete.
__all__ = ['create_logger']