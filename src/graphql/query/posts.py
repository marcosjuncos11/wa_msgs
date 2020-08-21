from graphene_sqlalchemy import SQLAlchemyConnectionField
from src.graphql.schemas.posts import PostObject

class PostQuery():
  all_posts = SQLAlchemyConnectionField(PostObject)