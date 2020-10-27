from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def show_home():
    return "Welcome to home page!"

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<user_name>')
def greet_user(user_name):
    return 'Hello, {}!'.format(user_name)

@app.route('/post/<int:id>')
def show_post(id):
    return 'Post ID {}'.format(id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Logging in..."
    else :
        return "Login form"
