from flask import Flask,g,render_template,request
from utils import login_log
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print('username:%s' % username)
        print('password:%s'% password)
        if username == 'zhiliao'and password == '111111':
            # 满足这个条件，就默认这个用户登录成功

            # # 此处调用不同函数要传许多不同的参数
            # login_log(username)

            # 可以利用g对象，将要传的参数绑定在g对象中，然后在utils中导入g，调用函数时就不用传参数了
            g.username = username
            g.ip = 'xxxxx'

            login_log()

            return '登录成功！'
            pass
        else:
            return '你的用户名或密码错误！'

if __name__ == '__main__':
    app.run(debug=True)
