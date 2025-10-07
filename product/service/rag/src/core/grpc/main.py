# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Descripción: Contiene las funcionalidades principales del
# servicio gRPC.
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
import grpc
from logging import (Logger)

# Internos:
from common.log import (LoggerManager)


# ------------------------------
# CLASES
# ------------------------------

class GrpcServer:
    """
    Servidor gRPC. Se encarga de gestionar todo lo necesario para poder iniciar y detener
    un servicio gRPC en un puerto dado.
    """
    # -- Default -- #

    def __init__(self, port:int=50051) -> None:
        """
        Inicializa las propiedades.

        Args:
            port (int): Puerto en el que escucha el servidor gRPC.
        """
        # Inicializa las propiedades.
        self.__logger:Logger = LoggerManager.get_logger(name='grpc_server')
        self.port:int = port
    

    # -- Métodos -- #

    def start(self) -> None:
        """
        Inicializa el servidor gRPC.
        """
        # Imprime la información.
        self.__logger.info(f"Server running at port {self.port}.")
    
    def stop(self) -> None:
        """
        Detiene el servidor gRPC.
        """
        # Imprime la información.
        self.__logger.info("Server stopped.")