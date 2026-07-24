# Installation Guide - GST App

## Quick Installation (3 Steps)

### Step 1: Clone Repository
```bash
git clone https://github.com/pranaykamdi691-dotcom/Shree-avadhut-traders.git
cd Shree-avadhut-traders
```

### Step 2: Run Setup Script

**For Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

**For Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
```

### Step 3: Run Application
```bash
python run.py
```

✅ Open browser: **http://localhost:5000**

---

## Detailed Installation

### Prerequisites
- **Python 3.8+** (Download from https://www.python.org/downloads/)
- **pip** (comes with Python)
- **Git** (optional, for cloning)

### Windows Installation

1. **Download Python**
   - Go to https://www.python.org/downloads/
   - Download Python 3.9 or higher
   - During installation, check "Add Python to PATH"

2. **Open Command Prompt** (Win + R → cmd)
   ```bash
   cd Desktop
   git clone https://github.com/pranaykamdi691-dotcom/Shree-avadhut-traders.git
   cd Shree-avadhut-traders
   ```

3. **Create Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Install Dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. **Create .env File**
   ```bash
   copy .env.example .env
   ```

6. **Run Application**
   ```bash
   python run.py
   ```

### Mac Installation

1. **Open Terminal**
   ```bash
   cd ~/Desktop
   git clone https://github.com/pranaykamdi691-dotcom/Shree-avadhut-traders.git
   cd Shree-avadhut-traders
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Create .env File**
   ```bash
   cp .env.example .env
   ```

5. **Run Application**
   ```bash
   python run.py
   ```

### Linux Installation

1. **Open Terminal**
   ```bash
   cd ~/
   git clone https://github.com/pranaykamdi691-dotcom/Shree-avadhut-traders.git
   cd Shree-avadhut-traders
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Create .env File**
   ```bash
   cp .env.example .env
   ```

5. **Run Application**
   ```bash
   python run.py
   ```

---

## Using Make Commands (Optional)

If you have `make` installed:

```bash
make install    # Install dependencies
make run        # Run application
make test       # Run tests
make clean      # Clean cache files
```

---

## First Login

1. **Open Browser:** http://localhost:5000
2. **Click "Register"**
3. **Create Account:**
   - Username: your_username
   - Email: your_email@example.com
   - Password: your_password
   - Company Name: Your Company
   - GSTIN: 27AABCT1234H2Z0 (optional)
4. **Click "Register"**
5. **Login with credentials**

---

## Troubleshooting

### Problem: "Python not found"
**Solution:** Python not installed or not in PATH
- Download from https://www.python.org/downloads/
- Make sure "Add Python to PATH" is checked
- Restart computer

### Problem: "pip: command not found"
**Solution:** Use `python -m pip` instead
```bash
python -m pip install -r requirements.txt
```

### Problem: "Port 5000 already in use"
**Solution:** Use different port
```bash
python run.py --port 5001
```

### Problem: "ModuleNotFoundError"
**Solution:** Make sure virtual environment is activated
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### Problem: "Database locked"
**Solution:** Delete database and restart
```bash
rm gst_app.db
python run.py
```

---

## After Installation

✅ **App is running at:** http://localhost:5000

### Next Steps:
1. Register a new account
2. Add some customers
3. Create test invoices
4. Generate GST reports
5. Download PDF reports

### To Stop Application:
- Press `Ctrl + C` in terminal

### To Restart Application:
```bash
# Activate virtual environment (if not already)
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Run app
python run.py
```

---

## Support

If you encounter issues:
1. Check Python version: `python --version` (should be 3.8+)
2. Check pip version: `pip --version`
3. Make sure virtual environment is activated
4. Try reinstalling: `pip install -r requirements.txt --force-reinstall`
5. Create GitHub issue with error message

