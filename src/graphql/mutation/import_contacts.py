from flask import Flask
import graphene
from flask_graphql_auth import (
    AuthInfoField,
    mutation_header_jwt_required,
)
from graphene.types import generic

from src.containers.import_contacts import ImportContactsContainer

class ImportContactsMutation(graphene.Mutation):
    class Arguments(object):
        file_name = graphene.String()

    list = generic.GenericScalar()

    @classmethod
    @mutation_header_jwt_required
    def mutate(cls, _, info, file_name):
        container = ImportContactsContainer()
        # print('***** 2')
        service = container.importContactsService()
        # print('***** 3')
        params = dict(file_name= file_name)
        res = service.execute(params)
        # print(res)
        return ImportContactsMutation(res)