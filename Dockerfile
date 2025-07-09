FROM ubuntu:22.04

# Prevent tzdata from prompting during install
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tzdata \
    python3 python3-pip python3-tk python3-venv python3-dev \
    libfuse2 libx11-dev libxext-dev libxrandr-dev \
    libxfixes-dev libxcursor-dev libxinerama-dev \
    libxi-dev libglib2.0-dev libgtk-3-dev \
    build-essential wget git curl file && \
    rm -rf /var/lib/apt/lists/*

# Install Python tools
RUN pip3 install --no-cache-dir pyinstaller customtkinter \
    git+https://github.com/AppImageCrafters/appimage-builder.git

# Install appimagetool
RUN wget -q https://github.com/AppImage/AppImageKit/releases/download/13/appimagetool-x86_64.AppImage \
    -O /usr/local/bin/appimagetool && \
    chmod +x /usr/local/bin/appimagetool

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . .

# Default command
CMD ["bash"]
