# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Creación: 06 Octubre 2025
# Última Edición: 06 Octubre 2025
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
from typing import (Tuple)
from enum import (Enum)


# ------------------------------
# ENUMS
# ------------------------------

class ColorScheme(str, Enum):
    """
    Esquema de colores ANSI para terminal.

    Attributes:
        RESET: Resetea al color por defecto.
        RED: Color rojo.
        GREEN: Color verde.
        YELLOW: Color amarillo.
        BLUE: Color azul.
        MAGENTA: Color magenta.
        CYAN: Color cian.
        WHITE: Color blanco.
    """
    # -- Atributos -- #
    RESET   = "\033[0m"
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"


    # -- Default -- #

    def __str__(self) -> str:
        """
        Retorna el valor en formato de cadena.

        Returns:
            str: Formato en cadena.
        """
        # Retorna el valor.
        return self.value
    

    # -- Métodos -- #

    @classmethod
    def create_custom_color(cls, rgb:Tuple[int, int, int]) -> str:
        """
        Crea un código ANSI para color rgb (soportado en terminales modernas).

        Args:
            rgb (Tuple): Tupla con valores rgb (0-255)
        Returns:
            Código de escape ANSI para el color personalizado.
        """
        # Obtiene los valores.
        r, g, b = rgb

        # Retorna el código ANSI.
        return f"\033[38;2;{r};{g};{b}m"