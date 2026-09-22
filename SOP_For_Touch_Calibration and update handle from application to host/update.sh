#!/bin/bash
set -e

HOST_COMPOSE="/home/torizon/docker-compose.yml"

echo "======================================"
echo "      APPLICATION UPDATE START"
echo "======================================"

export HOME=/root
export DOCKER_CONFIG=/root/.docker

cd /home/torizon || exit 1

USB_COMPOSE=""

for dir in /media/*; do
    if [ -f "$dir/docker-compose.yml" ]; then
        USB_COMPOSE="$dir/docker-compose.yml"
        break
    fi
done

if [ -z "$USB_COMPOSE" ]; then
    echo "No docker-compose.yml found on USB"
    exit 1
fi

echo "Stopping containers..."
docker compose -f "$HOST_COMPOSE" down -v || true

sleep 3

echo "Copying compose..."
cp "$USB_COMPOSE" "$HOST_COMPOSE"
sync

echo "Compose images:"
docker compose -f "$HOST_COMPOSE" config --images

echo "Pulling images..."
docker compose -f "$HOST_COMPOSE" pull

echo "Starting containers..."
docker compose -f "$HOST_COMPOSE" up -d

echo "Update completed."


sleep 4
# ---------------------------------------------------------
# SHOW RUNNING CONTAINERS
# ---------------------------------------------------------
echo "Running containers:"
docker ps

# ---------------------------------------------------------
# FIND WESTON CONTAINER
# ---------------------------------------------------------
WESTON_CONTAINER=$(docker ps --format '{{.Names}}' | grep weston | head -n 1)

if [ -z "$WESTON_CONTAINER" ]; then
    echo "ERROR: Weston container not running"
    exit 1
fi

echo "Weston container found:"
echo "$WESTON_CONTAINER"

# ---------------------------------------------------------
# UPDATE weston.ini INSIDE CONTAINER
# ---------------------------------------------------------
echo "Updating weston.ini ..."

docker exec "$WESTON_CONTAINER" rm -f /etc/xdg/weston/weston.ini

docker exec -i "$WESTON_CONTAINER" sh -c 'cat > /etc/xdg/weston/weston.ini' << 'EOF'
[core]
idle-time=0
require-input=false
xwayland=true
modules=screen-share.so
# uncomment line below to use kiosk shell
#shell=kiosk-shell.so

[shell]
background-image=/home/torizon/custom/Loading.png
background-color=0x00000000
panel-position=none
locking=false
allow-zap=false
num-workspaces=1

[keyboard]
vt-switching=false

# uncomment the [output] line below if you set any output configuration
#[output]
#name=HDMI-A-1
#transform=rotate-90
#app-ids=my-app-id
#mode=off
#mode=1680x1050@60

[screen-share]
command=/usr/bin/weston --no-config --backend=rdp-backend.so --shell=fullscreen-shell.so --rdp-tls-key=/var/volatile/tls.key --rdp-tls-cert=/var/volatile/tls.crt --no-clients-resize --force-no-compression
start-on-startup=true
EOF

echo "weston.ini updated successfully"

sync

# ---------------------------------------------------------
# FINAL STATUS
# ---------------------------------------------------------
echo "Final running containers:"
docker ps

echo "======================================"
echo " UPDATE SUCCESSFUL - REBOOTING "
echo "======================================"

sleep 5

reboot
