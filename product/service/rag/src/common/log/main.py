# ------------------------------------------------------------------------------------------
# Autor: Pablo González García
# Descripción: Contiene las funcionalidades principales de los
# loggers.
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
import logging.config
from typing import (Optional, Any, Tuple, Dict)
from pathlib import (Path)

# Externas:
import yaml


# ------------------------------
# VARIABLES
# ------------------------------

DEFAULT_LOGGING_CONFIG: Dict[str, Any] = {
    # Versión del esquema de configuración. Siempre usar 1.
    # Garantiza la compatibilidad con versiones futuras.
    "version": 1,
    
    # Gestiona los loggers previamente creados antes de establecer
    # la configuración.
    "disable_existing_loggers": False,
    
    # Configuración de los formatos.
    "formatters": {
        # Formato estándar.
        "standard": {
            # Formato del mensaje.
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            # Formato de la fecha del mensaje.
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        # Formato detallado.
        "detailed": {
            # Formato del mensaje.
            "format": "%(asctime)s [%(levelname)s] %(name)s - %(lineno)d: %(message)s",
            # Formato de la fecha del mensaje.
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    
    # Configuración de los handlers.
    "handlers": {
        # Handler básico para consola: Solo INFO y superior.
        "console_info": {
            # Clase del handler.
            "class": "logging.StreamHandler",
            # Mínimo nivel de severidad.
            "level": "INFO",
            # Formato.
            "formatter": "standard",
            # Salida por consola.
            "stream": "ext://sys.stdout"
        },
        
        # Handler para consola en desarrollo.
        "console_debug": {
            # Clase del handler.
            "class": "logging.StreamHandler",
            # Mínimo nivel de severidad.
            "level": "DEBUG",
            # Formato.
            "formatter": "detailed",
            # Salida por consola.
            "stream": "ext://sys.stdout"
        },
        
        # Handler para errores en consola.
        "console_error": {
            # Clase del handler.
            "class": "logging.StreamHandler",
            # Mínimo nivel de severidad.
            "level": "ERROR",
            # Formato.
            "formatter": "detailed",
            # Salida por consola.
            "stream": "ext://sys.stderr"
        },
        
        # Archivo para el servicio gRPC.
        "grpc_file": {
            # Clase del handler.
            "class": "logging.handlers.RotatingFileHandler",
            # Mínimo nivel de severidad.
            "level": "DEBUG",
            # Formato.
            "formatter": "standard",
            # Nombre del fichero.
            "filename": "logs/grpc.log",
            # Tamaño máximo del fichero.
            "maxBytes": 10485760,   # 10MB.
            # Número de backups.
            "backupCount": 3,
            # Codificación.
            "encoding": "utf-8"
        },
        
        # Archivo para errores.
        "error_file": {
            # Clase del handler.
            "class": "logging.handlers.RotatingFileHandler",
            # Mínimo nivel de severidad.
            "level": "ERROR",
            # Formato.
            "formatter": "detailed",
            # Nombre del fichero.
            "filename": "logs/error.log",
            # Tamaño máximo del fichero.
            "maxBytes": 5242880,   # 5MB.
            # Número de backups.
            "backupCount": 10,
            # Codificación.
            "encoding": "utf-8"
        }
    },
    
    # Configuración de los loggers.
    "loggers": {
        # Logger raíz: Captura todo lo no especificado.
        "": {
            # Handlers del logger.
            "handlers": ["console_info", "error_file"],
            # Mínimo nivel de severidad.
            "level": "WARNING",
            # Indica si los mensajes se envían o no al padre (en este caso
            # no hay pero es buena práctica).
            "propagate": False
        },
        
        # Logger principal.
        "app": {
            # Handlers del logger.
            "handlers": ["console_info", "error_file"],
            # Mínimo nivel de severidad.
            "level": "INFO",
            # Indica si los mensajes se envían o no al padre (en este caso
            # no hay pero es buena práctica).
            "propagate": False
        },
        
        # Logger para el servicio gRPC.
        "grpc_server": {
            # Handlers del logger.
            "handlers": ["console_info", "grpc_file", "error_file"],
            # Mínimo nivel de severidad.
            "level": "DEBUG",
            # Indica si los mensajes se envían o no al padre (en este caso
            # no hay pero es buena práctica).
            "propagate": False
        }
    }
}


# ------------------------------
# CLASES
# ------------------------------

class LoggerManager:
    """
    Gestor de los loggers de la aplicación. Permite cargar configuraciones de ficheros
    'yaml'.

    Attributes:
        configured (bool): Si esta configurado o no.
    """
    # -- Atributos -- #

    # Indica si esta configurado o no.
    configured:bool = False


    # -- Métodos -- #

    @classmethod
    def setup_config(cls, config_path:str='config/log.yml') -> Tuple[int, Optional[Exception]]:
        """
        Establece la configuración de los loggers. Intenta cargar la configuración desde el fichero
        o carga una configuración por defecto en caso de que no se pueda.

        Args:
            config_path (str): Ruta (Relativa/Absoluta) al fichero de configuración.
        Returns:
            Tuple[int,Optional[Exception]]: Tupla con el estado de la función y el error (en caso de que haya habido alguno).

                - int: Indica si se cargo correctamente el fichero o no.
                - Optional[Exception]: Error en caso de que hubiera alguno.
        """
        # -- Variables -- #

        # Configuración global por defecto.
        global DEFAULT_LOGGING_CONFIG

        # Genera el path.
        p:Path = Path(config_path)
        # Estado de la función.
        status:int = 0
        # Error de la función.
        error:Optional[Exception] = None
        # Configuración.
        config:Dict[str, Any] = DEFAULT_LOGGING_CONFIG


        # -- Lógica -- #

        # Try-Except para manejo de errores.
        try:
            # Crea el directorio de logs si no existe.
            Path('logs').mkdir(exist_ok=True)
            
            # Abre el fichero de configuración.
            with p.open(mode='r', encoding='utf-8') as f:
                # Carga los datos.
                config = yaml.safe_load(f)

        # Si ocurre algún error.
        except Exception as e:
            # Establece el estado.
            status = 1
            # Establece el error.
            error = e
            # Establece la configuración por defecto.
            logging.config.dictConfig(config=DEFAULT_LOGGING_CONFIG)

        # Finalmente.
        finally:
            # Aplica la configuración.
            logging.config.dictConfig(config=config)
            # Indica que está configurado.
            cls.configured = True
            # Retorna la tupla.
            return status, error
    
    @classmethod
    def get_logger(cls, name:Optional[str]=None, logger_type:str='default') -> logging.Logger:
        """
        Genera un logger configurado.

        Args:
            name (str): Nombre del módulo.
            logger_type (str): Tipo de ogger preconfigurado del YAML.
        """
        # -- Lógica -- #

        # Comprueba si no esta configurado.
        if not cls.configured:
            # Configura el logger.
            cls.setup_config()
        
        # Comprueba el tipo dado.
        if logger_type.lower() != "default":
            # Crea un logger preconfigurado por el tipo.
            return logging.getLogger(name=logger_type)
        
        # Crea un logger basado en el nombre del módulo.
        return logging.getLogger(name=name)