from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name='development'):
    """Application factory"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    with app.app_context():
        # Register blueprints
        from app.routes import auth_bp, dashboard_bp, invoice_bp, customer_bp, report_bp
        
        app.register_blueprint(auth_bp)
        app.register_blueprint(dashboard_bp)
        app.register_blueprint(invoice_bp)
        app.register_blueprint(customer_bp)
        app.register_blueprint(report_bp)
        
        # Create tables
        db.create_all()
    
    return app
