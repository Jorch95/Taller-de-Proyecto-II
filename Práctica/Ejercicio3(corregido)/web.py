# -- coding: utf-8 --
from flask import Flask
from flask import request
from flask import render_template
from readfile import devolverValores
from muestra import Muestra
aplicacion = Flask(__name__)

def calcularPromedio():
    suma = Muestra(0, 0, 0, 0)
    if index.lleno:
        tam = 9
    else:
        tam = len(index.muestras)
    for i in range(0,tam):
        suma += index.muestras[i]
    suma.presion /= len(index.muestras)
    suma.temperatura /= len(index.muestras)
    suma.humedad /= len(index.muestras)
    suma.velocidad /= len(index.muestras)
    return suma

frecuencia = 5 # por defecto para que se pueda ingresar bien los valores

@aplicacion.route('/')
def index():
    pos = index.pos
    muestra = devolverValores()
    if index.lleno:
        index.muestras.pop(pos)
    index.muestras.insert(pos, muestra)
    if (index.pos == 9):
        index.pos = 0
        index.lleno = True
    else:
        index.pos += 1
    promedio = calcularPromedio()
    return render_template('response.html', ultima=index.muestras[pos], prom=promedio, frec=frecuencia)

@aplicacion.route('/', methods = ['POST'])
def action_form():

    if request.method == 'POST':
        data = request.form
        global frecuencia
        frecuencia = data["frecuencia"]
        return index()


index.lleno = False
index.pos = 0
index.muestras = []
aplicacion.run(host='0.0.0.0', port=8765)
