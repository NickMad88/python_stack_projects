from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key= 'ThisisSecret'


@app.route('/')
def index():
    if 'app.num' not in session:
        session['app.num'] = random.randrange(0,101)
   

    # if session['guess'] == session['app.num']:

    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guesses():
    
    guess = int(request.form['guess'])
    print session['app.num']
    print guess
    print guess > session['app.num']

    if guess > session['app.num']:
        session['app.answer'] = "TOO HIGH!!"

    elif guess < session['app.num']:
        session['app.answer'] = "TOO LOW!!"

    elif guess == session['app.num']:
        session['app.answer'] = "NICE JOB!"


 
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.pop('app.num')
    session.pop('app.answer')
    return redirect('/')


app.run(debug=True) 











# run our server

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
# @app.route('/users', methods=['POST'])
# def create_user():
#    print "Got Post Info"
#    # we'll talk about the following two lines after we learn a little more
#    # about forms
#    session['name'] = request.form['name']
#    session['email'] = request.form['email']
#    # redirects back to the '/' route
#    return redirect('/show')

# @app.route('/show')
# def show_user():
#   return render_template('user.html')
