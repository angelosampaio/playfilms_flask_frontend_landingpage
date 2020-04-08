from app import app
from flask import send_from_directory,render_template

import os
@app.route("/")
def index():
    return "Hello world!"


@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    #uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=app.root_path, filename=filename)


@app.route('/login')
def login():
    return render_template("login.html")