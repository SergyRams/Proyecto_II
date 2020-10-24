from flask import Flask, render_template, jsonify,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db=SQLAlchemy()

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cdcbpwkylbzrrr:9a5ce1442c169cfe6c3ad8fc09df281ff9f4e732ea6735b6b49229398850c084@ec2-54-158-122-162.compute-1.amazonaws.com:5432/d19bqudloefpjs'
db.init_app(app)
#Host
#ec2-54-158-122-162.compute-1.amazonaws.com
#Database
#d19bqudloefpjs
#User
#cdcbpwkylbzrrr
#Port
#5432
#Password
#9a5ce1442c169cfe6c3ad8fc09df281ff9f4e732ea6735b6b49229398850c084
#URI
#postgres://cdcbpwkylbzrrr:9a5ce1442c169cfe6c3ad8fc09df281ff9f4e732ea6735b6b49229398850c084@ec2-54-158-122-162.compute-1.amazonaws.com:5432/d19bqudloefpjs
#Heroku CLI
#heroku pg:psql postgresql-vertical-12726 --app dbcmxelections


#else:
#    app.debug = False
#    app.config['SQLALCHEMY_DATABASE_URI'] = ''
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)


class Tvi(db.Model):
    __tablename__ = 'total_votos_integrado'
    id= db.Column(db.Integer,name='id', primary_key=True)
    ESTADO = db.Column(db.String(100),name='ESTADO')
    LATITUD = db.Column(db.Float,name='LATITUD')
    LONGITUD = db.Column(db.Float,name='LONGITUD')
    ANO = db.Column(db.Integer,name='ANO')
    voto = db.Column(db.Integer,name='voto')
    GANADOR = db.Column(db.String(80),name='GANADOR')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/api/votos/<ano>')
def votos(ano):
    resultados = Tvi.query.filter(Tvi.ANO==ano).all()
    resultados=[{'longitud':d.LONGITUD, 'latitud':d.LATITUD, 'estado':d.ESTADO, 'ganador':d.GANADOR} for d in resultados]
    return jsonify(resultados)

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
        return render_template('index.html', message=('Se ha registrado su voto'))


if __name__ == '__main__':
    app.debug = True
    app.run()
