from flask import Blueprint, jsonify
from models import db, Crop

crops_bp = Blueprint('crops_bp', __name__)

@crops_bp.route('/', methods=['GET'])
def get_crops():
    crops = Crop.query.all()
    return jsonify([{
        "id": c.id,
        "crop_name": c.crop_name,
        "season": c.season,
        "growth_days": c.growth_days,
        "farm_id": c.farm_id
    } for c in crops])