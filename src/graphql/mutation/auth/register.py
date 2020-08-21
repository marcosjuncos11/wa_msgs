import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from src.config.config import db
from src.models.users import User
from src.models.posts import Post
from src.graphql.schemas.users import UserObject

from src.graphql.schemas.posts import PostObject
from src.graphql.query.test import Test

from src.models.auth import Auth

# ------------------ Graphql Schemas ------------------


class Register(graphene.Mutation):
    class Arguments:        
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    token = graphene.String()

    def mutate(self, info, email, password):
        print('init register')
        print(email)
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return Register('User already exists. Please Log in.')
        try:
            user = User(
                email=email,
                password=password
            )            
            print('***************')
            # insert the user
            db.session.add(user)
            db.session.commit()
            # generate the auth token
            auth = Auth()
            auth_token = auth.encode_auth_token(user.id)
            print('auth_token')
            print(auth_token)
            return Register(auth_token.decode())
        except Exception as e:                
            return Register('Some error occurred. Please try again.')
        
