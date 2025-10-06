# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Creación: 06 Octubre 2025
# Última Edición: 06 Octubre 2025
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
import sys
from typing import (Dict, Final)
from enum import (Enum)

# Internas:
from .ansi import (ColorScheme)


# ------------------------------
# ENUMS
# ------------------------------

class MessageType(Enum):
    """
    Tipos de mensajes para salida consistente.

    Attributes:
        INFO: Mensajes informativos.
        ERROR: Mensajes de error.
        WARNING: Mensajes de advertencia.
        SUCCESS: Mensajes de éxito.
        DEBUG: Mensajes de depuración.
    """
    # -- Atributos -- #
    INFO    = "INFO"
    ERROR   = "ERROR"
    WARNING = "WARNING"
    SUCCESS = "SUCCESS"
    DEBUG   = "DEBUG"


# ------------------------------
# VARIABLES
# ------------------------------

# Diccionario que relaciona el tipo de mensaje y el color.
MESSAGE_COLORS: Final[Dict[MessageType, ColorScheme]] = {
    MessageType.INFO: ColorScheme.BLUE,
    MessageType.SUCCESS: ColorScheme.GREEN,
    MessageType.ERROR: ColorScheme.RED,
    MessageType.WARNING: ColorScheme.YELLOW,
    MessageType.DEBUG: ColorScheme.MAGENTA
}


# ------------------------------
# CLASES
# ------------------------------

class Console:
    """
    Maneja la salida de mensajes formateados a consola.

    Attributes:
        use_colors (bool): Indica si usar colores ANSI.
        verbose (bool): Nivel de verbosidad para filtrar mensajes.
    """
    # -- Default -- #
    
    def __init__(self, use_colors:bool = True, verbose:bool = True) -> None:
        """
        Inicializa las propiedades.

        Args:
            use_colors (bool): Indica si usar colores ANSI.
            verbose (bool): Nivel de verbosidad para filtrar mensajes.
        """
        # Inicializa las propiedades.
        self.use_colors:bool = use_colors and self.supports_ansi()
        self.verbose:bool = verbose
    

    # -- Métodos -- #

    @staticmethod
    def supports_ansi() -> bool:
        """
        Verifica si la terminal soporta códigos ANSI.

        Returns:
            bool: True en caso de que la terminal soporte códigos ANSI.
        """
        # Retorna si los soporta.
        return sys.stdout.isatty()
    
    def format_prefix(self, label:str, color:ColorScheme) -> str:
        """
        Formatea el prefijo del mensaje con colores opcionales.

        Args:
            label (str): Etiqueta del prefijo.
            color (ColorScheme): Color a usar.
        """
        # Comprueba si debe usar colores.
        if self.use_colors:
            # Retorna el mensaje.
            return f"[{color}{label}{ColorScheme.RESET}]:"
        
        # Retorna valor por defecto.
        return f"[{label}]:"

    def print_message(self, message:str, message_type:MessageType, file = sys.stdout) -> None:
        """
        Imprime un mensaje formateado según su tipo.

        Args:
            message (str): Mensaje a imprimir.
            message_type (MessageType): Tipo del mensaje.
            file: Flujo de salida (stdout/stderr)
        """
        # Comprueba.
        if not self.verbose and message_type == MessageType.DEBUG:
            # Finaliza.
            return
        
        # Genera el prefijo.
        prefix:str = self.format_prefix(label=message_type.value, color=MESSAGE_COLORS.get(message_type, ColorScheme.RESET))

        # Imprime el mensaje.
        print(f"{prefix} {message}", file=file)
    
    def info(self, message:str) -> None:
        """
        Imprime un mensaje de información.

        Args:
            message (str): Mensaje a imprimir.
        """
        # Imprime el mensaje.
        self.print_message(message=message, message_type=MessageType.INFO)
    
    def success(self, message:str) -> None:
        """
        Imprime un mensaje de verificación..

        Args:
            message (str): Mensaje a imprimir.
        """
        # Imprime el mensaje.
        self.print_message(message=message, message_type=MessageType.SUCCESS)
    
    def warn(self, message:str) -> None:
        """
        Imprime un mensaje de aviso.

        Args:
            message (str): Mensaje a imprimir.
        """
        # Imprime el mensaje.
        self.print_message(message=message, message_type=MessageType.WARNING)
    
    def error(self, message:str) -> None:
        """
        Imprime un mensaje de error.

        Args:
            message (str): Mensaje a imprimir.
        """
        # Imprime el mensaje.
        self.print_message(message=message, message_type=MessageType.ERROR)