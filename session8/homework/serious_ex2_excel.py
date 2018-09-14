from flask import Flask, render_template, redirect
import pyexcel

app = Flask(__name__)

users_list = pyexcel.get_records(file_name = 'class_list.xlsx')
name_list = []
for dic in users_list:
    name = dic['Name']
    name_list.append(name)

@app.route('/')
def homepage():
    return "<h1> Homepage </h1><h2><a href = '/users'> Exercise </a></h2>"

@app.route('/users/<name>')
def user(name):
    name = name.lower()
    name = name.capitalize()
    if name in name_list:
        pos = name_list.index(name)
        dic = users_list[pos]
        # [fullname, email, phone, dob, fb, uni, ref] = dic.values() # loi too many value to unpack
        fullname = dic['Fullname'].title()
        email = dic['Email']
        phone = dic['Phone']
        dob = dic['DOB']
        fb = dic['Link Facebook']
        uni = dic['University/Company']
        ref = dic['Ref']
        return render_template('serious_ex2.html',
        fullname = fullname,
        email = email,
        phone = phone,
        dob = dob,
        fb = fb,
        uni = uni,
        ref = ref)
    else:
        return "User not found"

@app.route('/users')
def users():
    return render_template('serious_ex2_users.html', name_list = name_list)

if __name__ == "__main__":
    app.run(debug = True)