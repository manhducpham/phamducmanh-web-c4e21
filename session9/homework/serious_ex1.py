from flask import Flask, render_template, request
import mlab
from post import Post

app = Flask(__name__)
mlab.connect()

@app.route('/')
def homepage():
    return "<h1>This is homepage</h1><h2><a href = '/register'> Click here to enter the excercise</a></h1>"

@app.route('/register', methods = ['GET', 'POST'])
def new_id():
    if request.method == 'GET':
        return render_template('serious_ex1.html')
    if request.method == 'POST':
        form = request.form
        name = form['name']
        email = form['email']
        your_id = form['your_id']
        password = form['password']
        id_new = Post(name = name, email = email, your_id = your_id, password = password)
        id_new.save()
        return 'Your register has been recorded.'

if __name__ == "__main__":
    app.run(debug = True)