#!/bin/bash

# Paths
PROJECT_DIR=$(dirname "$(realpath "$0")")
APPDIR="$PROJECT_DIR/AppDir"
OUTPUT_APPIMAGE="$PROJECT_DIR/Password_Generator-x86_64.AppImage"

echo "🔨 Building standalone binary with PyInstaller..."
source "$PROJECT_DIR/venv/bin/activate"
pyinstaller --onefile --noconsole pwdgenerator.py

echo "📦 Copying binary into AppDir..."
cp "$PROJECT_DIR/dist/pwdgenerator" "$APPDIR/pwdgenerator"
chmod +x "$APPDIR/pwdgenerator"

echo "⚙️  Updating AppRun..."
cat > "$APPDIR/AppRun" <<EOF
#!/bin/bash
HERE=\$(dirname "\$(readlink -f "\$0")")
exec "\$HERE/pwdgenerator"
EOF
chmod +x "$APPDIR/AppRun"

echo "🛠  Building AppImage..."
ARCH=x86_64 appimagetool "$APPDIR" "$OUTPUT_APPIMAGE"

echo "✅ AppImage created at: $OUTPUT_APPIMAGE"

