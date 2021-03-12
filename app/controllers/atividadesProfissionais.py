from flask import render_template
from app import app
from app.models.tables import AtividadeProfissional

@app.route('/atividades')
def atividades():
    lista = AtividadeProfissional.query.all()
    return render_template("listar_ativProfissional.html", lista=lista)
