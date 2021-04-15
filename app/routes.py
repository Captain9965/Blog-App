from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user={'username': 'Lenny'}  # mock object
    return render_template('index.html', title='Home', user=user)   #invokes the Jinja2 template engine that comes bundled with the Flask framework. Jinja2 substitutes {{ ... }} blocks with the corresponding values, given by the arguments provided in the render_template() call.





    
    
    
    

    

