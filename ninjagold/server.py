from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key= 'ThisisSecret'


@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def monies():
    

 
    return redirect('/')



app.run(debug=True) 