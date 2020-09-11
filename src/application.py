import os

import graphene
from flask import Flask, render_template,redirect,request,url_for,jsonify
from flask_cors import cross_origin
from flask_graphql import GraphQLView
from werkzeug.utils import secure_filename

from time import perf_counter
import uuid

from flask_sqlalchemy import SQLAlchemy
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from src.config.config import create_app
from src.config.app_configs import AppConfig
from flask_graphql_auth import (
    AuthInfoField,
    GraphQLAuth,
    get_jwt_identity,
    create_access_token,
    create_refresh_token,
    query_header_jwt_required,
    mutation_header_jwt_refresh_token_required,
    mutation_header_jwt_required,
)

from flask_cors import CORS

application = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
create_app(application)


application.config["REFRESH_EXP_LENGTH"] = 30
application.config["ACCESS_EXP_LENGTH"] = 10
application.config["JWT_SECRET_KEY"] = AppConfig.config('SECRET_KEY')  # change this!
# application.config["REFRESH_EXP_LENGTH"] = 30
# application.config["ACCESS_EXP_LENGTH"] = 10
# application.config["JWT_HEADER_NAME"] = 'Token'
# application.config["JWT_HEADER_TOKEN_PREFIX"] = ''
# application.config["JWT_ACCESS_TOKEN_EXPIRES"] = False

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, '../uploads')
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(application)
auth = GraphQLAuth(application)

# Flask Rest & Graphql Routes
@application.route('/')
def hello_world():
    return 'Hello From Graphql Tutorial!!'


@application.route('/result',methods=['GET'])
def result():
    return "File Uploaded Successfully"


@application.route('/api/upload', methods=['GET','POST'])
@cross_origin(allow_headers=['Content-Type'])
def upload_me():
    print('uploading...')
    if request.method == 'POST':

        file = request.files['file']
        filename = secure_filename(file.filename)

        # Gen GUUID File Name
        fileExt = filename.split('.')[1]
        autoGenFileName = uuid.uuid4()

        newFileName = str(autoGenFileName) + '.' + fileExt

        file.save(os.path.join(application.config['UPLOAD_FOLDER'], newFileName))
        return newFileName


# Routes
from src.routes.posts import posts
application.register_blueprint(posts, url_prefix="/posts")

### graph ql
from src.graphql.queries import Query
from src.graphql.mutations import Mutation
# /graphql-query
application.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql-query',
    schema=graphene.Schema(query=Query, mutation=Mutation), graphiql=True
))

