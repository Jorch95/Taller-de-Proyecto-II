from flask import Flask 
from flask import request
from flask import render_template
import random
from readfile import devolverValores

#TODO definir inicio

app = Flask(__name__)

filename="datos.txt"
#arch = open(filename, 'r')
@app.route('/')
def index():
    # presion = random.randrange(101)
    # temperatura = random.randrange(0,30)
    # humedad = random.randrange(60,95) #Si estamos en La Plata.
    # velocidadViento = random.randrange(60,120)
    arreglo = []
    arreglo = devolverValores()
    return render_template('response.html',dataT=arreglo[0],dataH=arreglo[1],dataP=arreglo[2], dataV=arreglo[3])
    
if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=1111)