from app import app
from flask import render_template, url_for, redirect

@app.route('/')
@app.route('/index')
@app.route('/index/<name>', methods=['GET'])
def index(article1='MY HOBBIES', article2 ='MY GOAL'):
    return render_template('index.html', article1=article1, article2=article2, title='HOME')
