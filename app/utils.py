from flask import render_template

class APIResponse:
    """Standard API Response Format"""
    @staticmethod
    def success(data=None, message="Success", status_code=200):
        return {
            'status': 'success',
            'message': message,
            'data': data
        }, status_code
    
    @staticmethod
    def error(message="Error", status_code=400, errors=None):
        return {
            'status': 'error',
            'message': message,
            'errors': errors or []
        }, status_code

class InvoiceCalculator:
    """Handle GST calculations"""
    @staticmethod
    def calculate_gst(amount, gst_rate, state_code=None):
        """Calculate GST amounts"""
        gst_amount = amount * (gst_rate / 100)
        
        # For same state: CGST + SGST
        # For different state: IGST
        if state_code and state_code != 'IGST':
            cgst = gst_amount / 2
            sgst = gst_amount / 2
            igst = 0
        else:
            cgst = 0
            sgst = 0
            igst = gst_amount
        
        return {
            'cgst': round(cgst, 2),
            'sgst': round(sgst, 2),
            'igst': round(igst, 2),
            'total_gst': round(gst_amount, 2)
        }
    
    @staticmethod
    def calculate_invoice_total(items):
        """Calculate invoice totals from items"""
        subtotal = 0
        total_cgst = 0
        total_sgst = 0
        total_igst = 0
        
        for item in items:
            line_total = item['quantity'] * item['unit_price']
            gst_calc = InvoiceCalculator.calculate_gst(line_total, item['gst_rate'])
            
            subtotal += line_total
            total_cgst += gst_calc['cgst']
            total_sgst += gst_calc['sgst']
            total_igst += gst_calc['igst']
        
        return {
            'subtotal': round(subtotal, 2),
            'cgst': round(total_cgst, 2),
            'sgst': round(total_sgst, 2),
            'igst': round(total_igst, 2),
            'total': round(subtotal + total_cgst + total_sgst + total_igst, 2)
        }
