from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'martina'


@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/porcesar/result', methods=['POST'])         
def procesar_datos():
    print(request.form)
    session["datos"] = request.form
    return render_template("/results.html")

@app.route("/result")         
def resultados():
    return render_template("/results.html")




if __name__=="__main__":   
    app.run(debug=True)