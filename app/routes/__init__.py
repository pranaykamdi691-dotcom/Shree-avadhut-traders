from .auth import auth_bp
from .dashboard import dashboard_bp
from .invoice import invoice_bp
from .customer import customer_bp
from .report import report_bp

__all__ = ['auth_bp', 'dashboard_bp', 'invoice_bp', 'customer_bp', 'report_bp']
