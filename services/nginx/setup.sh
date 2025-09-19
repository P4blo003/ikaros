#!/usr/bin/env bash

# ------------------------------------------------------------
# File: install.sh
# Author: Pablo González García
# Description: Script para configurar e inicializar
# nginx.
# ------------------------------------------------------------s


# ------------------------------
# CONFIGURACIÓN
# ------------------------------

# -e: El script se detiene inmediatamente si cualquier comando devuelve
# un código de error diferente de 0.
# -u: Si se usa una variable no definida, el script falla.
# -o pipefail: Si cualquier comando falla, el pipeline falla.
set -euo pipefail

# Controla como bash divide cadenas de palabras. Solo divide en líneas
# o tabulaciones, ignorando espacios.
IFS=$'\n\t'

# Ruta al fichero de instalación.
INSTALL_DIR="./install.sh"


# ------------------------------
# FUNCIONES
# ------------------------------

# Imprime mensaje de información.
info() { echo -e "[\e[34mINFO\e[0m] $*";}
# Imprime mensaje de exito.
success() { echo -e "[\e[32mSUCCESS\e[0m] $*";}
# Imprime mensaje de error.
error() { echo -e "[\e[31mERROR\e[0m] $*">&2; exit 1;}

# Imprime el título con un formato específico.
print_h1() {
    # Título.
    local title="$1"
    # Ancho de la terminal.
    local width=$(tput cols)
    # Espaciado del título.
    local padding=$(( (width - ${#title}) / 2 ))

    print_splitter "$width"
    printf '%*s%s%*s\n' "$padding" '' "$title" "$padding" ''
    print_splitter "$width" && echo
}

# Imprime un separador varias veces en la misma línea.
print_splitter() {
    # Ancho de la terminal.
    local width="$1"

    # Imprime el separador.
    printf '=%.0s' $(seq 1 "$width") && echo
}


# ------------------------------
# FLUJO PRINCIPAL
# ------------------------------

# Imprime la cabecera.
print_h1 "NGINX SETUP"
# Imprime información.
echo "Starting nginx installation ..."
# Ejecuta el script de instalación.
print_splitter "$(( $(tput cols) / 2 ))"
bash "$INSTALL_DIR"
print_splitter "$(( $(tput cols) / 2 ))"