#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GST App - Quick Setup Script
इस script को run करने से पूरा setup हो जाएगा
"""

import os
import sys
import subprocess
import platform

def print_header(text):
    print("\n" + "="*50)
    print(text)
    print("="*50)

def print_success(text):
    print("✅ " + text)

def print_error(text):
    print("❌ " + text)

def print_info(text):
    print("ℹ️  " + text)

def check_python():
    """Check if Python 3.8+ is installed"""
    print_header("Checking Python Version")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print_error(f"Python 3.8+ required. You have {version.major}.{version.minor}")
        return False
    
    print_success(f"Python {version.major}.{version.minor}.{version.micro} found")
    return True

def create_venv():
    """Create virtual environment"""
    print_header("Creating Virtual Environment")
    
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print_success("Virtual environment created")
        return True
    except Exception as e:
        print_error(f"Failed to create venv: {e}")
        return False

def get_pip_command():
    """Get pip command based on OS"""
    if platform.system() == "Windows":
        return [os.path.join("venv", "Scripts", "pip")]
    else:
        return [os.path.join("venv", "bin", "pip")]

def install_requirements():
    """Install dependencies"""
    print_header("Installing Dependencies")
    
    try:
        pip_cmd = get_pip_command()
        
        # Upgrade pip
        print_info("Upgrading pip...")
        subprocess.run(pip_cmd + ["install", "--upgrade", "pip"], check=True)
        print_success("pip upgraded")
        
        # Install requirements
        print_info("Installing requirements...")
        subprocess.run(pip_cmd + ["install", "-r", "requirements.txt"], check=True)
        print_success("Dependencies installed")
        
        return True
    except Exception as e:
        print_error(f"Failed to install dependencies: {e}")
        return False

def create_env_file():
    """Create .env file from template"""
    print_header("Creating .env File")
    
    try:
        if not os.path.exists(".env"):
            if os.path.exists(".env.example"):
                with open(".env.example", "r") as f:
                    content = f.read()
                with open(".env", "w") as f:
                    f.write(content)
                print_success(".env file created")
            else:
                print_info(".env.example not found, skipping")
        else:
            print_info(".env already exists")
        return True
    except Exception as e:
        print_error(f"Failed to create .env: {e}")
        return False

def main():
    print("\n")
    print("╔════════════════════════════════════════════╗")
    print("║   GST App - Automatic Setup Script        ║")
    print("║   Shree Avadhut Traders                   ║")
    print("╚════════════════════════════════════════════╝")
    
    # Check Python
    if not check_python():
        print_error("Please install Python 3.8 or higher")
        sys.exit(1)
    
    # Create venv
    if not create_venv():
        print_error("Setup failed at virtual environment creation")
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        print_error("Setup failed at dependency installation")
        sys.exit(1)
    
    # Create .env
    if not create_env_file():
        print_error("Setup failed at .env creation")
        sys.exit(1)
    
    # Success
    print_header("✅ Setup Complete!")
    
    print("\n📋 Next Steps:")
    print("\n1. Activate virtual environment:")
    
    if platform.system() == "Windows":
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    
    print("\n2. Run the application:")
    print("   python run.py")
    
    print("\n3. Open browser:")
    print("   http://localhost:5000")
    
    print("\n✨ Happy coding! 😊\n")

if __name__ == "__main__":
    main()
