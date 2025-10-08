# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Descripción: Contiene las funcionalidades principales relacionadas
# con gRPC.
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
from logging import (Logger)

# Internas:
from common.log import (LoggerManager)


# ------------------------------
# CLASES
# ------------------------------

class GrpcServer:
    """
    Servidor gRPC. Inicializa las instancias necesarias y permite la ejecución y detención
    del servidor gRPC.
    """
    # -- Default -- #

    def __init__(self) -> None:
        """
        Inicializa las propiedades.
        """
        # -- Lógica -- #
        
        # Inicializa las propiedades.
        self.__logger:Logger = LoggerManager.get_logger('grpc_server')


    # -- Métodos -- #

    def start(self) -> None:
        """
        Inicia la ejecución del servidor gRPC.
        """
        # Imprime la información.
        self.__logger.info(msg="Running gRPC Server at port {} ...")

    def stop(self) -> None:
        """
        Detiene la ejecución del servidor gRPC.
        """
        # Imprime la información.
        self.__logger.info(msg="gRPC Server stopped.")