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
from .service import ServiceManager


# ------------------------------
# CONFIGURACIÓN
# ------------------------------

# Permite importar directamente desde el paquete.
__all__ = ['ServiceManager']