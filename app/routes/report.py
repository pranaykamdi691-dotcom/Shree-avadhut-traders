from flask import Blueprint, render_template, request, send_file
from flask_login import login_required, current_user
from app.models import Invoice
from datetime import datetime, timedelta
import io
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

report_bp = Blueprint('report', __name__, url_prefix='/reports')

@report_bp.route('/')
@login_required
def index():
    return render_template('report/index.html')

@report_bp.route('/gst')
@login_required
def gst_report():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    query = Invoice.query.filter_by(user_id=current_user.id)
    
    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        query = query.filter(Invoice.invoice_date >= start_date)
    
    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        query = query.filter(Invoice.invoice_date <= end_date)
    
    invoices = query.all()
    
    total_sales = sum(inv.subtotal for inv in invoices)
    total_cgst = sum(inv.cgst for inv in invoices)
    total_sgst = sum(inv.sgst for inv in invoices)
    total_igst = sum(inv.igst for inv in invoices)
    total_gst = total_cgst + total_sgst + total_igst
    
    context = {
        'invoices': invoices,
        'total_sales': total_sales,
        'total_cgst': total_cgst,
        'total_sgst': total_sgst,
        'total_igst': total_igst,
        'total_gst': total_gst,
        'start_date': start_date,
        'end_date': end_date
    }
    
    return render_template('report/gst.html', **context)

@report_bp.route('/gst/pdf')
@login_required
def gst_report_pdf():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    # Generate PDF
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    
    styles = getSampleStyleSheet()
    
    # Title
    title = Paragraph(f"GST Report - {current_user.company_name}", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))
    
    # Summary data
    query = Invoice.query.filter_by(user_id=current_user.id)
    if start_date:
        query = query.filter(Invoice.invoice_date >= datetime.strptime(start_date, '%Y-%m-%d').date())
    if end_date:
        query = query.filter(Invoice.invoice_date <= datetime.strptime(end_date, '%Y-%m-%d').date())
    
    invoices = query.all()
    
    summary_data = [
        ['Total Sales', f"₹{sum(inv.subtotal for inv in invoices):.2f}"],
        ['CGST', f"₹{sum(inv.cgst for inv in invoices):.2f}"],
        ['SGST', f"₹{sum(inv.sgst for inv in invoices):.2f}"],
        ['IGST', f"₹{sum(inv.igst for inv in invoices):.2f}"],
        ['Total GST', f"₹{sum(inv.cgst + inv.sgst + inv.igst for inv in invoices):.2f}"]
    ]
    
    summary_table = Table(summary_data)
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(summary_table)
    
    doc.build(elements)
    buffer.seek(0)
    
    return send_file(buffer, mimetype='application/pdf', as_attachment=True, download_name='gst_report.pdf')
