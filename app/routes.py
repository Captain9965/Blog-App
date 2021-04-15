from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user={'username': 'Lenny'}  # mock object
    posts = [
        {
            'author': {'username': 'Kelvin'},
            'body': 'All have a blessed day!'
        },
        {
            'author': {'username': 'Sue'},
            'body': 'Bike riding is super awesome!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)





    
    
    
    

    

