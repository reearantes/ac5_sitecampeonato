from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:mudar@2021@localhost/equipes'
db = SQLAlchemy(app)

class equipes(db.Model):
    __tablename__="equipes"
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    equipe = db.Column(db.String(50))
    telefone = db.Column(db.String(20))
    cidade = db.Column(db.String(50))
    tecnico = db.Column(db.String(50))
    jogador = db.Column(db.String(50))
    def __init__(self,equipe,telefone,cidade,tecnico,jogador):
        self.equipe = equipe
        self.telefone = telefone
        self.cidade = cidade
        self.tecnico = tecnico
        self.jogador = jogador


db.create_all()

@app.route("/testeinicial")
def testeinicial():
    return "Funcionou!!"

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/mensagem")
def mensagem():
    return render_template("mensagem.html")

@app.route("/cadastrar",methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        equipe = (request.form.get("equipe"))
        telefone = (request.form.get("telefone"))
        cidade = (request.form.get("cidade"))
        tecnico = (request.form.get("tecnico"))
        jogador = (request.form.get("jogador"))
        if equipe:
            f = equipes(equipe,telefone,cidade,tecnico,jogador)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("mensagem"))

@app.route("/times")

def times():
    return render_template("times.html")

app.run(debug=True)

