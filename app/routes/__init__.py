from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/enunciado')
def enunciado():
    return render_template('enunciado.html')