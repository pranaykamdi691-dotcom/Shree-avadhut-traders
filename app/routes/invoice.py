from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import Invoice, InvoiceItem, Customer
from datetime import datetime, timedelta

invoice_bp = Blueprint('invoice', __name__, url_prefix='/invoices')

@invoice_bp.route('/')
@login_required
def list_invoices():
    invoices = Invoice.query.filter_by(user_id=current_user.id).order_by(Invoice.created_at.desc()).all()
    return render_template('invoice/list.html', invoices=invoices)

@invoice_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_invoice():
    customers = Customer.query.filter_by(user_id=current_user.id).all()
    
    if request.method == 'POST':
        customer_id = request.form.get('customer_id')
        invoice_date = datetime.strptime(request.form.get('invoice_date'), '%Y-%m-%d').date()
        due_date = datetime.strptime(request.form.get('due_date'), '%Y-%m-%d').date() if request.form.get('due_date') else None
        notes = request.form.get('notes')
        
        # Generate invoice number
        last_invoice = Invoice.query.filter_by(user_id=current_user.id).order_by(Invoice.id.desc()).first()
        invoice_number = f"INV-{current_user.id}-{(last_invoice.id + 1) if last_invoice else 1}"
        
        invoice = Invoice(
            user_id=current_user.id,
            customer_id=customer_id,
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            due_date=due_date,
            notes=notes
        )
        
        db.session.add(invoice)
        db.session.flush()
        
        # Add items
        items_data = request.form.getlist('items')
        for item_data in items_data:
            # Parse item data (implementation depends on form structure)
            pass
        
        db.session.commit()
        flash('Invoice created successfully!', 'success')
        return redirect(url_for('invoice.view_invoice', invoice_id=invoice.id))
    
    return render_template('invoice/create.html', customers=customers)

@invoice_bp.route('/<int:invoice_id>')
@login_required
def view_invoice(invoice_id):
    invoice = Invoice.query.get_or_404(invoice_id)
    if invoice.user_id != current_user.id:
        flash('Unauthorized', 'error')
        return redirect(url_for('dashboard.index'))
    
    return render_template('invoice/view.html', invoice=invoice)

@invoice_bp.route('/<int:invoice_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_invoice(invoice_id):
    invoice = Invoice.query.get_or_404(invoice_id)
    if invoice.user_id != current_user.id:
        flash('Unauthorized', 'error')
        return redirect(url_for('dashboard.index'))
    
    if request.method == 'POST':
        invoice.notes = request.form.get('notes')
        db.session.commit()
        flash('Invoice updated successfully!', 'success')
        return redirect(url_for('invoice.view_invoice', invoice_id=invoice.id))
    
    return render_template('invoice/edit.html', invoice=invoice)
