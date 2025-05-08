from flask import Blueprint, request, jsonify
from services.verification_service import verify_document

verification_bp = Blueprint('verification', __name__)

@verification_bp.route('/verify', methods=['POST'])
def verify():
    data = request.json.get("document_data", "")
    result = verify_document(data)
    return jsonify(result)
