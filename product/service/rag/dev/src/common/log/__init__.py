# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Descripción: Contiene las funcionalidades que se pueden exportar
# desde el módulo.
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
from typing import List

# Internas:
from .main import LoggerManager


# ------------------------------
# VARIABLES
# ------------------------------

# Contiene las funcionalidades a exportar.
__all__:List[str] = []


# ------------------------------
# LÓGICA
# ------------------------------

# Establece las clases.
__all__.append("LoggerManager")