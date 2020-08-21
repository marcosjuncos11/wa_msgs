import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from src.config.config import db
from src.models.users import User
from src.models.posts import Post
from src.graphql.schemas.users import UserObject

from src.graphql.query.posts import PostQuery
from src.graphql.query.test import Test
# ------------------ Graphql Schemas ------------------

class Query(graphene.ObjectType, PostQuery, Test):
    node = graphene.relay.Node.Field()
    
    def resolve_post_queries(parent, info):
      return parent

    all_users = SQLAlchemyConnectionField(UserObject)

    
    goodbye = graphene.String()

    
    def resolve_goodbye(root, info):
        return 'See ya!'


# noinspection PyTypeChecker
# schema_query = graphene.Schema(query=Query)
