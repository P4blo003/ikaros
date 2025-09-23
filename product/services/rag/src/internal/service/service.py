# ------------------------------------------------------------
# Autor: Pablo González García
# Fecha: 23 Septiembre 2025
# Descripción: Contiene el flujo las funcionalidades y 
#       configuración del servicio gRPC.
# ------------------------------------------------------------


# ------------------------------
# IMPORTS
# ------------------------------

# Estándar:
import grpc
from concurrent import futures
from logging import Logger

# Internas:
from .model import ServiceConfig
from common.logger import create_logger
from proto.rag import (
    service_pb2,
    service_pb2_grpc
)


# ------------------------------
# CLASES
# ------------------------------

class RagServiceServicer(service_pb2_grpc.RagServiceServicer):
    """
    Implementación del servicio RAG gRPC.
    """
    # -- Default -- #

    def __init__(self) -> None:
        """
        Inicializa el servicio.
        """
        # Inicializa el logger.
        self.__logger:Logger = create_logger(name="rag-service-servicer")

        # TODO: Lógica de inicialización.
    

    # -- Funciones -- #

    def GetContext(self, request, context):
        """
        Implementación del método para obtener el contexto.
        """
        # Imprime información.
        self.__logger.info("Petición recibida.")
        # TODO: Lógica principal.


class ServiceManager:
    """
    Representa un gestor de servicios. Se encarga de inicializar el servidor gRPC
    y gestionar sus posibles errores.
    """
    # -- Default -- #

    def __init__(self) -> None:
        """
        Inicializa las propiedades.
        """
        # Inicializa el logger.
        self.__logger:Logger = create_logger(name="service-manager")

        # Inicializa el servicio.
        self.__servicer:service_pb2_grpc.RagServiceServicer = RagServiceServicer()
        # Inicializa el servidor.
        self.__server:grpc.Server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        # Establece la dirección.
        self.__server.add_insecure_port(f'[::]:50051')
        # Añade el servicio a servidor.
        service_pb2_grpc.add_RagServiceServicer_to_server(self.__servicer, 
                                                          self.__server)


    # -- Funciones -- #

    def serve(self) -> None:
        """
        Inicializa el servidor gRPC del servicio RAG.
        """
        # Inicia el servidor gRPC.
        self.__server.start()

        # Imprime información.
        self.__logger.info("Running gRPC service at [::]:50051")

        # Espera a que finalice el servidor gRPC.
        self.__server.wait_for_termination()

    def stop(self) -> None:
        """
        Detiene y libera recursos empleados.
        """
        # Comprueba si el servidor gRPC no es nulo.
        if self.__server:
            # Detiene el servidor gRPC.
            self.__server.stop(0)
            # Imprime información.
            self.__logger.info("gRPC Server finished.")
        
        # Imprime información.
        self.__logger.info("Finished.")