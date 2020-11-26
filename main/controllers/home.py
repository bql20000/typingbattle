from flask import render_template

from main.app import app


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')
