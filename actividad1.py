from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/actividad1",methods = ["GET","POST"])
def operas():
    if request.method == "POST":
        op = request.form.get("sel")
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        

        if op == "suma":
            return "<h2>La suma es: {}".format(str(int(num1)+int(num2)))
        elif op == "resta":
            return "<h2>La resta es: {}".format(str(int(num1)-int(num2)))
        elif op == "multi":
            return "<h2>La multiplicación es: {}".format(str(int(num1)*int(num2)))
        elif op == "divi":
            return "<h2>La división es: {}".format(str(int(num1)/int(num2)))
    else:
        return '''
        
        <form action = "/actividad1" method = "POST">

        <input type="radio" id="suma" name="sel" value="suma">
        <label for="suma">SUMA </label><br>
        
        <input type="radio" id="resta" name="sel" value="resta">
        <label for="rest">RESTA </label><br>

        <input type="radio" id="multi" name="sel" value="multi">
        <label for="multi">MULTIPLICACION </label><br>
        
        <input type="radio" id="divi" name="sel" value="divi">
        <label for="divi">DIVISION </label><br><br>

        <label>N1: </label>
        <input type="text" name = "num1" /><br><br>
        <label>N2: </label>
        <input type="text" name = "num2" /><br><br>
        <input type="submit" value = "calcular"/>
        </form>


        '''


if __name__ == "__main__":
    app.run(debug = True, port = 3000)