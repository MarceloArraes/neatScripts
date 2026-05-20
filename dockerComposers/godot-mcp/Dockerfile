FROM ubuntu:22.04

# X11 + GL libs needed for Godot to connect to Xvfb
RUN apt-get update && apt-get install -y --no-install-recommends \
    xvfb wget unzip ca-certificates \
    libx11-6 libxcursor1 libxi6 libxinerama1 libxrandr2 \
    libgl1-mesa-glx libgl1 libegl1 libglib2.0-0 \
    libfreetype6 libfontconfig1 libasound2 \
    && rm -rf /var/lib/apt/lists/*

ARG GODOT_VERSION=4.4-stable

RUN mkdir -p /opt/godot && \
    wget -q "https://github.com/godotengine/godot/releases/download/${GODOT_VERSION}/Godot_v${GODOT_VERSION}_linux.x86_64.zip" \
         -O /tmp/godot.zip && \
    unzip -q /tmp/godot.zip -d /opt/godot/ && \
    mv /opt/godot/Godot_v${GODOT_VERSION}_linux.x86_64 /opt/godot/godot4 && \
    chmod +x /opt/godot/godot4 && \
    rm /tmp/godot.zip

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /project

ENTRYPOINT ["/entrypoint.sh"]
