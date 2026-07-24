import pytest
from app import create_app, db
from app.models import User, Customer, Invoice

@pytest.fixture
def app():
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def user(app):
    user = User(
        username='testuser',
        email='test@example.com',
        company_name='Test Company',
        gstin='27AABCT1234H2Z0'
    )
    user.set_password('password123')
    db.session.add(user)
    db.session.commit()
    return user

@pytest.fixture
def customer(app, user):
    customer = Customer(
        user_id=user.id,
        name='Test Customer',
        email='customer@example.com',
        phone='9876543210',
        gstin='27AABCU1234H2Z0',
        city='Mumbai',
        state='MH'
    )
    db.session.add(customer)
    db.session.commit()
    return customer
