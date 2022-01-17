# this is the default file. so, this will be iported autmatically when we import forem source.
from flask import Flask
import os
from src.auth2 import auth
from src.bookmarks2 import bookmarks
from src.database2 import db
from flask_jwt_extended import JWTManager


def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)

  if test_config == None:
    app.config.from_mapping(
      SECRET_KEY=os.environ.get("SECRET_KEY"),
      SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
      SQLALCHEMY_TRACK_MODIFICATIONS=False,
      JWT_SECRET_KEY=os.environ.get('JWT_SECRET_TOKEN')
    )
  else:
    app.config.from_mapping(test_config)

  db.app = app
  db.init_app(app)

  JWTManager(app)

  app.register_blueprint(auth)
  app.register_blueprint(bookmarks)

  return app