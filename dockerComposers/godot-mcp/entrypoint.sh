#!/bin/bash
# Start Xvfb, then Godot editor — force X11, not Wayland

Xvfb :99 -screen 0 1280x1024x24 -ac +extension GLX +render &
XVFB_PID=$!
sleep 1

echo "Xvfb started on :99 (PID $XVFB_PID)"
echo "Starting Godot editor..."

export DISPLAY=:99
unset WAYLAND_DISPLAY
export GDK_BACKEND=x11
export QT_QPA_PLATFORM=xcb

exec /opt/godot/godot4 --editor --path /project --display-driver x11 --rendering-driver opengl3
