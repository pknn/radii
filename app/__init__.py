from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_dance.consumer.backend.sqla import SQLAlchemyBackend
from flask_dance.contrib.github import make_github_blueprint
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


github_blueprint = make_github_blueprint(
    client_id="b26917e9a8092b6effd7",
    client_secret="12711bc7f79c54a9bc92a67c77a7e75653bb73df",
)

app.register_blueprint(github_blueprint, url_prefix="/login")

login_manager = LoginManager()
login_manager.init_app(app)

from app import routes, models

github_blueprint.backend = SQLAlchemyBackend(models.OAuth, db.session)
