from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from services.document_service import upload_document
from services.verification_service import verify_document

document_bp = Blueprint('documents', __name__)

# Upload Aadhaar document route
@document_bp.route('/upload-aadhaar', methods=['POST'])
def upload_aadhaar():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filename = secure_filename(file.filename)
        upload_folder = os.path.join('uploads')
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)

        # Upload logic (optional — just storing for now)
        upload_result, _ = upload_document(file, user_id='test_user')

        # Aadhaar Verification
        verification_result = verify_document(file_path)

        # Debug output
        print("DEBUG VERIFICATION RESULT:", verification_result)

        return jsonify({
            "message": "Document processed",
            "upload_result": upload_result,
            "verification_result": verification_result
        }), 200
