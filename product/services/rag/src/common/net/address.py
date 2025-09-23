# ------------------------------
# FUNCIONES
# ------------------------------

# Estándar:
from typing import List
from enum import Enum


# ------------------------------
# ENUMS
# ------------------------------

class IP_VERSION(Enum):
    """
    Representa la versión IP empleada.

    Attributes:
        IP_V4: Ip versión 4.
        IP_V6: Ip versión 6.
    """
    # -- Attributes -- #
    IP_V4 = 0
    IP_V6 = 1


# ------------------------------
# FUNCIONES
# ------------------------------

def check_ip(ip:str, version:IP_VERSION=IP_VERSION.IP_V4) -> bool:
    """
    Comprueba si la IP dada es válida o no.

    Args:
        ip (str): Ip a comprobar.
        version (IP_VERSION): Versión de IP empleada.
    """
    # Comprueba si está vacía.
    if ip == "":
        # Retorna falso.
        return False
    
    # Comprueba si la versión es ip versión 4.
    if version == IP_VERSION.IP_V4:
        # Separa la IP en cada uno de sus valores.
        parts:List[str] = ip.split('.')
        # Comprueba que no tenga 4 partes.
        if len(parts) != 4:
            # Retorna falso.
            return False
        # Try-except para maenejo de errores.
        try:
            # Recorre las partes obtenidas.
            for part in parts:
                # Convierte la parte en entero.
                part_as_integer:int = int(part)
                # Comprueba si no está dentro del rango.
                if part_as_integer < 0 or part_as_integer > 255:
                    # Retorna falso.
                    return False

            # Retorna cierto.
            return True

        # Si ocurre algún ValueError.
        except ValueError:
            # Retorna falso.
            return False
        
    # Comprueba si la versión es ip versión 6.
    elif version == IP_VERSION.IP_V6:
        # TODO: Implementar lógica.
        return False