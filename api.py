from main import *
from templates import *
from flask_marshmallow import Marshmallow
from flask import Flask, request, render_template
from app.controller import *
from mostramapa import MostraMapas

app =Flask(__name__)
ma = Marshmallow(app)

@app.route('/')
def apresenta_home():
    render_template("index.html")
    
@app.route('/login')    
def recebe_login():
    render_template("login.html")
    email = request.form.get("email")
    senha = request.form.get("senha")
    
    ValidacaoUsuario.valida_user(email, senha)

@app.route('/maps')
def apresenta_maps():
    MostraMapas.ismostramaps
    return render_template("mostramapa.html")

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)