from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    lista = ['Programador front-end', 'Programador back-end', 'Devops']
    return render_template('index.html', lista=lista)
