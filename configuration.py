import os 
from access import username, password, localhost, database #probably unnecessary, edit your secret values according to your likes

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIF = False #SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future

#use formatting to access and add tables to database, may be hosted on cloud
'''  if however, you're using a different sql besides postgres, just modify the values
     for example: SQLALCHEMY_DATABASE_URI = "sqlite:///app.db if you are using SQlite
'''
SQLALCHEMY_DATABASE_URI= f"postgresql://{username}:{password}@{localhost}/{database}"
