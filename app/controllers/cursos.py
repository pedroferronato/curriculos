from flask import render_template
from app import app
from app.models.tables import Curso

@app.route('/cursos')
def cursos():
    lista = Curso.query.all()
    return render_template("listar_cursos.html", lista=lista)
