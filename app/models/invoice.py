from app import db
from datetime import datetime
from enum import Enum

class InvoiceStatus(Enum):
    DRAFT = 'draft'
    ISSUED = 'issued'
    PAID = 'paid'
    CANCELLED = 'cancelled'

class Invoice(db.Model):
    __tablename__ = 'invoices'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    
    invoice_number = db.Column(db.String(50), unique=True, nullable=False, index=True)
    invoice_date = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    due_date = db.Column(db.Date)
    
    status = db.Column(db.String(20), default=InvoiceStatus.DRAFT.value)
    
    # Amounts
    subtotal = db.Column(db.Float, default=0.0)
    sgst = db.Column(db.Float, default=0.0)  # State GST
    cgst = db.Column(db.Float, default=0.0)  # Central GST
    igst = db.Column(db.Float, default=0.0)  # Integrated GST
    total_amount = db.Column(db.Float, default=0.0)
    
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    items = db.relationship('InvoiceItem', backref='invoice', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Invoice {self.invoice_number}>'

class InvoiceItem(db.Model):
    __tablename__ = 'invoice_items'
    
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoices.id'), nullable=False)
    
    description = db.Column(db.String(500), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    gst_rate = db.Column(db.Float, default=18.0)  # GST percentage
    
    line_total = db.Column(db.Float)  # quantity * unit_price
    line_gst = db.Column(db.Float)  # GST on line_total
    line_amount = db.Column(db.Float)  # line_total + line_gst
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<InvoiceItem {self.description}>'
