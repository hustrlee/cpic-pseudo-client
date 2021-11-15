import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    """
    初始化数据库配置
    """
    database_uri = "sqlite:///" + os.path.join(os.path.dirname(__file__), "cpic.db")  # noqa: E501
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = True
    app.app_context().push()
    db.init_app(app)
