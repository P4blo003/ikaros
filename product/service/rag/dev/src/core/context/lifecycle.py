# ------------------------------------------------------------------------------------------
# Autor: Pablo González García.
# Descripción: Contiene las funcionalidades relacionadas
# con el ciclo de vida del programa.
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
from contextlib import contextmanager
from logging import Logger

# Internos:
from common.log import LoggerManager


# ------------------------------
# CLASES
# ------------------------------

class LifecycleManager:
    """
    Gestiona el ciclo de vida del programa.
    """
    # -- Default -- #
    
    def __init__(self) -> None:
        """
        Inicializa la instancia.
        """
        # -- Variables -- #
        self.__shutdown_requested:bool = False


    # -- Métodos -- #

    def __shutdown(self) -> None:
        """
        Realiza las tareas de cierre del programa.
        """
        # -- Lógica -- #

        # Comprueba si se ha solicitado el cierre.
        if self.__shutdown_requested:
            # Finaliza.
            return

        # Try-Except para manejo de errores.
        try:
            # Establece el cierre solicitado.
            self.__shutdown_requested = True

            # Imprime la información.
            self.__logger.info("Starting shutdown ...")

            # TODO: Implementar cierre del ciclo de vida.

            # Imprime la información.
            self.__logger.info("Shutdown completed.")

        # Si ocurre algún error.
        except Exception as e:
            # Imprime el error.
            self.__logger.error(f"Error during shutdown: {e}")

    @contextmanager
    def managed_context(self):
        """
        Contexto gestionado para el ciclo de vida del programa.
        """
        # -- Lógica -- #

        # Try-Except para manejo de errores.
        try:
            # Obtiene el logger.
            self.__logger:Logger = LoggerManager.get_logger('app')

            # Imprime la información.
            self.__logger.info("Starting lifecycle ...")

            # TODO: Implementar inicio del ciclo de vida.

            # Imprime la información.
            self.__logger.info("Lifecycle started.")

            # Retorna el contexto.
            yield self

        # Si ocurre algún error.
        except Exception as e:
            pass
        # Se ejecuta finalmente.
        finally:
            # Inicia el cierre.
            self.__shutdown()