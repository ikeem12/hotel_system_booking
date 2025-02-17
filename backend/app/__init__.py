from flask import Flask

from config import Config
from .core.extensions import db, limiter

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    limiter.storage_uri = app.config["STORAGE_URI"]
    limiter.init_app(app)

    return app