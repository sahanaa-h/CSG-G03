import pytesseract
from PIL import Image
import io
import re

def verify_document(file):
    image = Image.open(file.stream)
    extracted_text = pytesseract.image_to_string(image)

    # Aadhaar card pattern check
    aadhaar_number_match = re.search(r'\b\d{4} \d{4} \d{4}\b', extracted_text)
    has_goi = "government of india" in extracted_text.lower()
    has_gender = "male" in extracted_text.lower() or "female" in extracted_text.lower()
    has_dob = re.search(r'\b\d{2}/\d{2}/\d{4}\b', extracted_text)

    # 🔍 Check if suspicious name appears (example only)
    suspicious_names = ["DONALD TRUMP", "obama", "putin", "elon", "kim jong", "iron man"]
    extracted_text_lower = extracted_text.lower()
    has_fake_name = any(name in extracted_text_lower for name in suspicious_names)

    # Basic verification
    is_valid = all([aadhaar_number_match, has_goi, has_gender, has_dob]) and not has_fake_name

    result = {
        "status": "Verified" if is_valid else "Fake",
        "extracted_text": extracted_text
    }

    return result
