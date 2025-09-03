#!/usr/bin/env python3
"""
Run the QSS Theme Tester application with error handling
"""

import sys
import os
from pathlib import Path

def check_requirements():
    """Check requirements"""
    try:
        import PyQt6
        print(f"✅ PyQt6 available - version: {PyQt6.QtCore.PYQT_VERSION_STR}")
        return True
    except ImportError:
        print("❌ PyQt6 not installed")
        print("To install PyQt6, use the command:")
        print("pip install PyQt6")
        return False

def main():
    """Run the application"""
    print("🚀 Starting QSS Theme Tester...")
    
    if not check_requirements():
        return 1
    
    # Add current directory to Python path
    current_dir = Path(__file__).parent
    sys.path.insert(0, str(current_dir))
    
    try:
        from theme_tester import main as run_app
        run_app()
    except Exception as e:
        print(f"❌ Error running application: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
