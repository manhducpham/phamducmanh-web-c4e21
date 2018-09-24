from post import Post
from flask import Flask, render_template, redirect, url_for, request
import mlab

app = Flask(__name__)
mlab.connect()

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/posts')
def posts():
    posts = Post.objects()
    return render_template('posts.html', posts = posts)

@app.route('/post/<post_id>')
def post(post_id):
    post = Post.objects().with_id(post_id)
    return render_template('post.html', post = post)

@app.route('/new-post', methods = ['GET', 'POST'])
def new_post():
    if request.method == 'GET':
        return render_template('new_post.html')
    if request.method == 'POST':
        form = request.form
        title = form['title']
        author = form['author']
        content = form['content']
        new_post = Post(title = title, author = author, content = content)
        new_post.save()
        return render_template('done.html')

@app.route('/delete/<post_id>')
def delete(post_id):
    post = Post.objects().with_id(post_id)
    post.delete()
    return redirect(url_for('posts'))

@app.route('/update/<post_id>', methods = ['GET', 'POST'])
def update(post_id):
    post = Post.objects().with_id(post_id)
    if request.method == 'GET':
        return render_template('update.html', post = post)
    if request.method == 'POST':
        form = request.form
        title = form['title']
        author = form['author']
        content = form['content']
        post.update(set__title = title, set__author = author, set__content = content)
        #inc__likes
        # push__
        p.reload()
        return render_template('done.html')

if __name__ == '__main__':
    app.run(debug=True)