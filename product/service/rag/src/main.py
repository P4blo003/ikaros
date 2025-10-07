# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Descripción: Contiene el flujo principal de la aplicación.
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
from typing import (Optional)
from logging import (Logger)

# Internos:
from common.log import (LoggerManager)
from core.grpc import (GrpcServer)


# ------------------------------
# LÓGICA
# ------------------------------

# Comprueba si se está llamando como script.
if __name__ == "__main__":

    # -- Variables -- #

    # Logger principal.
    logger:Optional[Logger] = None
    # Servidor gRPC.
    grpc_server:Optional[GrpcServer] = None


    # -- Lógica principal -- #

    # Try-Except para manejo de errores.
    try:
        # Inicializa la configuración del logger.
        LoggerManager.setup_logging()
        # Inicializa el logger.
        logger = LoggerManager.get_logger(name='main')

        # Inicializa el servidor gRPC.
        grpc_server = GrpcServer()
        # Inicia el servidor.
        grpc_server.start()

    # Si se detecta Ctrl+C.
    except KeyboardInterrupt:
        pass

    # Si se detecta cualquier error.
    except Exception as e:
        # Comprueba si se ha creado el logger.
        if logger:
            # Imprime el error.
            logger.error(f"{type(e).__name__}: {e}")

    # Se ejecuta finalmente.
    finally:
        # Comprueba si se ha creado el servidor.
        if grpc_server:
            # Detiene el servidor.
            grpc_server.stop()
