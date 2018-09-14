# 1. Create a flask app
from flask import Flask, render_template

app = Flask(__name__) # name là cách để cho python biết đang ở đâu

# 2. Create router
@app.route('/') #định nghĩa một đường dẫn
def homepage(): # nối đường dẫn này với hàm nào
    ps = [
        'Hôm nay tôi buồn',
        'Hôm nay tôi rất buồn',
        'Hôm nay tôi quá buồn'
    ]
    return render_template('homepage.html', 
    tittle = 'Thứ ngày tháng',
    posts = ps)

@app.route('/manh')
def manh_page():
    return "Hello Manh"

@app.route('/hello/<name>') #<> để cho người dùng tự đặt tên, mapping 2 chiều
def hello(name):
    return 'hello ' + name
# bài tập: viết đường dẫn /add/ + 2 số bất kì /5/7 tính tổng 2 số

# @app.route('/add/<x>/<y>')
# def addxy(x, y):
    # x1 = int(x) # cách thông thường
    # y1 = int(y)
    # axy = str(x1 + y1)
    # return axy

@app.route('/add/<int:x>/<int:y>')
def addxy(x, y):
    return str(x + y)

@app.route('/h1tag')
def h1tag():
    return '<h1>Heading 1 - Bigggg</h1><p> Hôm nay tôi buồn </p>' #nhúng thẳng thẻ vào return, số thẻ trong html rất nhiều, tách html sang 1 file riêng
# tạo file html (template)
# 3. Run app
print('Running app')
if __name__ == "__main__": #code trên máy, bỏ đi không sao, deploy thì sẽ deploy trên nhiều máy, có nhiều luồng chạy, nếu không để thì sẽ tạo ra nhiều server, tách dữ liệu thành nhiều server
# dùng để check xem dùng trực tiếp file app không hay là dùng gián tiếp, nếu dùng gián tiếp sẽ tạo ra nhiều server    
    app.run(debug = True) #listening to serve
