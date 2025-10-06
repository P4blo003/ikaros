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
from typing import (Optional)

# Internas:
from core.grpc import (GrpcServer)

from common.os.console import (Console)
from common.log import (LoggerFactory)
from common.log import (init_factory, get_factory)

# ------------------------------
# FUNCIONES
# ------------------------------

def init_singletons() -> None:
    """
    Inicializa los singletons del programa.
    """
    # Inicializa la factoría de loggers.
    init_factory()


# ------------------------------
# LÓGICA
# ------------------------------

# -- Lógica principal -- #
if __name__ == "__main__":

    # -- Variables -- #
    status_code:int = 0
    console:Optional[Console] = None
    grpc_server:Optional[GrpcServer] = None


    # -- Lógica principal -- #

    # Try-Except para manejo de errores.
    try:
        # Objeto para imprimir por consola.
        console = Console()

        # Inicializa singletons.
        init_singletons()

        # Inicializa el servidor gRPC.
        grpc_server = GrpcServer(service_name='RagGrpcServer')

        # Inicia el servicio.
        grpc_server.start()

    # Si se detecta Ctrl+C.
    except KeyboardInterrupt:
        pass
        
    # Si se detecta algún error.
    except Exception as e:
        # Comprueba si el objeto ha sido creado.
        if console:
            # Imprime la información.
            console.error(f"{e}")

        # Establece el estado.
        status_code = 1

    # Finalmente.
    finally:
        # Comprueba si el servidor gRPC ha sido inicializado.
        if grpc_server:
            # Detiene el servicio en caso de que este corriendo.
            grpc_server.stop()

        # Comprueba si el objeto ha sido inicializado.
        if console:
            # Imprime la información.
            console.info("Service shutdown complete.")

        # Finaliza el programa.
        sys.exit(status_code)