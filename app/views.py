from app import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'Olá, me chamo fulaninho e sou estudante :)'