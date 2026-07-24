from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Invoice, Customer

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@login_required
def index():
    invoices = Invoice.query.filter_by(user_id=current_user.id).all()
    customers = Customer.query.filter_by(user_id=current_user.id).all()
    
    total_invoiced = sum(inv.total_amount for inv in invoices)
    total_gst = sum(inv.sgst + inv.cgst + inv.igst for inv in invoices)
    
    context = {
        'invoices': invoices,
        'customers': customers,
        'total_invoiced': total_invoiced,
        'total_gst': total_gst,
        'invoice_count': len(invoices),
        'customer_count': len(customers)
    }
    
    return render_template('dashboard/index.html', **context)
