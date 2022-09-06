from flask import Flask
from markupsafe import escape

app = Flask(__name__)

##se utiliza el decorador app.route para definir la ruta de acceso!
@app.route('/')
def index():
    return "Index Page"

@app.route('/hello')
def hello():
    return "Hello, World"

##Variable rules!

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {escape(post_id)}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'

##trailing slash
##@app.route('/plants/')
##esto produce error porque le impide al navegado indexar la pagina

