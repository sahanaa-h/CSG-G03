from services.document_service import verify_aadhaar

def verify_document(file_path):
    # For now, treat everything as Aadhaar for testing
    result = verify_aadhaar(file_path)
    
    return {
        "status": result.get("status"),
        "confidence": result.get("confidence"),
        "ocr_text": result.get("ocr_text"),
        "qr_data": result.get("qr_data")
    }
