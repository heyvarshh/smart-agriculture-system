from flask import Flask
from flask_cors import CORS
from config import Config
from models import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app)
    db.init_app(app)

    # Register blueprints
    from routes.farmers import farmers_bp
    from routes.crops import crops_bp
    from routes.sensors import sensors_bp
    from routes.irrigation import irrigation_bp
    from routes.analytics import analytics_bp
    from routes.logs import logs_bp

    app.register_blueprint(farmers_bp, url_prefix='/api/farmers')
    app.register_blueprint(crops_bp, url_prefix='/api/crops')
    app.register_blueprint(sensors_bp, url_prefix='/api/sensors')
    app.register_blueprint(irrigation_bp, url_prefix='/api/irrigation')
    app.register_blueprint(analytics_bp, url_prefix='/api/analytics')
    app.register_blueprint(logs_bp, url_prefix='/api/logs')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5002)
