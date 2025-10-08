# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Descripción: Contiene las funcionalidades relacionadas con 
# el ciclo de vida de la aplicación.
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
import sys
import signal
from logging import (Logger)
from typing import (Callable, Optional, List)
from contextlib import (contextmanager)

# Internas:
from common.log import (LoggerManager)


# ------------------------------
# TIPOS
# ------------------------------

# Tipo para las funciones a llamar en el shutdown.
ShutdownHook = Callable[[], None]


# ------------------------------
# CLASES
# ------------------------------

class ApplicationLifeCycle:
    """
    Gestiona el ciclo de vida de la aplicación.
    """
    # -- Defauult -- #

    def __init__(self) -> None:
        """
        Inicializa el gestor de la aplicación.
        """
        # -- Variables -- #
        
        # Logger principal.
        self.__logger:Optional[Logger] = None
        self.__shutdown_requested:bool = False
        self.__shutdown_hooks:List[ShutdownHook] = []


    # -- Propiedades -- #

    @property
    def shutdown_requested(self) -> bool:
        """
        Comprueba si se ha solicitado un shutdown.

        Returns:
            bool: True si se ha solicitado y False en caso contrario.
        """
        # Retorna el valor.
        return self.__shutdown_requested

    # -- Métodos -- #

    def __signal_handler(self, signum:int, frame) -> None:
        """
        Manejador de señales para graceful shutdown.

        Args:
            signum (int): Código de la señal recibida.
            frame: 
        """
        # Comrprueba si ya ha sido solicitadeo el shutdown.
        if self.__shutdown_requested:
            # Finaliza.
            return
        
        # Establece el valor.
        self.__shutdown_requested = True

        # Obtiene el nombre de la señal.
        sig_name:str = signal.Signals(value=signum).name

        # Limpia la terminal.
        sys.stdout.write('\r\033[K')
        sys.stdout.flush()

        # Comprueba si el logger ha sido inicializado.
        if self.__logger:
            # Imprime la información.
            self.__logger.info(f"Gets {sig_name} signal. Starting shutdown ...")
        
        # Ejecuta el graceful shutdown.
        self.__execute_shutdown()
    
    def __execute_shutdown(self) -> None:
        """
        Ejecuta el gracful shutdown.
        """
        # -- Variables -- #

        # Listado con los errores.
        errors:List[Exception] = []

        # Comprueba si el logger ha sido inicializado.
        if self.__logger:
            # Imprime la información.
            self.__logger.info(f"Application must execute {len(self.__shutdown_hooks)} functions before complete the shutdown.")
        
        # Recorre las funciones.
        for hook in reversed(self.__shutdown_hooks):
            # Try-Except para manejo de errores.
            try:
                # Ejecuta la función.
                hook()
            
            # Si ocurre algún error.
            except Exception as e:
                # Añade el error.
                errors.append(e)
            
        # Comprueba si el logger ha sido inicializado.
        if self.__logger:
            # Comprueba si hubo errores.
            if errors:
                # Variable para mensaje de error.
                error_msg:str = ""

                # Perpara el mensaje de errores.
                for error in errors:
                    # Añade el error al mensaje.
                    error_msg += f"\t{error}\n"

                # Imprime el aviso.
                self.__logger.warning(f"Shutdown completed with {len(errors)} errors.\n{error_msg}")
            
            # Si no hubo errores.
            else:
                # Imprime la información.
                self.__logger.info("Shutdown complete with no errors.")
    
    def __setup_signals(self) -> None:
        """
        Inicializa y configura las señales.
        """
        # Inicializa la señal SIGINT.
        signal.signal(signalnum=signal.SIGINT, handler=self.__signal_handler)
        # Inicializa la señal SIGTERM.
        signal.signal(signalnum=signal.SIGTERM, handler=self.__signal_handler)

    def __setup_logging(self) -> None:
        """
        Inicializa la configuración de logging.
        """
        # -- Lógica -- #
        
        # Inicializa la configuración.
        error:Optional[Exception] = LoggerManager.setup_config()

        # Inicializa el logger.
        self.__logger = LoggerManager.get_logger('app')

        # Comprueba si hubo error durante la inicialización.
        if error:
            # Imprime el error.
            self.__logger.warning(f"Using default logger configuration: {error}")

    @contextmanager
    def managed_context(self):
        """
        Context manager para el ciclo de vida gestionado.
        """
        # Try-Except para manejo de errores.
        try:
            # Inicializa las señales.
            self.__setup_signals()

            # Inicializa el logging.
            self.__setup_logging()

            # Retorna.
            yield self

        # Si ocurre algún error.
        except Exception as e:
            # Comprueba si el logger ha sido inicializado.
            if self.__logger:
                # Imprime el error.
                self.__logger.error(f"Error during app execution: {e}")
            
            # Relanza el error.
            raise
            
        # Se ejecuta al final.
        finally:
            # Comprueba si no se ha solicitado el shutdown.
            if not self.__shutdown_requested:
                # Establece el valor.
                self.__shutdown_requested = True

                # Ejecuta el shutdown.
                self.__execute_shutdown()