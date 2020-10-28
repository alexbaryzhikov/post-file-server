from flask import Flask
from flask import request, redirect, abort, url_for
import os

from flask.json import jsonify

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


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return redirect(url_for('login'))


@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['file']
    f.save('{}/{}'.format(os.getcwd(), f.filename))
    return 'Received file "{}", size={}'.format(f.filename, request.content_length)


@app.route('/error')
def error():
    abort(401)


@app.route('/me')
def me_api():
    return {
        "username": "alex",
        "status": "online"
    }


@app.route('/people')
def people_api():
    return jsonify(["alice", "bob", "chuck"])
