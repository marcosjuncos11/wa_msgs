import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from src.models.users import User


class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)
