import connexion
from flask_sqlalchemy import SQLAlchemy

from cpic_interface import encoder

db = SQLAlchemy()


def create_app():
    connex_app = connexion.App(__name__, specification_dir="./openapi/")
    app = connex_app.app

    app.json_encoder = encoder.JSONEncoder

    # 配置数据库
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cpic.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = True
    app.app_context().push()
    db.init_app(app)

    return connex_app
