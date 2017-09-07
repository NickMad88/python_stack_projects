from flask import Flask, render_template  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.
@app.route('/') 
def welcome():
   return render_template('index.html')                        # The "@" symbol designates a "decorator" which attaches the
@app.route('/about')  
def about():
    return render_template('about.html')
@app.route('/projects')                                      # following function to the '/' route. This means that

def projects():
    return render_template('Projects.html')                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following "hello_world" function.
app.run(debug=True)

