from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def homepage():
    return "<h1> Homepage </h1><h2><a href = '/about-me'> Exercise </a></h2>"

@app.route('/about-me')
def about_me():
    return '<h1>Name: Manh Duc Pham</h1><h2>Work: freelancer</h2><h2>School: Banking Academy</h2><h2>Hobbies: Gym, Swim, Read</h2><h2>Facebook: https://www.facebook.com/manh.pd031094'
    

@app.route('/school')
def school_redirect():
    return redirect('http://techkids.vn', code = 302)

if __name__ == "__main__":
    app.run(debug = True)