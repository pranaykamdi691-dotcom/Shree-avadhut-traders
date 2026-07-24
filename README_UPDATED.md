# GST App - README.md (Updated)

# 🎯 Shree Avadhut Traders - GST Management App

एक complete GST management application जो Indian businesses के लिए invoices, GST calculations, और reports generate करता है।

## 🚀 Quick Start (60 Seconds)

### Windows
```bash
git clone https://github.com/pranaykamdi691-dotcom/Shree-avadhut-traders.git
cd Shree-avadhut-traders
python setup_app.py
venv\Scripts\activate
python run.py
```

### Mac/Linux
```bash
git clone https://github.com/pranaykamdi691-dotcom/Shree-avadhut-traders.git
cd Shree-avadhut-traders
python3 setup_app.py
source venv/bin/activate
python run.py
```

✅ Open: http://localhost:5000

---

## ✨ Features

### 📄 Invoice Management
- ✅ Create & manage invoices
- ✅ Add multiple line items
- ✅ Real-time GST calculation
- ✅ View & edit invoices
- ✅ Invoice status tracking

### 👥 Customer Management
- ✅ Add & manage customers
- ✅ Store GSTIN numbers
- ✅ Customer type classification
- ✅ Contact information

### 📊 GST Calculations
- ✅ Automatic CGST calculation
- ✅ Automatic SGST calculation
- ✅ IGST for inter-state sales
- ✅ Multiple GST rates (0%, 5%, 12%, 18%, 28%)

### 📈 Reports
- ✅ GST reports with filtering
- ✅ PDF export
- ✅ Summary statistics
- ✅ Date range reports

### 🔐 User Management
- ✅ Secure authentication
- ✅ Password encryption
- ✅ Multi-user support
- ✅ User profile

---

## 📋 Requirements

- Python 3.8+
- pip (Python package manager)
- Git (optional)

---

## 📚 Documentation

| Document | Purpose |
|----------|----------|
| [QUICKSTART.md](QUICKSTART.md) | Copy-paste commands |
| [INSTALL.md](INSTALL.md) | Detailed installation |
| [DOCUMENTATION.md](DOCUMENTATION.md) | Complete guide |
| [DEVELOPMENT.md](DEVELOPMENT.md) | Developer guide |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contributing guide |

---

## 🎯 Usage

### 1. Register Account
```
Go to http://localhost:5000
Click "Register"
Fill details
Click "Register"
```

### 2. Add Customers
```
Go to Customers
Click "Add New Customer"
Fill details
Save
```

### 3. Create Invoices
```
Go to Invoices
Click "Create Invoice"
Select customer
Add items
GST calculated automatically
Save invoice
```

### 4. Generate Reports
```
Go to Reports
Select date range
View GST summary
Download PDF
```

---

## 🛠️ Useful Commands

```bash
# Run app
python run.py

# Run tests
pytest tests/ -v

# Clean cache
make clean

# Open Flask shell
flask shell
```

---

## 📁 Project Structure

```
app/
├── models/          # Database models
├── routes/          # API endpoints
├── templates/       # HTML pages
├── static/          # CSS/JS
└── utils.py         # Utilities

tests/               # Test suite
docs/                # Documentation

run.py               # Entry point
config.py            # Configuration
requirements.txt    # Dependencies
```

---

## ❓ Troubleshooting

### Port 5000 already in use
```bash
python run.py --port 5001
```

### Python not found
- Install from https://www.python.org/downloads/
- Make sure "Add Python to PATH" is checked

### Virtual environment error
```bash
# Delete and recreate
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

More help in [INSTALL.md](INSTALL.md)

---

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📞 Support

- 📖 Check documentation
- 🐛 Report bugs on GitHub
- 💬 Start discussions

---

## 📄 License

MIT License - See LICENSE file

---

## 👨‍💻 Author

Pranay Kamdi
- GitHub: [@pranaykamdi691-dotcom](https://github.com/pranaykamdi691-dotcom)
- Email: pranaykamdi691@gmail.com

---

**Built with ❤️ for Indian businesses**
