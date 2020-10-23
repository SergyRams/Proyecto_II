from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class total_votos_integrado(db.Model):
    __tablename__ = 'total_votos_integrado'
    ESTADO = db.Column(db.varchar(100))
    ANO = db.Column(db.Integer)
    voto = db.Column(db.Integer)
    comentarios = db.Column(db.varchar(800))

    def __init__(self, ESTADO, ANO, voto, comentarios):
        self.ESTADO = ESTADO
        self.ANO = ANO
        self.voto = voto
        self.comentarios = comentarios


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        ESTADO = request.form['ESTADO']
        ANO = request.form['ANO']
        voto = request.form['voto']
        comentarios = request.form['comentarios']
        # print(customer, dealer, rating, comments)
        if ESTADO == '' or ANO == '':
            return render_template('index.html', message='Ingrese los campos requeridos')
        if db.session.query(total_votos_integrado).filter(total_votos_integrado.ESTADO == ESTADO).count() == 0:
            data = total_votos_integrado(ESTADO, ANO, voto, comentarios)
            db.session.add(data)
            db.session.commit()
            return render_template('success.html')
        return render_template('index.html', message=('Se ha registrado su voto')


if __name__ == '__main__':
    app.debug = True
    app.run()
