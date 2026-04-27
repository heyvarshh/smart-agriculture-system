from flask import Blueprint, jsonify
from models import db, Farmer

farmers_bp = Blueprint('farmers_bp', __name__)

@farmers_bp.route('/', methods=['GET'])
def get_farmers():
    farmers = Farmer.query.all()
    return jsonify([{
        "id": f.id,
        "name": f.name,
        "phone": f.phone,
        "location": f.location
    } for f in farmers])