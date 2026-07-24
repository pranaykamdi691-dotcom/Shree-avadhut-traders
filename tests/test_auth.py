import pytest

def test_register(client):
    """Test user registration"""
    response = client.post('/auth/register', data={
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password': 'password123',
        'company_name': 'New Company',
        'gstin': '27AABCT1234H2Z1'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Registration successful' in response.data

def test_login(client, user):
    """Test user login"""
    response = client.post('/auth/login', data={
        'username': 'testuser',
        'password': 'password123'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Login successful' in response.data

def test_login_invalid(client):
    """Test login with invalid credentials"""
    response = client.post('/auth/login', data={
        'username': 'testuser',
        'password': 'wrongpassword'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Invalid username or password' in response.data

def test_logout(client, user):
    """Test user logout"""
    client.post('/auth/login', data={
        'username': 'testuser',
        'password': 'password123'
    })
    
    response = client.get('/auth/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'logged out' in response.data
