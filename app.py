# Import dependencies
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

# Path to presidents' images
PEOPLE_FOLDER = os.path.join('static','pres_photos')

# Flask setup
app = Flask(__name__)

# Instantiate db object from SQLAlchemy class
db=SQLAlchemy()

app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cdcbpwkylbzrrr:9a5ce1442c169cfe6c3ad8fc09df281ff9f4e732ea6735b6b49229398850c084@ec2-54-158-122-162.compute-1.amazonaws.com:5432/d19bqudloefpjs'
db.init_app(app)

# Model definition
class Tvi(db.Model):
    __tablename__ = 'total_votos_integrado'
    id= db.Column(db.Integer,name='id', primary_key=True)
    ESTADO = db.Column(db.String(100),name='ESTADO')
    LATITUD = db.Column(db.Float,name='LATITUD')
    LONGITUD = db.Column(db.Float,name='LONGITUD')
    ANO = db.Column(db.Integer,name='ANO')
    voto = db.Column(db.Integer,name='voto')
    GANADOR = db.Column(db.String(80),name='GANADOR')

# Flask routes
@app.route('/')
def ƒ():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'],'2018elections.jpeg')
    return render_template('index.html', user_image = full_filename)

# Election results per year
@app.route('/api/votos/<ano>')
def votos(ano):
    # Query results for selected year
    resultados = Tvi.query.filter(Tvi.ANO==ano).all()
    # Create a dictionary from resultados
    resultados=[{'longitud':d.LONGITUD, 'latitud':d.LATITUD, 'estado':d.ESTADO, 'ganador':d.GANADOR} for d in resultados]
    # Generate JSON using Flask's jsonify() function
    return jsonify(resultados)

@app.route('/about')
def aboutpage():
    return render_template('about.html')

# ELection results for year 2012
@app.route('/2012elections')
def twelveelections():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'],'2012elections.jpeg')
    return render_template('2012elections.html', user_image = full_filename)

# ELection results for year 2006
@app.route('/2006elections')
def sixelections():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'],'2006elections.jpeg')
    return render_template('2006elections.html', user_image = full_filename)

# ELection results for year 2000
@app.route('/2000elections')
def twothousandselections():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'],'2000elections.jpeg')
    return render_template('2000elections.html', user_image = full_filename)

# ELection results for year 1994
@app.route('/1994elections')
def ninetyfourelections():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'],'1994elections.png')
    return render_template('1994elections.html', user_image = full_filename)

if __name__ == '__main__':
    app.debug = True
    app.run()
