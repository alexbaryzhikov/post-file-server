from flask import Flask
from flask import request
import os

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


def is_valid_login(login, password):
    return login == 'alex' and password == '123'


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if is_valid_login(request.form['username'],
                          request.form['password']):
            return 'Logging in as {}...'.format(request.form['username'])
        else:
            return 'Login error!'
    else:
        return 'Please, provide credentials'


@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['file']
    f.save('{}/{}'.format(os.getcwd(), f.filename))
    return 'Received file "{}"'.format(f.filename)
