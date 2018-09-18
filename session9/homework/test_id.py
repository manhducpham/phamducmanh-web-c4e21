import mlab
from post import Post

# 1. Connect
mlab.connect()

# 2. Create Data
p = Post(name = "Manh", email = 'manh@gmail.com', your_id = "manhpro", password = "CodeTheChange")

# 4. Write data
p.save()