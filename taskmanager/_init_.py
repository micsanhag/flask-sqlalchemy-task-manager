import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env # noqa


    app = Flask(_name_)
    appconfig["SECRET_KEY"] os.environ.get("SECRETR_KEY")
    appconfig["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

    db = SQLAlchemy()

    from taskmanager import routes # noqa