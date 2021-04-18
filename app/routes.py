from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse 
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User

@app.route('/', methods=['GET'])             # Home route
@app.route('/index')
@login_required
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
    return render_template('index.html', title='Home Page', posts=posts)

@app.route('/login', methods=['GET','POST'])    # Login route
def login():
    if current_user.is_authenticated:   #For user that is already logged in
        return redirect(url_for('index'))
    form=LoginForm()
    if form.validate_on_submit():       # runs all field validators and teturns true
        user = User.query.filter_by(username=form.username.data).first()    #will return the user object if it exists, or None if it does not.
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')        #return the user to the endpoint they tried to access
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
    
    
    
    

    

