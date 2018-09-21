from flask import Flask, render_template, request, redirect, url_for
import mlab
from post import Post

app = Flask(__name__)
mlab.connect()




@app.route('/posts/<post_id>')
def one_dict(post_id):
    # all_post = Post.objects()
    # for post in all_post:
    #     if post[id] = post_id:
    #         p = post
    p = Post.objects().with_id(post_id)
    return render_template('dict.html', post = p)

@app.route('/posts')
def multi_dict():
    all_post = Post.objects()
    return render_template('posts.html', posts = all_post)

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
        # return redirect('/posts')
        return redirect(url_for('multi_dict'))
@app.route('/delete/<post_id>')
def del_post(post_id):
    post = Post.objects().with_id(post_id)
    post.delete()
    return redirect('/posts')

@app.route('/update/<post_id>', methods = ['GET', 'POST'])
def update_post(post_id):
    post = Post.objects().with_id(post_id)
    if request.method == 'GET':
        return render_template('update.html', post = post)
    if request.method == 'POST':
        form = request.form
        t = form['title']
        a= form['author']
        c = form['content']
        post.update(set__title = t, set__author = a, set__content = c)
        return redirect('/posts')
if __name__ == "__main__":
    app.run(debug = True)