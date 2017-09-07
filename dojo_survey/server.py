from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print request.form
    name = request.form['name']
    location = request.form['location']
    comment = request.form['comment']

    return render_template('results.html', name=name, location=location, comment=comment)
    



app.run(debug=True)