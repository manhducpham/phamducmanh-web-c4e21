from flask import Flask, render_template, request
import mlab
from post import Post

app = Flask(__name__)
mlab.connect()

p = {
    'title': 'C4E21',
    'content': 'Today is a bad day',
    'author': 'Quan',
    'date': '2018/09/02',
},

ps = [
    {
        'title': 'C4E21',
        'content': 'Today is a bad day',
        'author': 'Quan',
        'date': '2018/09/02',
    },
    {
        'title': 'C4E22',
        'content': 'Today is a good day',
        'author': 'Manh',
        'date': '2018/09/03',
    },
    {
        'title': 'C4E23',
        'content': 'Today is a awesome day',
        'author': 'Nam',
        'date': '2018/09/04',
    },
]



@app.route('/post')
def one_dict():
    return render_template('dict.html', post = p)

@app.route('/posts')
def multi_dict():
    return render_template('dicts.html', posts = ps)

@app.route('/new-post', methods = ['GET', 'POST'])
def new_post():
    if request.method == 'GET':
        return render_template('new_post.html')
    elif request.method == 'POST':
        # 1. Get form & extract data
        form = request.form
        t = form['title']
        a= form['author']
        c = form['content']
        #Cách khi có database
        new_post = Post(title = t, author = a, content = c, likes = 0)
        new_post.save()
        # Cách đầu tiên khi chưa có database
        # new_p = {
        #     'title': t,
        #     'author': a,
        #     'content': c,
        # }
        # # print(title, author, content)
        # # 2. Add new post
        # ps.append(new_p)
        return 'OK'

if __name__ == "__main__":
    app.run(debug = True)