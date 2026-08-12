from flask import Blueprint, render_template
from Controllers import controllers

home_pg = Blueprint('home', __name__,)

@home_pg.route('/')
def home():
    return render_template('index.html')

@home_pg.route('/buscar', methods=['POST'])
def buscar():
    return controllers.Buscar()
