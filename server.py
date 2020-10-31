from flask import Flask, request, abort, make_response
from typing import Text
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import os

UPLOAD_DIR = os.environ.get('UPLOAD_DIR') or os.getcwd()
ALLOWED_EXTENSIONS = ['log', 'zip', 'gz']

app = Flask(__name__)
app.config['UPLOAD_DIR'] = UPLOAD_DIR


def is_allowed_file(filename: str):
    return any([filename.endswith('.' + x) for x in ALLOWED_EXTENSIONS])


def bad_request(error: str):
    return make_response("ERROR: " + error, 400)


@app.route('/api/upload_log', methods=['POST'])
def upload_log():
    if 'file' not in request.files:
        abort(bad_request('No file part'))

    file: FileStorage = request.files['file']

    if file.filename == '':
        abort(bad_request('No selected file'))

    if not is_allowed_file(file.filename):
        abort(bad_request('File type is not allowed. Must be one of ' +
                          str(ALLOWED_EXTENSIONS)))

    filename: Text = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_DIR'], filename))
    return 'OK'
