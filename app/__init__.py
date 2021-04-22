from flask import Flask # creates the application object as an instance of class Flask imported from the flask package
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager    #Flask login extension
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os



app= Flask(__name__)    # the __name__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is used
app.config.from_object(Config)
db=SQLAlchemy(app)      # create database instance
migrate= Migrate(app, db)# database migration engine instance
login=LoginManager(app) #initialize login instance
login.login_view = 'login' #for flask_login to know the view that handles login
from app import routes, models, errors  # importing the routes module and models module that will define the database structure
                        # The bottom import is a workaround to circular imports, a common problem with Flask applications
if not app.debug:   #when the application is running without debug mode
    if app.config['MAIL_SERVER']:#also when the email server exists in the configuration.
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(         #creates a SMTPHandler instance
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)#only reports errors and not warnings
        app.logger.addHandler(mail_handler)#attaches it to the app.logger object from Flask.
# File logging
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)#limiting the size of the log file to 10KB, and I'm keeping the last ten log files as backup.
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))#timestamp, the logging level, the message and the source file and line number from where the log entry originated.
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')