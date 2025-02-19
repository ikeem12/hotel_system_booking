from flask import Flask

from config import Config
from .core.extensions import db, limiter
from .services.reservation_services.v1 import bp_rsv_svc_v1
from .core.error_handler import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    limiter.storage_uri = app.config["STORAGE_URI"]
    limiter.init_app(app)

    app.register_blueprint(
        bp_rsv_svc_v1,
        url_prefix='/api/v1'
    )

    register_error_handlers(app)

    return app