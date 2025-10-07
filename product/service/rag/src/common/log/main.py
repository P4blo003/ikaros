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
from typing import (Dict, Optional)
from pathlib import (Path)

# Externas:
import yaml


# ------------------------------
# CLASES
# ------------------------------

class LoggerManager:
    """
    Gestor de los loggers de la aplicación.

    Attributes:
        - configured (bool): True si esta configurado.
    """
    # -- Atributos -- #

    # Si esta configurado o no.
    configured:bool = False


    # -- Métodos -- #

    @classmethod
    def setup_logging(cls, config_path:str='config/log.yml'):
        """
        Establece la configuración a partir de un fichero dado.

        Args:
            config_path (str): Ruta realtiva o absoluta al fichero de configuración.
        """
        # Comprueba si ya esta configurado.
        if cls.configured:
            # Finaliza.
            return

        # Genera el path.
        file_path:Path = Path(config_path)

        # Try-Except para manejo de errores.
        try:
            
            # Carga la configuración desde el path.
            with file_path.open(mode='r', encoding='utf-8') as f:
                # Carga la configuración.
                config:Dict = yaml.safe_load(f)
            
            # Crea el directorio de logs si no existe.
            Path('logs').mkdir(exist_ok=True)

            # Aplica la configuración.
            logging.config.dictConfig(config=config)
            # Establece que se ha cargado la configuración.
            cls.configured = True

        # Si ocurre algún error.
        except Exception as e:
            # Establece una configuración por defecto.
            logging.basicConfig(level=logging.INFO)
            logging.error(f"Failed to load YAML configuration: {e}")

    @classmethod
    def get_logger(cls, name:Optional[str]=None, logger_type:str='default'):
        """
        Obtiene un logger configurado.

        Args:
            name (str): Nombre del módulo.
            logger_type (str): Tipo de ogger preconfigurado del YAML.
        """
        # Comprueba si no se ha cargado la configuracion.
        if not cls.configured:
            # Carga la configuración.
            cls.setup_logging()
        
        # Comprueba el tipo dado.
        if logger_type.lower() != "default":
            # Crea un logger preconfigurado por el tipo.
            return logging.getLogger(name=logger_type)
        
        # Crea un logger basado en el nombre del módulo.
        return logging.getLogger(name=name)