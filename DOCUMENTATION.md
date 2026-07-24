# GST App Documentation

## Overview
Shree Avadhut Traders GST Management Application - A comprehensive tool for managing invoices and GST calculations for small and medium businesses in India.

## Features

### 1. User Management
- User registration and authentication
- Secure password hashing
- User profile with company details
- GSTIN (GST Identification Number) storage

### 2. Invoice Management
- Create invoices with multiple line items
- Edit existing invoices
- View invoice details
- Automatic GST calculation
- Invoice status tracking (Draft, Issued, Paid, Cancelled)

### 3. Customer Management
- Add and manage customers
- Store customer GSTIN
- Customer type classification
- Address and contact information

### 4. GST Calculations
- Automatic CGST (Central GST) calculation
- Automatic SGST (State GST) calculation
- IGST (Integrated GST) for inter-state sales
- Support for multiple GST rates (0%, 5%, 12%, 18%, 28%)

### 5. Reports
- GST reports with date filtering
- PDF export functionality
- Summary statistics
- Monthly and custom period reports

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- SQLite3 (included with Python)

### Steps

1. Clone the repository
```bash
git clone https://github.com/pranaykamdi691-dotcom/Shree-avadhut-traders.git
cd Shree-avadhut-traders
```

2. Run the setup script
```bash
chmod +x setup.sh
./setup.sh
```

Or manually:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

3. Run the application
```bash
python run.py
```

4. Open your browser and navigate to
```
http://localhost:5000
```

## Usage

### Creating an Account
1. Click on "Register" link
2. Enter your details:
   - Username
   - Email
   - Password
   - Company Name
   - GSTIN (optional)
3. Submit the form

### Adding Customers
1. Go to "Customers" section
2. Click "Add New Customer"
3. Fill in customer details:
   - Name
   - Email/Phone
   - GSTIN
   - Address
   - Customer Type (Individual/Business)
4. Save customer

### Creating Invoices
1. Go to "Dashboard" or "Invoices"
2. Click "Create Invoice"
3. Select customer
4. Add invoice items:
   - Description
   - Quantity
   - Unit Price
   - GST Rate
5. System automatically calculates GST
6. Add notes if needed
7. Submit invoice

### Generating Reports
1. Go to "Reports" section
2. Select date range (optional)
3. View GST summary
4. Download PDF report

## Project Structure

```
app/
├── models/
│   ├── __init__.py
│   ├── user.py              # User model
│   ├── invoice.py           # Invoice and InvoiceItem models
│   ├── customer.py          # Customer model
│   └── vendor.py            # Vendor model
├── routes/
│   ├── __init__.py
│   ├── auth.py              # Authentication routes
│   ├── dashboard.py         # Dashboard routes
│   ├── invoice.py           # Invoice management routes
│   ├── customer.py          # Customer management routes
│   └── report.py            # Report generation routes
├── templates/
│   ├── base.html            # Base template
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   ├── dashboard/
│   │   └── index.html
│   ├── invoice/
│   │   ├── list.html
│   │   ├── create.html
│   │   ├── view.html
│   │   └── edit.html
│   ├── customer/
│   │   ├── list.html
│   │   ├── create.html
│   │   └── edit.html
│   ├── report/
│   │   ├── index.html
│   │   └── gst.html
│   └── errors/
│       ├── 404.html
│       └── 500.html
├── static/
│   └── css/
│       └── style.css
├── __init__.py              # App factory
└── utils.py                 # Utility functions

tests/
├── conftest.py              # Pytest fixtures
├── test_auth.py             # Auth tests
├── test_customer.py         # Customer tests
└── test_utils.py            # Utility tests

config.py                   # Configuration
run.py                      # Entry point
requirements.txt           # Dependencies
Makefile                   # Make commands
pytest.ini                 # Pytest config
.env.example               # Environment variables template
.gitignore                 # Git ignore
```

## API Utilities

### InvoiceCalculator

**calculate_gst(amount, gst_rate, state_code=None)**
- Calculates GST on an amount
- Returns CGST, SGST, IGST breakdown

**calculate_invoice_total(items)**
- Calculates total invoice amount with all GST components
- Takes list of items with quantity, unit_price, gst_rate

### APIResponse

**success(data=None, message="Success", status_code=200)**
- Returns standardized success response

**error(message="Error", status_code=400, errors=None)**
- Returns standardized error response

## Testing

Run tests using:
```bash
pytest tests/ -v
```

Or use the test script:
```bash
chmod +x run_tests.sh
./run_tests.sh
```

## Troubleshooting

### Port 5000 already in use
```bash
python run.py --port 5001
```

### Database errors
```bash
rm gst_app.db
python run.py
```

### Module not found errors
```bash
pip install -r requirements.txt --force-reinstall
```

## Configuration

Edit `.env` file to configure:
- `FLASK_ENV`: development/production
- `SECRET_KEY`: Flask secret key
- `DATABASE_URL`: Database connection string

## Security Notes

- Always use strong passwords
- Change SECRET_KEY in production
- Use HTTPS in production
- Validate all user inputs
- Never commit `.env` file with secrets

## Performance Tips

1. Use database indexing for frequent queries
2. Cache reports if generating frequently
3. Use pagination for large invoice lists
4. Enable gzip compression in production
5. Use CDN for static files

## Future Enhancements

- [ ] Multi-user/multi-company support
- [ ] Email notifications
- [ ] API endpoints for integrations
- [ ] Advanced reporting and analytics
- [ ] Mobile app
- [ ] Payment gateway integration
- [ ] Automated GST filing
- [ ] Inventory management

## Support

For issues and suggestions, please create an issue on GitHub.

## Contact

For queries, contact: pranaykamdi691@gmail.com
