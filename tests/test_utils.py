from app.utils import InvoiceCalculator

def test_calculate_gst():
    """Test GST calculation"""
    result = InvoiceCalculator.calculate_gst(1000, 18)
    assert result['total_gst'] == 180
    assert result['cgst'] == 90
    assert result['sgst'] == 90

def test_calculate_gst_igst():
    """Test IGST calculation"""
    result = InvoiceCalculator.calculate_gst(1000, 18, 'IGST')
    assert result['total_gst'] == 180
    assert result['igst'] == 180
    assert result['cgst'] == 0
    assert result['sgst'] == 0

def test_calculate_invoice_total():
    """Test invoice total calculation"""
    items = [
        {'quantity': 2, 'unit_price': 100, 'gst_rate': 18},
        {'quantity': 1, 'unit_price': 500, 'gst_rate': 18}
    ]
    
    result = InvoiceCalculator.calculate_invoice_total(items)
    # 2*100 + 1*500 = 700
    # GST = 700 * 18% = 126
    assert result['subtotal'] == 700
    assert result['total_gst'] == 126
    assert result['total'] == 826
