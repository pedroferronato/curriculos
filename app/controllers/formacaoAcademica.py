from flask import render_template
from app import app
from app.models.tables import FormacaoAcademica

@app.route('/academicas')
def formAcademica():
    lista = FormacaoAcademica.query.all()
    return render_template("listar_formAcademica.html", lista=lista)
