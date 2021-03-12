from flask import render_template
from app.models.tables import Usuario
from app import app

@app.route('/usuarios')
def home():
    lista = Usuario.query.all()
    return render_template('index.html', lista=lista)

