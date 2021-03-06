from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name="Modality Apps"):
    return "Hello there, from {}".format(name)

@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
def add(num1, num2):
    return render_template("add.html", num1=num1, num2=num2)

@app.route('/multiply/<int:num1>/<int:num2>')
@app.route('/multiply/<float:num1>/<float:num2>')
@app.route('/multiply/<float:num1>/<int:num2>')
@app.route('/multiply/<int:num1>/<float:num2>')
def multiply(num1, num2):
    return render_template("multiply.html", num1=num1, num2=num2)


app.run(debug=True)