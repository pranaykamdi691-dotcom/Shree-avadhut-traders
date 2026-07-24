import pytest
from app.models import Customer
from app import db

def test_create_customer(client, user):
    """Test creating a new customer"""
    # Login first
    client.post('/auth/login', data={
        'username': 'testuser',
        'password': 'password123'
    })
    
    response = client.post('/customers/create', data={
        'name': 'New Customer',
        'email': 'newcustomer@example.com',
        'phone': '9876543210',
        'gstin': '27AABCU1234H2Z1',
        'city': 'Delhi',
        'state': 'DL',
        'customer_type': 'Business'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Customer added successfully' in response.data

def test_list_customers(client, user, customer):
    """Test listing customers"""
    client.post('/auth/login', data={
        'username': 'testuser',
        'password': 'password123'
    })
    
    response = client.get('/customers/')
    assert response.status_code == 200
    assert b'Test Customer' in response.data

def test_edit_customer(client, user, customer):
    """Test editing a customer"""
    client.post('/auth/login', data={
        'username': 'testuser',
        'password': 'password123'
    })
    
    response = client.post(f'/customers/{customer.id}/edit', data={
        'name': 'Updated Customer',
        'email': 'updated@example.com',
        'phone': '9876543210',
        'city': 'Bangalore',
        'state': 'KA',
        'customer_type': 'Business'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Customer updated successfully' in response.data
