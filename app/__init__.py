from flask import Flask # creates the application object as an instance of class Flask imported from the flask package
app= Flask(__name__)    # the __name__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is used
from app import routes  # importing the routes module
                        # The bottom import is a workaround to circular imports, a common problem with Flask applications
