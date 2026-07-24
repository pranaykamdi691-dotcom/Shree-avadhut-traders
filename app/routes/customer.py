from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Customer

customer_bp = Blueprint('customer', __name__, url_prefix='/customers')

@customer_bp.route('/')
@login_required
def list_customers():
    customers = Customer.query.filter_by(user_id=current_user.id).all()
    return render_template('customer/list.html', customers=customers)

@customer_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_customer():
    if request.method == 'POST':
        customer = Customer(
            user_id=current_user.id,
            name=request.form.get('name'),
            email=request.form.get('email'),
            phone=request.form.get('phone'),
            gstin=request.form.get('gstin'),
            address=request.form.get('address'),
            city=request.form.get('city'),
            state=request.form.get('state'),
            pincode=request.form.get('pincode'),
            customer_type=request.form.get('customer_type')
        )
        db.session.add(customer)
        db.session.commit()
        flash('Customer added successfully!', 'success')
        return redirect(url_for('customer.list_customers'))
    
    return render_template('customer/create.html')

@customer_bp.route('/<int:customer_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    if customer.user_id != current_user.id:
        flash('Unauthorized', 'error')
        return redirect(url_for('dashboard.index'))
    
    if request.method == 'POST':
        customer.name = request.form.get('name')
        customer.email = request.form.get('email')
        customer.phone = request.form.get('phone')
        customer.gstin = request.form.get('gstin')
        customer.address = request.form.get('address')
        customer.city = request.form.get('city')
        customer.state = request.form.get('state')
        customer.pincode = request.form.get('pincode')
        customer.customer_type = request.form.get('customer_type')
        
        db.session.commit()
        flash('Customer updated successfully!', 'success')
        return redirect(url_for('customer.list_customers'))
    
    return render_template('customer/edit.html', customer=customer)
