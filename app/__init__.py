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
    client_id="674925257692ed46a38b",
    client_secret="319fb87ac542c68085927440429a968f0bf55dbf",
)

app.register_blueprint(github_blueprint, url_prefix="/login")

login_manager = LoginManager()
login_manager.init_app(app)

from app import routes, models

github_blueprint.backend = SQLAlchemyBackend(models.OAuth, db.session)
