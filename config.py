import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db') #  location of the application's database 
    SQLALCHEMY_TRACK_MODIFICATIONS = False      



       # database URL from the DATABASE_URL environment variable or
        #database named app.db located in the main directory of the application,
        # which is stored in the basedir variable.
