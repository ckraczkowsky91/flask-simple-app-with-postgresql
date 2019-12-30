from flask import Flask
from flask_sqlalchemy import SQLAlchemy

simpleApp = Flask(__name__)

simpleApp.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/sample-flask-app-with-postgresql'
db = SQLAlchemy(simpleApp)

from . import routes
