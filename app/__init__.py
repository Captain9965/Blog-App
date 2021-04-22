from flask import Flask # creates the application object as an instance of class Flask imported from the flask package
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager    #Flask login extension



app= Flask(__name__)    # the __name__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is used
app.config.from_object(Config)
db=SQLAlchemy(app)      # create database instance
migrate= Migrate(app, db)# database migration engine instance
login=LoginManager(app) #initialize login instance
login.login_view = 'login' #for flask_login to know the view that handles login
from app import routes, models, errors  # importing the routes module and models module that will define the database structure
                        # The bottom import is a workaround to circular imports, a common problem with Flask applications
