# ------------------------------------------------------------------------------------------
# Autor: Pablo González García.
# Descripción: Contiene las funcionalidades principales
# relacionadas con el logging del sistema.
# ------------------------------------------------------------------------------------------


# ------------------------------
# MÓDULOS
# ------------------------------

# Estándar:
import logging.config
from typing import (Optional, Dict, Any)
from pathlib import Path

# Internos:
from .default import DEFAULT_LOGGING_CONFIG

# Externos:
import yaml


# ------------------------------
# CLASES
# ------------------------------

class LoggerManager:
    """
    Clase que gestiona los loggers del programa. Permite configurar y obtener loggers.
    """
    # -- Atributos -- #

    # Indica si se ha cargado alguna configuración.
    _configured: bool = False


    # -- Métodos -- #

    @classmethod
    def setup_config(cls, cfg_file:Optional[str] = None) -> Optional[Exception]:
        """
        Configura el formato y salidas de los loggers del programa. Si se pasa un fichero de configuración,
        intenta cargarlo. Si no, usa una configuración por defecto.

        Args:
            cfg_file (Optional[str]): Ruta al fichero de configuración. Si es None, usa configuración por defecto.

        Returns:
            Optional[Exception]: Excepción si ocurre algún error, None en caso contrario.
        """
        # -- Variables -- #

        # Para almacenar el error si ocurre.
        error:Optional[Exception] = None
        # Para almacenar la configuración a cargar.
        cfg:Dict[str, Any] = DEFAULT_LOGGING_CONFIG
        # Para almacenar el path del fichero de configuración.
        p:Optional[Path] = None


        # -- Lógica -- #

        # Try-Except para manejo de errores.
        try:
            # Crea la carpeta de logs si no existe.
            Path('logs').mkdir(exist_ok=True)

            # Comprueba si se ha pasado un fichero de configuración.
            if cfg_file:
                # Crea el path.
                p = Path(cfg_file)

                # Apre el fichero en modo lectura.
                with p.open('r', encoding='utf-8') as f:
                    # Carga la configuración desde el fichero.
                    cfg = yaml.safe_load(f)

        # Si ocurre algún error.
        except Exception as e:
            # Establece el error.
            error = e
        
        # Se ejecuta finalmente.
        finally:
            # Establece la configuración.
            logging.config.dictConfig(cfg)
            # Establece que se ha configurado.
            cls._configured = True

            # Retorna el error (si existe).
            return error
    
    @classmethod
    def get_logger(cls, name:str) -> logging.Logger:
        """
        Obtiene un logger con el nombre especificado.

        Args:
            name (str): Nombre del logger.

        Returns:
            logging.Logger: Logger con el nombre especificado.
        """
        # Comprueba si no se ha configurado.
        if not cls._configured:
            # Configura el logging.
            cls.setup_config()

        # Retorna el logger.
        return logging.getLogger(name)