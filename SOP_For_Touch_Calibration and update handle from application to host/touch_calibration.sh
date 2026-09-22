#!/bin/sh

set -e

echo "======================================"
echo "      TOUCH CALIBRATION START"
echo "======================================"

cd /home/torizon

echo "Stopping all running containers..."
docker stop $(docker ps -q) 2>/dev/null || true

sleep 2

echo "Removing old calibration container..."
docker rm -f touchcal 2>/dev/null || true

echo "Starting calibration..."

docker run -d \
    --name touchcal \
    -e HEAD=DPI-1 \
    --privileged \
    -v /dev:/dev \
    -v /run/udev:/run/udev \
    -v /etc/udev/rules.d:/etc/udev/rules.d \
    torizon/weston-touch-calibrator:3

COUNT=0

echo "Monitoring calibration..."

while true
do
    COUNT=$(docker logs touchcal 2>&1 | grep -c "applying calibration" || true)

    echo "Calibration count: $COUNT"

    if [ "$COUNT" -ge 3 ]; then
        echo "Calibration complete."

        sleep 2

        echo "Stopping calibration container..."
        docker stop touchcal || true

        docker rm -f touchcal || true

        echo "Rebooting in 5 seconds..."
        sleep 5

        reboot
        exit 0
    fi

    sleep 1
done
