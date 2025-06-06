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
    mutation_header_jwt_required,
)


class MessageField(graphene.ObjectType):
    message = graphene.String()

class ProtectedUnion(graphene.Union):
    class Meta:
        types = (MessageField, AuthInfoField)

    @classmethod
    def resolve_type(cls, instance, info):
        return type(instance)    

class ProtectedMutation(graphene.Mutation):
    class Arguments(object):
        pass

    message = graphene.Field(ProtectedUnion)

    @classmethod
    @mutation_header_jwt_required
    def mutate(cls, _, info):
        return ProtectedMutation(
            message=MessageField(message="Protected mutation works")
        )