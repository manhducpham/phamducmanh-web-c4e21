import mlab
from post import Post

# 1. Connect
mlab.connect()

# 2. Create Data
p = Post(title = 'C4E21', author = 'Manh', content = 'Thử tí cho vui', likes = 310)
print(p.title)
print(p.author)
print(p.content)
print(p.likes)

# 4. Write data
p.save()