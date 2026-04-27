from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# ---------------- FARMER ----------------
class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.String(20), unique=True, nullable=False)  # e.g. FRM-001
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    village = db.Column(db.String(100), nullable=False)
    land = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='Active')

    def to_dict(self):
        return {
            "id": self.farmer_id,
            "name": self.name,
            "phone": self.phone,
            "village": self.village,
            "land": self.land,
            "status": self.status
        }


# ---------------- CROP ----------------
class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_id = db.Column(db.String(20), unique=True, nullable=False)  # e.g. CRP-101
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    farmer = db.Column(db.String(100), nullable=False)
    sow = db.Column(db.String(20), nullable=False)
    harvest = db.Column(db.String(20), nullable=False)
    stage = db.Column(db.Integer, nullable=False)
    health = db.Column(db.String(50), nullable=False)
    sensor = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.crop_id,
            "name": self.name,
            "type": self.type,
            "farmer": self.farmer,
            "sow": self.sow,
            "harvest": self.harvest,
            "stage": self.stage,
            "health": self.health,
            "sensor": self.sensor
        }


# ---------------- ZONE (Sensor + Irrigation Combined) ----------------
class Zone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zone_id = db.Column(db.String(20), unique=True, nullable=False)  # e.g. Z-01
    name = db.Column(db.String(50), nullable=False)
    crop = db.Column(db.String(50), nullable=False)
    level = db.Column(db.Integer, nullable=False)   # water level / moisture
    flow = db.Column(db.String(20), nullable=False) # flow status
    status = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            "id": self.zone_id,
            "name": self.name,
            "crop": self.crop,
            "level": self.level,
            "flow": self.flow,
            "status": self.status
        }


# ---------------- LOG ----------------
class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    module = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    trigger = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            "time": self.time.isoformat() + "Z",
            "module": self.module,
            "text": self.text,
            "trigger": self.trigger,
            "status": self.status
        }
