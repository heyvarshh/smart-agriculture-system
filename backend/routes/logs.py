from flask import Blueprint, jsonify

logs_bp = Blueprint('logs_bp', __name__)

@logs_bp.route('/', methods=['GET'])
def logs():
    return jsonify({"message": "Logs working"})