from flask import Blueprint, jsonify
from models import Zone

sensors_bp = Blueprint('sensors_bp', __name__)

@sensors_bp.route('/', methods=['GET'])
def get_sensors():
    zones = Zone.query.all()
    return jsonify([z.to_dict() for z in zones])