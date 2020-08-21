import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
application = Flask(__name__)
# Database Configs [Check it base on other Database Configuration]

# # Initialize Database

db = SQLAlchemy(application)
def create_app(application):
  db.init_app(application)
  application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://devuser:devuser@host.docker.internal/whatsapp_api'
  application.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
  application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# #app = Flask(__name__)
# db.init_app(application)