import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from src.config.config import db
from src.models.users import User
from src.models.posts import Post
from src.graphql.schemas.users import UserObject

from src.graphql.schemas.posts import PostObject
from src.graphql.query.test import Test
from src.graphql.mutation.auth.register import Register
from src.graphql.mutation.auth.auth import Auth

# ------------------ Graphql Schemas ------------------
class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)
        email = graphene.String(required=True)

    post = graphene.Field(lambda: PostObject)

    def mutate(self, info, title, body, email):
        user = User.query.filter_by(email=email).first()
        post = Post(title=title, body=body)
        if user is not None:
            post.author = user
        db.session.add(post)
        db.session.commit()
        return CreatePost(post=post)


class Mutation(graphene.ObjectType):
    save_post = CreatePost.Field()
    register = Register.Field()
    auth = Auth.Field()



# class Mutation(graphene.ObjectType, PostQuery, Test):
#     node = graphene.relay.Node.Field()
    
#     def resolve_save_post(root, info):
#         save_post = CreatePost.Field()
#         return 'saved!'


# noinspection PyTypeChecker
# schema_mutation = graphene.Schema(mutation=Mutation)
