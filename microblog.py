from app import app, db
from app.models import User, Post


@app.shell_context_processor #decorator registers the function as a shell context function
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
# ngrok support for testing:

def start_ngrok():
    from pyngrok import ngrok

    url = ngrok.connect(5000).public_url
    print(' * Tunnel URL:', url)
if app.config['START_NGROK']:
    start_ngrok()