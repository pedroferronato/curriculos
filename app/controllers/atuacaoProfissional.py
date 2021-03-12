from flask import render_template
from app import app
from app.models.tables import AtuacaoProfissional

@app.route('/atuacoes')
def atuacoes():
    lista = AtuacaoProfissional.query.all()
    return render_template("listar_atuaProfissional.html", lista=lista)
