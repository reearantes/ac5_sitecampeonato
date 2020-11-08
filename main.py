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
    __tablename__="relacao_equipes"
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    equipe  = db.Column(db.String(50))
    def __init__(self,equipe):
        self.equipe = equipe


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
        if equipe:
            f = equipes(equipe)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("mensagem"))

@app.route("/equipes")
def equipes():
    return render_template("equipes.html")

app.run(debug=True)

