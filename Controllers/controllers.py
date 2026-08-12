from flask import render_template, request
from Services import services

def Buscar():
    tag = request.form.get('tag')
    tag = tag.replace("#", "").upper()
    dados = services.Pesquisar(tag)
    return render_template('resultados.html', dados=dados)