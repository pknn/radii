import os

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy_utils import create_database, database_exists

app = Flask(__name__)
app.config.from_object(Config)

if not database_exists(Config.SQLALCHEMY_DATABASE_URI):
    create_database(Config.SQLALCHEMY_DATABASE_URI)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models
