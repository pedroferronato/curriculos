from flask import render_template
from app import app
from app.models.tables import Instituicao

@app.route('/instituicoes')
def instituicao():
    lista = Instituicao.query.all()
    return render_template("listar_instituicoes.html", lista=lista)
