from flask import Flask,render_template
from flask import request

app = Flask(__name__)



@app.route("/",methods = ["GET"])
def index():
    return render_template("cineOpera.html")

@app.route("/res",methods = ["POST"])
def result():
    nBoletos = request.form.get("canBol")
    pagoTarjetaC = request.form.get("sel")
    cantidadC = request.form.get("canComp")

    if int(nBoletos) <= 2:
        rest = sinDescuento()
    elif int(nBoletos) > 2 and int(nBoletos) <= 5:
        rest = descuentoDiez()
    elif int(nBoletos) > 5:
        rest = descuentoQuince()
    
    if pagoTarjetaC == "si":
        rest = rest - (rest*.10)
    else:
        rest = rest

    if int(nBoletos) > 7 and int(cantidadC) == 1:
        return render_template ("resultadoCinepolis.html",res = "SOLO 7 BOLETAS POR COMPRADOR")
    else:
         return render_template ("resultadoCinepolis.html",res = rest)

def sinDescuento():
    nBoletos = request.form.get("canBol")
    return int(nBoletos)*12

def descuentoDiez():
    nBoletos = request.form.get("canBol")
    return sinDescuento() - (sinDescuento()*.10)

def descuentoQuince():
    nBoletos = request.form.get("canBol")
    return sinDescuento() - (sinDescuento()*.15)

if __name__ == "__main__":
    app.run(debug = True, port = 3000)