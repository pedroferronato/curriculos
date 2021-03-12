from flask import render_template
from app import app
from app.models.tables import FormacaoComplementar

@app.route('/complementar')
def complementar():
    lista = FormacaoComplementar.query.all()
    return render_template("listar_formComplementar.html", lista=lista)
