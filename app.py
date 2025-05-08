from flask import Flask, request, jsonify 
from werkzeug.utils import secure_filename
import os
import pytesseract
from PIL import Image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'jpg', 'jpeg', 'png', 'gif', 'bmp'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route("/", methods=["GET"])
def home():
    return "Hello, Flask is running!"

@app.route("/api/verify", methods=["POST"])
def verify_document():
    if 'document' not in request.files:
        return jsonify({"status": "error", "message": "No document part in the request"}), 400

    document = request.files['document']

    if document.filename == '':
        return jsonify({"status": "error", "message": "No selected file"}), 400

    if document and allowed_file(document.filename):
        filename = secure_filename(document.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # ✅ Create uploads folder if it doesn't exist
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

        document.save(filepath)

        # 🔍 OCR: Extract text
        try:
            extracted_text = pytesseract.image_to_string(Image.open(filepath))
        except Exception as e:
            return jsonify({"status": "error", "message": f"OCR failed: {str(e)}"}), 500

        return jsonify({
            "status": "success",
            "message": "Document verified successfully!",
            "extracted_text": extracted_text
        }), 200

    return jsonify({"status": "error", "message": "Invalid file type"}), 400


if __name__ == "__main__":
    app.run(debug=True) 