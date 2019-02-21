from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    avatar = 'http://p2.so.qhmsg.com/bdr/_240_/t016695577d4315b9b7.jpg'
    comments = [
        {
            'user':'张三',
            'content':'这个网站不错哦!'
        },
        {
            'user':'李四',
            'content':'这里的课程讲的好棒！'
        }
    ]
    return render_template('index.html',avatar=avatar,comments = comments)


if __name__ == '__main__':
    app.run(debug=True)
