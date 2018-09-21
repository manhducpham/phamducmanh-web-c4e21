import mlab
from post import Post

# 1. Connect
mlab.connect()

# 2. Create Data
# p = Post(title = 'C4E21', author = 'Manh', content = 'Thử tí cho vui', likes = 310)
# print(p.title)
# print(p.author)
# print(p.content)
# print(p.likes)

# # 3. Write data
# p.save()
def test_load_data():
    # 2 load all documents
    all_posts = Post.objects()

    # 3. Print all documents:
    for post in all_posts:
        print(post.title)
        print(post.author)
        print(post.content)
        print(post.likes)
        print('----------------')

def test_one_data(post_id):
    post = Post.objects().with_id(post_id)
    if post is None:
        print('Not Found')
    else:
        print(post.title)
        print(post.author)
        print(post.content)
        print(post.likes)
# test_one_data('5b9cd081d7bca010183befeb')
def delete_one_post(post_id):
    #1. retrive doc
    post = Post.objects().with_id(post_id)
    #2. delete doc
    if post is None:
        print('not found')
    else:
        post.delete()

# delete_one_post('5b9cd081d7bca010183befeb')
def update_one_post(post_id, new_title):
    post = Post.objects().with_id(post_id)
    # post[key] = new
    # update
    # slug
    post.update(set__title = new_title)

update_one_post('5b9cd24bd7bca02d0c25f764', 'New title, hihi')