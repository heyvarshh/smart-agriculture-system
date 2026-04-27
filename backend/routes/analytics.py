from flask import Blueprint, jsonify

analytics_bp = Blueprint('analytics_bp', __name__)

@analytics_bp.route('/', methods=['GET'])
def analytics():
    return jsonify({"message": "Analytics working"})