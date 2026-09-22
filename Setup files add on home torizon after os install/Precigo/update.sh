#!/bin/bash

set -e

echo "======================================"
echo "        APPLICATION UPDATE"
echo "======================================"

HOST_COMPOSE="/home/torizon/docker-compose.yml"
TEMP_COMPOSE="/tmp/docker-compose.yml"

# ---------------------------------------------------------
# FIND docker-compose.yml FROM USB
# ---------------------------------------------------------
echo "Searching USB for docker-compose.yml ..."

USB_COMPOSE=""

for dir in /media/*; do

    if [ -d "$dir" ]; then

        echo "Checking USB: $dir"

        if [ -f "$dir/docker-compose.yml" ]; then
            USB_COMPOSE="$dir/docker-compose.yml"
            break
        fi

        if [ -f "$dir/docker-compose.yaml" ]; then
            USB_COMPOSE="$dir/docker-compose.yaml"
            break
        fi

    fi

done

if [ -z "$USB_COMPOSE" ]; then
    echo "ERROR: No docker-compose.yml found in USB"
    exit 1
fi

echo "Compose file found:"
echo "$USB_COMPOSE"

# ---------------------------------------------------------
# COPY USB COMPOSE TO TEMP
# ---------------------------------------------------------
cp "$USB_COMPOSE" "$TEMP_COMPOSE"

sync

# ---------------------------------------------------------
# CHECK APP IMAGE VERSION ONLY
# ---------------------------------------------------------
echo "Checking app image version..."

CURRENT_IMAGE=$(awk '
/app:/ {found=1}
found && /image:/ {
print $2
exit
}' "$HOST_COMPOSE")

NEW_IMAGE=$(awk '
/app:/ {found=1}
found && /image:/ {
print $2
exit
}' "$TEMP_COMPOSE")

echo "Current App Image: $CURRENT_IMAGE"
echo "New App Image    : $NEW_IMAGE"

CURRENT_NAME=$(echo "$CURRENT_IMAGE" | cut -d':' -f1)
CURRENT_TAG=$(echo "$CURRENT_IMAGE" | cut -d':' -f2)

NEW_NAME=$(echo "$NEW_IMAGE" | cut -d':' -f1)
NEW_TAG=$(echo "$NEW_IMAGE" | cut -d':' -f2)

# ---------------------------------------------------------
# VALIDATION
# ---------------------------------------------------------
if [ "$CURRENT_NAME" != "$NEW_NAME" ]; then
    echo "ERROR: Different app image detected"
    echo "Update cancelled"
    exit 1
fi

if [ "$CURRENT_TAG" = "$NEW_TAG" ]; then
    echo "Same app version already installed"
    exit 0
fi

echo "New app version detected"
echo "Updating from $CURRENT_TAG --> $NEW_TAG"

# ---------------------------------------------------------
# STOP OLD CONTAINERS
# ---------------------------------------------------------
echo "Stopping old containers..."

cd /home/torizon

docker compose down -v || true

sleep 5

# ---------------------------------------------------------
# COPY NEW COMPOSE FILE
# ---------------------------------------------------------
echo "Copying new docker-compose.yml ..."

cp "$TEMP_COMPOSE" "$HOST_COMPOSE"

sync

# ---------------------------------------------------------
# START NEW CONTAINERS
# ---------------------------------------------------------
echo "Starting new containers..."

docker compose up -d --remove-orphans

echo "Waiting for containers..."

sleep 20

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
