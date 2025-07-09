# Password Generator

A secure, portable password generator for Linux.
Use your **master password** and an optional custom phrase to generate strong, unique passwords.

This AppImage is **self-contained** — no Python or dependencies required.

---

## Features

* Stateless password generation (deterministic: same inputs → same output)
* Supports custom phrases for site-specific passwords
* Option to include symbols for stronger passwords
* Clean and minimal GUI built with **CustomTkinter**
* Fully portable AppImage — no installation needed

---

## Download & Run

1️ [Download Password\_Generator-x86\_64.AppImage](https://github.com/asellers3rd/releases/latest)
2️ Make it executable:

```bash
chmod +x Password_Generator-x86_64.AppImage
```

3️ Run the app:

```bash
./Password_Generator-x86_64.AppImage
```

---

## 🛠 Build From Source (For Developers)

### 1️ Clone the Repo

```bash
git clone https://github.com/asellers3rd/pwdgeneratorapp.git
cd pwdgeneratorapp
```

### 2️ Install Build Tools

Install Python + virtualenv + PyInstaller:

```bash
sudo apt install python3 python3-pip python3-venv -y
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install pyinstaller customtkinter
```

---

### 3️ Build the AppImage

Run the provided build script:

```bash
chmod +x build_appimage.sh
./build_appimage.sh
```

 This will create `Password_Generator-x86_64.AppImage` in the project root.

---

## 📂 Project Structure

```
pwdgeneratorapp/
├── AppDir/                   # AppImage directory
│   ├── AppRun                # AppImage entry point
│   ├── icon.png              # App icon
├── build_appimage.sh         # Build script
├── pwdgenerator.py           # Main Python app
├── icon.png                  # App icon
├── Password_Generator-x86_64.AppImage  # Built AppImage
```

---

## 📜 License

This project is licensed under the MIT License.
See [LICENSE](LICENSE) for details.
