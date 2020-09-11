from flask import Flask
import graphene
from flask_graphql_auth import (
    AuthInfoField,
    GraphQLAuth,
    get_jwt_identity,
    get_raw_jwt,
    create_access_token,
    create_refresh_token,
    query_jwt_required,
    mutation_jwt_refresh_token_required,
    mutation_jwt_required,
)
from src.models.users import User

class Auth(graphene.Mutation):
    class Arguments(object):
        username = graphene.String()
        password = graphene.String()

    access_token = graphene.String()
    refresh_token = graphene.String()

    @classmethod
    def mutate(cls, _, info, username, password):
        user = User.query.filter_by(email=username, password=password).first()
        if not user:
          return Auth(access_token=None)
        return Auth(
            access_token=create_access_token(username),
            refresh_token=create_refresh_token(username),
        )