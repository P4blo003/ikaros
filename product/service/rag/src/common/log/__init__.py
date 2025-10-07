# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Descripción: Contiene las funcionalidades que se pueden exportar
# desde el módulo.
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Internas:
from .main import LoggerManager


# ------------------------------
# VARIABLES
# ------------------------------

# Contiene las funcionalidades a exportar.
__all__ = []

# ------------------------------
# LÓGICA
# ------------------------------

# Establece las clases.
__all__ += ['LoggerManager']