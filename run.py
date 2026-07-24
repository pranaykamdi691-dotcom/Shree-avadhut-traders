import os
from app import create_app, db
from app.models import User, Invoice, InvoiceItem, Customer, Vendor
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_ENV', 'development'))
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Invoice': Invoice, 'InvoiceItem': InvoiceItem, 'Customer': Customer, 'Vendor': Vendor}

@app.errorhandler(404)
def not_found_error(error):
    from flask import render_template
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    from flask import render_template
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
