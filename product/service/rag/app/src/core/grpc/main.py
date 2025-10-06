# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Creación: 06 Octubre 2025
# Última Edición: 06 Octubre 2025
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
import grpc
from typing import List
from concurrent import futures
from logging import Logger

# Internas:
from common.log import (get_factory)


# ------------------------------
# CLASES
# ------------------------------

class GrpcServer:
    """
    Servidor gRPC. Gestiona el servicio y servidor gRPC.
    """
    # -- Default -- #

    def __init__(self, service_name:str, port:int=50051, max_workers:int = 10, max_message_length:int = 100 * 1024 * 1024) -> None:
        """
        Inicializa las propiedades.

        Args:
            service_name (str): Nombre del servicio.
            port (int): Puerto del servidor gRPC (50051 por defecto.)
            max_workers (int): Número máximo de trabajadores (10 workers por defecto).
            max_message_length (int): Tamnaño máximo de mensajes (100 MB por defecto).
        """
        # Inicializa las propiedades.
        self.service_name:str = service_name
        self.port:int = port
        self.max_workers:int = max_workers
        self.max_message_length:int = max_message_length
        self.is_running:bool = False

        self.__logger:Logger = get_factory().get_logger(name=self.service_name)
        self.__server:grpc.Server = self.__create_grpc_server(max_message_length=self.max_message_length)
    

    # -- Métodos -- #

    def __create_grpc_server(self, max_message_length:int) -> grpc.Server:
        """
        Crea y configura el servidor gRPC.

        Args:
            max_message_length (int): Tamaño máximo del mensaje.
        Returns:
            grpc.Server: Servidor gRPC.
        """
        # Genera las opciones del servidor.
        options:List = [
            ('grpc.max_send_message_length', max_message_length),
            ('grpc.max_receive_message_length', max_message_length),
            ('grpc.max_current_streams', 1000),
            ('grpc.so_reuseport', 1),
            ('grpc.so_keepalive', 1)
        ]

        # Crea el servidor.
        server:grpc.Server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=self.max_workers),
            options=options
        )

        # Retorna el servidor creado.
        return server
    
    def stop(self) -> None:
        """
        Detiene el servidor gRPC.
        """
        # Comprueba si el servidor no está corriendo.
        if not self.is_running:
            # Imprime el aviso.
            self.__logger.warning(f"gRPC Server is not running.")
            # Finaliza.
            return

        # Establece que está detenido.
        self.is_running = False
        # Imprime la información.
        self.__logger.info("gRPC Server stopped.")

    def start(self) -> None:
        """
        Inicia el servidor de manera bloqueante.
        """
        # Comprueba si el servidor está corriendo.
        if self.is_running:
            # Imprime el aviso.
            self.__logger.warning(f"gRPC Server is already running at port {self.port}")
            # Finaliza.
            return

        # Establece que esta corriendo.
        self.is_running = True
        # Imprime la información.
        self.__logger.info(f"gRPC Server running at port {self.port}.")