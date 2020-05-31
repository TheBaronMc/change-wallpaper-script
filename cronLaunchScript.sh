#!/bin/bash

PID=$(pgrep -n gnome-session)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

python3 /Path/script.py {CYCLIC | RANDOM}