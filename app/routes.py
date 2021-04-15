from app import app

@app.route('/')
@app.route('/index')
def index():
    user={'username': 'Lenny'}  # mock object
    return '''
 <html>
    <head>
        <title> Homepage- Microblog</title>
    </head>
    <body>
        <h1> Welcome, ''' + user['username']+ '''!</h1>
    </body>

</html>'''
    




    
    
    
    

    

