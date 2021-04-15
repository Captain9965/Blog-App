from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/', methods=['GET'])             # Home route
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

@app.route('/login', methods=['GET','POST'])    # Login route
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))         # display message to the user
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)




    
    
    
    

    

