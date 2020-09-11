from flask import Flask
import graphene
from flask_graphql_auth import (
    AuthInfoField,
    mutation_header_jwt_required,
)

# class ResponseField(graphene.ObjectType):
#     message = graphene.String()

class ImportContactsMutation(graphene.Mutation):
    class Arguments(object):
        pass

    message = graphene.Field(graphene.Boolean)

    @classmethod
    @mutation_header_jwt_required
    def mutate(cls, _, info):
        return ImportContactsMutation(
            message=True
        )