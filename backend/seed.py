from backend.app import create_app
from backend.models import db, Farmer, Crop, Zone, Log
from datetime import datetime, timedelta

app = create_app()

def seed_database():
    with app.app_context():
        # Drop all tables and recreate them
        print("Dropping all existing tables...")
        db.drop_all()
        print("Creating new tables...")
        db.create_all()

        print("Inserting Farmers...")
        farmers_data = [
            {"id": 'FRM-001', "name": 'Ramesh Kumar', "phone": '9876543210', "village": 'Pune Rural', "land": 4.5, "status": 'Active'},
            {"id": 'FRM-002', "name": 'Sunita Devi', "phone": '8765432109', "village": 'Nashik East', "land": 2.1, "status": 'Active'},
            {"id": 'FRM-003', "name": 'Mohan Patel', "phone": '7654321098', "village": 'Surat North', "land": 7.8, "status": 'Active'},
            {"id": 'FRM-004', "name": 'Lakshmi Bai', "phone": '6543210987', "village": 'Jaipur Rural', "land": 3.2, "status": 'Inactive'},
            {"id": 'FRM-005', "name": 'Arjun Singh', "phone": '5432109876', "village": 'Ludhiana', "land": 9.6, "status": 'Active'}
        ]
        for f in farmers_data:
            db.session.add(Farmer(farmer_id=f['id'], name=f['name'], phone=f['phone'], village=f['village'], land=f['land'], status=f['status']))

        print("Inserting Crops...")
        crops_data = [
            {"id": 'CRP-101', "name": 'Wheat', "type": 'Cereal', "farmer": 'Ramesh Kumar', "sow": '2025-11-01', "harvest": '2026-04-15', "stage": 90, "health": 'Healthy', "sensor": 'SN-014'},
            {"id": 'CRP-102', "name": 'Rice', "type": 'Cereal', "farmer": 'Arjun Singh', "sow": '2026-06-15', "harvest": '2026-11-10', "stage": 10, "health": 'Healthy', "sensor": 'SN-015'},
            {"id": 'CRP-103', "name": 'Tomato', "type": 'Vegetable', "farmer": 'Sunita Devi', "sow": '2026-02-10', "harvest": '2026-05-20', "stage": 65, "health": 'At Risk', "sensor": 'SN-016'},
            {"id": 'CRP-104', "name": 'Cotton', "type": 'Cash Crop', "farmer": 'Mohan Patel', "sow": '2026-05-01', "harvest": '2026-10-30', "stage": 35, "health": 'Healthy', "sensor": 'SN-017'}
        ]
        for c in crops_data:
            db.session.add(Crop(crop_id=c['id'], name=c['name'], type=c['type'], farmer=c['farmer'], sow=c['sow'], harvest=c['harvest'], stage=c['stage'], health=c['health'], sensor=c['sensor']))

        print("Inserting Zones...")
        zones_data = [
            {"id": 'Z-01', "name": 'North Field A', "crop": 'Wheat', "level": 85, "flow": '4.2 L/m', "status": 'ON'},
            {"id": 'Z-02', "name": 'South Field B', "crop": 'Rice', "level": 92, "flow": '5.0 L/m', "status": 'ON'},
            {"id": 'Z-03', "name": 'East Greenhouse', "crop": 'Tomato', "level": 45, "flow": '0.0 L/m', "status": 'OFF'},
            {"id": 'Z-04', "name": 'West Sector 1', "crop": 'Cotton', "level": 30, "flow": '0.0 L/m', "status": 'OFF'}
        ]
        for z in zones_data:
            db.session.add(Zone(zone_id=z['id'], name=z['name'], crop=z['crop'], level=z['level'], flow=z['flow'], status=z['status']))

        print("Inserting Logs...")
        now = datetime.utcnow()
        logs_data = [
            {"time": now, "module": 'Sensor', "text": 'High Temp Alert in SN-014', "trigger": 'System', "status": 'Critical'},
            {"time": now - timedelta(hours=1), "module": 'Irrigation', "text": 'Zone Z-01 Turned ON', "trigger": 'Admin', "status": 'OK'},
            {"time": now - timedelta(hours=2), "module": 'Farmer', "text": 'Added new farmer Meera Nair', "trigger": 'Admin', "status": 'OK'},
            {"time": now - timedelta(hours=4), "module": 'Crop', "text": 'Tomato health changed to At Risk', "trigger": 'System', "status": 'Warning'}
        ]
        for l in logs_data:
            db.session.add(Log(time=l['time'], module=l['module'], text=l['text'], trigger=l['trigger'], status=l['status']))

        db.session.commit()
        print("Database seeding completed successfully! You can verify data in 'smart_kisan.db'")

if __name__ == '__main__':
    seed_database()
