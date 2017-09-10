from flask import Flask 
from flask import request
from flask import render_template
import random

#TODO definir inicio

app = Flask(__name__)

filename="datos.txt"

@app.route('/')
def index():
    # presion = random.randrange(101)
    # temperatura = random.randrange(0,30)
    # humedad = random.randrange(60,95) #Si estamos en La Plata.
    # velocidadViento = random.randrange(60,120)
    return render_template('response.html',dataP=presion,dataT=temperatura,dataH=humedad,dataV=velocidadViento)
    
if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=1111)