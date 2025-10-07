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
from typing import (Optional, Tuple, Dict)
from pathlib import (Path)

# Externas:
import yaml


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

        # Genera el path.
        p:Path = Path(config_path)
        # Estado de la función.
        status:int = 0
        # Error de la función.
        error:Optional[Exception] = None


        # -- Lógica -- #

        # Try-Except para manejo de errores.
        try:
            # Abre el fichero de configuración.
            with p.open(mode='r', encoding='utf-8') as f:
                # Carga los datos.
                config:Dict = yaml.safe_load(f)
            
            # Crea el directorio de logs si no existe.
            Path('logs').mkdir(exist_ok=True)

            # Aplica la configuración.
            logging.config.dictConfig(config=config)

            # Indica que está configurado.
            cls.configured = True

        # Si ocurre algún error.
        except Exception as e:
            # Establece el estado.
            status = 1
            # Establece el error.
            error = e
        
        # Finalmente.
        finally:
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