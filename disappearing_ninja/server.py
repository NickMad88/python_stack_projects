from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/ninja')
def ninja():
    return render_template("ninja.html")

@app.route('/ninja/orange')
def ninjaorange():
    return render_template("mikey.html")

@app.route('/ninja/purple')
def ninjapurple():
    return render_template("donny.html")

@app.route('/ninja/red')
def ninjared():
    return render_template("raph.html")

@app.route('/ninja/blue')
def ninjaoblue():
    return render_template("leo.html")




app.run(debug=True)