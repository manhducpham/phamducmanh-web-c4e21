from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def homepage():
    return "<h1> Homepage </h1>"

@app.route('/bmi/<int:x>/<int:y>')
def bmi_cal(x, y):
    y = y /  100
    bmi = round(x / (y**2), 2)
    if bmi < 16:
        result = 'Severely underweight'
    elif bmi < 18.5:
        result = ' Underweight'
    elif bmi < 25:
        result = 'Normal'
    elif bmi < 30:
        result = 'Overweight'
    else:
        result = 'Obese'
    return render_template('serious_ex1_render.html', 
    weight = x, 
    height = y, 
    bmi = bmi, 
    conclusion = result)

if __name__ == "__main__":
    app.run(debug = True)