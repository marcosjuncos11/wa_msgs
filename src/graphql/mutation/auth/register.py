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

    ok = graphene.String()

    def mutate(self, info, email, password):        
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
            return Register('User created')
        except Exception as e:                
            return Register('Some error occurred. Please try again.')
        
