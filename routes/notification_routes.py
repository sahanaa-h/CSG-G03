from flask import Blueprint, jsonify

notification_bp = Blueprint('notification', __name__)

@notification_bp.route('/notify', methods=['GET'])
def notify():
    # Placeholder logic for notification
    return jsonify({"message": "Notification sent successfully"})
