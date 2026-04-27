from flask import Blueprint, jsonify
from models import Zone

irrigation_bp = Blueprint('irrigation_bp', __name__)

@irrigation_bp.route('/', methods=['GET'])
def get_irrigation():
    zones = Zone.query.all()
    return jsonify([z.to_dict() for z in zones])