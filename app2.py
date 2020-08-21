from flask import Flask
import sqlalchemy as db

engine = db.create_engine('mysql://devuser:devuser@host.docker.internal/whatsapp_api')

connection = engine.connect()
metadata = db.MetaData()
census = db.Table('users', metadata, autoload=True, autoload_with=engine)
print(census.columns.keys())
