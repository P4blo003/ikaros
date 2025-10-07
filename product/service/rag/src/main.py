# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Descripción: Contiene las funcionalidades principales de la
# aplicación.
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
import sys
import signal
import time
from typing import (Optional)
from contextlib import (contextmanager)
from logging import (Logger)

# Internos:
from common.log import (LoggerManager)


# ------------------------------
# UTILIDADES
# ------------------------------

@contextmanager
def application_lifecycle():
    """
    Context manager para gestionar el ciclo de vida de la aplicación.
    Maneja la inicialización, ejecución y shutdown graceful.
    """
    # -- Variables -- #

    # Logger principal.
    logger:Optional[Logger] = None
    # Servidor gRPC.

    # Solicitud de finalización.
    shutdown_request:bool = False


    # -- Funciones -- #

    def signal_handler(signum:int, frame) -> None:
        """
        Manejador para señales de terminación.

        Args:
            signum (int): Identificador de la señal.
            frame:
        """
        # -- Variables -- #

        # Para saber si ya se está procesando una señal de terminación.
        nonlocal shutdown_request

        # Comprueba si ya se está manejando.
        if shutdown_request:
            # Retorna.
            return
        
        # Establece que se esta procesando.
        shutdown_request = True
        # Obtiene el nombre de la señal.
        signal_name:str = 'SIGINT' if signum == signal.SIGINT else 'SIGTERM'

        # Comprueba si el logger esta inicializado.
        if logger:
            # Imprime la información.
            logger.info(f"Signal {signal_name} received. Starting gracefull shutdown ...")

        # Limpieza del carácter C^.
        sys.stdout.write('\r\033[K')
        sys.stdout.flush()
    

    # -- Lógica -- #

    # Try-Except para manejo de errores.
    try:
        # Configura los manejadores de señales.
        signal.signal(signalnum=signal.SIGINT, handler=signal_handler)
        # Configura los manejadores de señales.
        signal.signal(signalnum=signal.SIGTERM, handler=signal_handler)

        # Inicializa el logger manager.
        status, error = LoggerManager.setup_config()

        # Inicializa el logger.
        logger = LoggerManager.get_logger('app')

        # Imprime la información.
        if status != 0:
            # Genera el mensaje.
            msg:str = "Couldn't load configuration from file. Using default configuration"
            # Comprueba si hay alguna excepción.
            if error:
                # Añade la excepción al mensaje.
                msg += f"because: {error}"

            # Imprime el aviso.
            logger.warning(msg)
        
        # Imprime la información.
        logger.info("Starting ...")

        # Retorna los valores generados.
        yield logger

    # Si ocurre algún error.
    except Exception as e:
        # Comprueba si el logger esta inicializado.
        if logger:
            # Imprime información.
            logger.error(f"Error occurred during initialization: {e}")
        
        # Relanza la excepción.
        raise

    # Finalmente.
    finally:
        # Comprueba si el logger esta inicializado.
        if logger:
            # Imprime información.
            logger.info(f"Starting gracefull shutdown ...")
        
        # Obtiene el tiempo inicial.
        shutdown_start:float = time.time()

        # Try-Except para manejo de errores.
        try:
            # Coprueba si el servidor está inicializado.
            pass

        # Si ocurre algún error.
        except Exception as e:
            # Comprueba si el logger esta inicializado.
            if logger:
                # Imprime información.
                logger.error(f"Error occurred during shutdown: {e}")
            
        # Finalmente.
        finally:
            # Obtiene la duración.
            shutdown_time:float = time.time() - shutdown_start

            # Comprueba si el logger esta inicializado.
            if logger:
                # Imprime información.
                logger.info(f"Shutdown complete in %.2fs", shutdown_time)


# ------------------------------
# FUNCIONES
# ------------------------------

def main() -> int:
    """
    Lógica principal de la aplicación. Retorna 0 en caso de ejecución exitosa y mayor que 0
    en caso de que ocurra algún error.
    """
    # Inicializa el contexto de la aplicación.
    with application_lifecycle() as (logger):
        # Try-Except para manejo de errores.
        try:
            pass
            # Retorna ejecución exitos.
            return 0

        # Si ocurre algún error.
        except Exception as e:
            # Imprime el error.
            logger.critical(f"Critical error during the execution: {e}")
            # Retorna ejecución fallida.
            return 1
        


# ------------------------------
# LÓGICA
# ------------------------------

# Comprueba que se esta ejecutando como main.
if __name__ == "__main__":

    # Try-Except para manejo de errores.
    try:
        # Obtiene el código de ejecución.
        exit_code:int = main()
        # Finaliza el programa.
        sys.exit(exit_code)

    # Si ocurre algún error.
    except Exception as e:
        # Imprime el error.
        print(f"Fatal error during initialization: {e}")

        # Finaliza el programa.
        sys.exit(2)