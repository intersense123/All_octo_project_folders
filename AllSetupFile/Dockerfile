# ARGUMENTS --------------------------------------------------------------------
##
# Board architecture
##
ARG IMAGE_ARCH=

##
# Base container version
##
ARG BASE_VERSION=4

##
# Directory of the application inside container
##
ARG APP_ROOT=

FROM --platform=linux/${IMAGE_ARCH} \
    torizon/qt5-wayland:stable-rc AS deploy

ARG IMAGE_ARCH
ARG APP_ROOT

# your regular RUN statements here
# Install required packages
RUN apt-get -q -y update && \
    apt-get -q -y install \
    openssl \
    openssh-server \
    sqlite3 \
    python3-minimal \
    python3-pip \
    python3-venv \
    python3-pyside2.qtcore python3-pyside2.qtwidgets \
    python3-pyside2.qtgui -y python3-dbus \
    python3-sqlalchemy python3-spidev python3-libgpiod \
    python3-matplotlib python3-numpy \
# DO NOT REMOVE THIS LABEL: this is used for VS Code automation
    # __torizon_packages_prod_start__
    # __torizon_packages_prod_end__
# DO NOT REMOVE THIS LABEL: this is used for VS Code automation
    && apt-get clean && apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

# Create virtualenv
RUN python3 -m venv ${APP_ROOT}/.venv --system-site-packages

# Install pip packages on venv
COPY requirements-release.txt /requirements-release.txt
RUN . ${APP_ROOT}/.venv/bin/activate && \
    pip3 install --upgrade pip && pip3 install -r requirements-release.txt && \
    rm requirements-release.txt

# Copy the application source code in the workspace to the $APP_ROOT directory
# path inside the container, where $APP_ROOT is the torizon_app_root
# configuration defined in settings.json
COPY ./src ${APP_ROOT}/src

WORKDIR ${APP_ROOT}

ENV APP_ROOT=${APP_ROOT}
ENV QT_QPA_PLATFORM=wayland
ENV XDG_RUNTIME_DIR=/tmp/1000-runtime-dir
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND="noninteractive"

# Activate and run the code
CMD . ${APP_ROOT}/.venv/bin/activate && python3 -u src/main.py --no-sandbox
