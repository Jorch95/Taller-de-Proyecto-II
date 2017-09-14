from flask import Flask
from flask import request
from flask import render_template
from readfile import devolverValores
import random
aplicacion = Flask(__name__)

@aplicacion.route('/')
def index():
    arreglo = devolverValores()
    return render_template('response.html', dataP=arreglo[0], dataT=arreglo[1], dataH=arreglo[2], dataV=arreglo[3])

aplicacion.run(host='0.0.0.0', port=1111)
