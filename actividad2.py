from flask import Flask,render_template
from flask import request

app = Flask(__name__)

@app.route("/operacionA2",methods = ["GET"])
def operacionA2():
    return render_template("operacionA2.html")

@app.route("/resultado2",methods = ["POST"])
def resultado2():
    n1 = request.form.get("txtNum1")
    n2 = request.form.get("txtNum2")
    rest = ""
    for tem in range(0,int(n2)):
        rest +=  str(n1) 
        if tem == int(n2)-1:
            rest +=  ""
        else:
            rest +=  " + "
    
    rest += " = "+ str(int(n1)*int(n2))
    return render_template("resultado2.html",res = rest)

if __name__ == "__main__":
    app.run(debug = True, port = 3000)