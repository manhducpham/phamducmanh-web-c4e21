from flask import Flask, render_template, redirect
import pyexcel

app = Flask(__name__)

user_dict = {
	'huy': {
		'name' : 'Nguyen Quang Huy',
		'age' : 29
    },
    'tuananh': {
		'name' : 'Huynh Tuan Anh',
		'age' : 22
    },
}
name_list = []
for key in user_dict.keys():
    name_list.append(key)
print(name_list)

@app.route('/')
def homepage():
    return "<h1> Homepage </h1><h2><a href = '/users'> Exercise </a></h2>"

@app.route('/users/<name>')
def user(name):
    name = name.lower()
    if name in name_list:
        dic = user_dict[name]
        [name, age] = dic.values()
        return render_template('serious_ex2_nesteddict.html',
        name = name,
        age = age)
    else:
        return "User not found"

@app.route('/users')
def users():
    return render_template('serious_ex2_users.html', name_list = name_list)

if __name__ == "__main__":
    app.run(debug = True)