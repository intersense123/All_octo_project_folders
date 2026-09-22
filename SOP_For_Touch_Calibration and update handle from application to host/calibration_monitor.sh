#!/bin/sh

TRIGGER=/tmp/start_touch_calibration

echo "Calibration monitor started..."

while true
do
    if [ -f "$TRIGGER" ]; then

        echo "Calibration request received."

        rm -f "$TRIGGER"

        /home/torizon/Precigo/touch_calibration.sh
    fi

    sleep 1
done
