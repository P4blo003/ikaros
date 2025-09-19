#!/usr/bin/env bash

# ------------------------------------------------------------
# File: install.sh
# Author: Pablo González García
# Description: Script para instalar nginx.
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


# ------------------------------
# FUNCIONES
# ------------------------------

# Imprime mensaje de información.
info() { echo -e "[\e[34mINFO\e[0m] $*";}
# Imprime mensaje de exito.
success() { echo -e "[\e[32mSUCCESS\e[0m] $*";}
# Imprime mensaje de error.
error() { echo -e "[\e[31mERROR\e[0m] $*">&2; exit 1;}

# Comprueba el sistema operativo.
check_os() {
    # Imprime información.
    info "Checking so ..."

    # Comprueba el fichero de información.
    if [[ -f /etc/os-release ]]; then
        # Ejecuta el contenido del archivo.
        . /etc/os-release
        # Almacena el ID del SO.
        OS_ID=$ID
    else
        error "Couldn't detect OS."
    fi

    # Case para saber el SO.
    case "$OS_ID" in
        ubuntu|debain)
            PKG_INSTALL="sudo apt update && sudo apt install -y nginx"
            SERVICE_CMD="sudo systemctl enable --now nginx"
            ;;
        centos|rhel|fedora)
            PKG_INSTALL="sudo dnf install -y nginx || sudo dnf yum install -y nginx"
            SERVICE_CMD="sudo systemctl enable --now nginx"
            ;;
        *)
            error "SO not supported -> \e[33m$OS_ID\e[0m"
            ;;
    esac

    # Imprime información.
    success "SO detected -> \e[33m$OS_ID\e[0m"
}
# Comprueba el acceso a internet.
check_internet() {
    # Imprime información.
    info "Checking internet connection ..."
    # Comprueba con un ping.
    if ! ping -c 2 8.8.8.8 &>/dev/null; then
        # Imprime error.
        error "There is no conection. Check your net."
    fi
    # Imprime exito.
    success "Net connection available."
}

# Comprueba si nginx esta instalado.
check_nginx_installed() {

    # Comprueba el comando.
    if command -v nginx &>/dev/null; then
        return 0
    else
        return 1
    fi
}

# Instala nginx.
install_nginx() {
    # Comprueba si nginx esta instalado.
    if ! check_nginx_installed; then
        # Imprime información.
        info "Installing nginx ..."
        # Instala nginx.
        eval "$PKG_INSTALL"
        # Imprime éxito.
        success "Nginx installed."
    else
        # Imprime información.
        info "Nginx is already installed."
    fi
}

# Inicia el servicio de nginx.
start_nginx() {
    # Imprime información
    info "Starting and enabling nginx service ..."
    if eval "$SERVICE_CMD"&>/dev/null; then
        # Imprime éxito.
        success "Nginx started and enabled."
    else
        # Imprime error.
        error "Nginc couldn't be started and enabled."
    fi
}


# ------------------------------
# FLUJO PRINCIPAL
# ------------------------------

# Obtiene el sistema operativo.
check_os
# Comprueba si hay acceso a internet.
check_internet
# Instala nginx.
install_nginx
# Inicia el servicio de nginx.
start_nginx