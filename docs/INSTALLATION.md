# 📦 Installation Guide

## 🚀 Quick Installation

### Method 1: Direct Download
```bash
# Download the repository
git clone https://github.com/GTRONICK/QSS.git
cd QSS

# Install Python dependencies
pip install -r requirements.txt

# Run the theme tester
python theme_tester.py
```

### Method 2: Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv qss-env

# Activate virtual environment
# On Linux/Mac:
source qss-env/bin/activate
# On Windows:
qss-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python theme_tester.py
```

## 🔧 System Requirements

### Minimum Requirements
- **Python**: 3.8 or higher
- **PyQt6**: 6.4.0 or higher
- **RAM**: 512 MB
- **Storage**: 50 MB

### Recommended Requirements
- **Python**: 3.10+
- **PyQt6**: 6.5.0+
- **RAM**: 1 GB
- **Storage**: 100 MB

## 🖥️ Platform-Specific Instructions

### Windows
```powershell
# Install Python from python.org
# Then run:
pip install PyQt6
git clone https://github.com/GTRONICK/QSS.git
cd QSS
python theme_tester.py
```

### macOS
```bash
# Install using Homebrew
brew install python
pip3 install PyQt6

# Clone and run
git clone https://github.com/GTRONICK/QSS.git
cd QSS
python3 theme_tester.py
```

### Linux (Ubuntu/Debian)
```bash
# Install dependencies
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Install PyQt6
pip3 install PyQt6

# Clone and run
git clone https://github.com/GTRONICK/QSS.git
cd QSS
python3 theme_tester.py
```

### Linux (Arch/Manjaro)
```bash
# Install from AUR
yay -S python-pyqt6

# Or using pip
pip install PyQt6

# Clone and run
git clone https://github.com/GTRONICK/QSS.git
cd QSS
python theme_tester.py
```

## 🔍 Troubleshooting

### Common Issues

#### "ModuleNotFoundError: No module named 'PyQt6'"
```bash
# Solution:
pip install PyQt6
# or
pip3 install PyQt6
```

#### "Permission denied" on Linux
```bash
# Make script executable:
chmod +x theme_tester.py
./theme_tester.py
```

#### Virtual environment issues
```bash
# Recreate virtual environment:
rm -rf qss-env
python -m venv qss-env
source qss-env/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

## ✅ Verification

### Test Installation
```bash
# Check Python version
python --version

# Check PyQt6 installation
python -c "import PyQt6; print('PyQt6 installed successfully')"

# Run theme tester
python theme_tester.py
```

### Expected Output
- Theme tester window opens
- All themes load without errors
- Widgets display correctly
- No console errors

## 🔄 Updates

### Update to Latest Version
```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Run updated version
python theme_tester.py
```

## 🆘 Getting Help

If you encounter issues:
1. Check this troubleshooting guide
2. Search existing GitHub issues
3. Create a new issue with:
   - Your OS and version
   - Python version
   - PyQt6 version
   - Error messages
   - Steps to reproduce
