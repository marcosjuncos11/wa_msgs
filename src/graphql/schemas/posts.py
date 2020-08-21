import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from src.models.posts import Post

class PostObject(SQLAlchemyObjectType):
    class Meta:
        model = Post
        interfaces = (graphene.relay.Node,)