"""The app module, containing the app factory function."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost/atn_btn"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
migrate = Migrate(app, db, directory='db/migrations')

db.init_app(app)

from router import init_routes

init_routes(app)
