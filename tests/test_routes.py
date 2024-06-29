import pytest
from app import app, db
from models import Product

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_create_product(client):
    response = client.post('/products/', json={
        'name': 'Test Product',
        'price': 100.0,
        'category': 'Test Category'
    })
    assert response.status_code == 201
    assert response.json['message'] == 'Product created'

def test_get_products(client):
    client.post('/products/', json={
        'name': 'Test Product',
        'price': 100.0,
        'category': 'Test Category'
    })
    response = client.get('/products/')
    assert response.status_code == 200
    assert len(response.json) == 1
