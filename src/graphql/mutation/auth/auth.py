import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from src.config.config import db
from src.models.users import User
from src.models.posts import Post
from src.graphql.schemas.users import UserObject

from src.graphql.schemas.posts import PostObject
from src.graphql.query.test import Test

from src.models.auth import Auth as AuthModel

# ------------------ Graphql Schemas ------------------


class Auth(graphene.Mutation):
    class Arguments:        
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    token = graphene.String()

    def mutate(self, info, email, password):
        try:
            # fetch the user data
            user = User.query.filter_by(
                email=email, password=password
              ).first()
            auth = AuthModel()
            auth_token = auth.encode_auth_token(user.id)                
            return Auth(auth_token.decode())
        except Exception as e:
            print(e)            
            return Auth('Failed, try again')