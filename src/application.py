import os

import graphene
from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from src.config.config import create_app
application = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
create_app(application)


# class Query(graphene.ObjectType):
#     node = graphene.relay.Node.Field()
#     all_posts = SQLAlchemyConnectionField(PostObject)
#     all_users = SQLAlchemyConnectionField(UserObject)


# # noinspection PyTypeChecker
# schema_query = graphene.Schema(query=Query)


# Mutation Objects Schema



# noinspection PyTypeChecker
# schema_mutation = graphene.Schema(query=Query, mutation=Mutation)


# Flask Rest & Graphql Routes
@application.route('/')
def hello_world():
    return 'Hello From Graphql Tutorial!!'



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

# /graphql-mutation
# application.add_url_rule('/graphql-mutation', view_func=GraphQLView.as_view(
#     'graphql-mutation',
#     schema=schema_mutation, graphiql=True
# ))
