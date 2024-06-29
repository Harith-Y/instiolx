from flask import Blueprint, send_from_directory

documentation_bp = Blueprint('documentation', __name__)

@documentation_bp.route('/api-documentation', methods=['GET'])
def get_api_documentation():
    return send_from_directory('documentation', 'api_documentation.yaml')
