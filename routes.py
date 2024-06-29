from flask import Blueprint, request, jsonify
from app import db
from models import Product

product_bp = Blueprint('products', __name__)

from flask import Blueprint, request, jsonify
from app import db
from models import Product

product_bp = Blueprint('products', __name__)

@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data or 'category' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    new_product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        category=data['category'],
        images=data.get('images', '')
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created', 'product_id': new_product.id}), 201

@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

@product_bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict()), 200

@product_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.category = data.get('category', product.category)
    product.images = data.get('images', product.images)
    db.session.commit()
    return jsonify({'message': 'Product updated'}), 200

@product_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'}), 200
