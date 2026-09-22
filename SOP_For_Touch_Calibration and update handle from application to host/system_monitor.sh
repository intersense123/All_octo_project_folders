#!/bin/sh

CALIB=/tmp/start_touch_calibration
UPDATE=/tmp/start_update

echo "System Monitor Started..."

while true
do
    if [ -f "$CALIB" ]; then

        echo "Calibration requested."

        rm -f "$CALIB"

        /home/torizon/Precigo/touch_calibration.sh

    fi

    if [ -f "$UPDATE" ]; then

        echo "Software update requested."

        rm -f "$UPDATE"

        /home/torizon/Precigo/update.sh

    fi

    sleep 1
done
