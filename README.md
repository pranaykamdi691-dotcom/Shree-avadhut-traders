# Shree Avadhut Traders - GST App

A comprehensive GST (Goods and Services Tax) management application for small and medium businesses.

## Features
- Invoice management
- GST calculation
- Tax return generation
- Customer/Vendor management
- Reports and analytics
- Multi-user support

## Tech Stack
- **Backend:** Python Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite (Development), PostgreSQL (Production)
- **Reports:** ReportLab for PDF generation

## Project Structure
```
shree-avadhut-traders/
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   ├── templates/
│   └── static/
├── tests/
├── config.py
├── requirements.txt
└── run.py
```

## Installation

1. Clone the repository
```bash
git clone https://github.com/pranaykamdi691-dotcom/Shree-avadhut-traders.git
cd Shree-avadhut-traders
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python run.py
```

The app will be available at `http://localhost:5000`

## Getting Started

- Access the dashboard at `/` after login
- Create invoices from the dashboard
- Generate GST reports as needed
