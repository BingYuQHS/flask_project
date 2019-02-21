from flask import Flask,render_template,request,session,redirect,url_for,g
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def index():
    # return render_template('index.html',username='zhiliao')
    return render_template('index.html')

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
            # 下一次请求时知道当前用户是谁,设置一个session
            session['username'] = 'zhiliao'
            return '登录成功！'
        else:
            return '你的用户名或密码错误！'

@app.route('/edit/')
def deit():
    # # # 要在登录的请况下执行编辑信息的函数
    # # if session.get('username'):
    # #     return '修改信息成功！'
    # # else:
    # #     # 如果没有登录，就跳转到登录页面进行登录
    # #     return redirect(url_for('login'))
    #
    # if g.username:
    #     return '修改信息成功！'
    # else:
    #     return redirect(url_for('login'))

    # return render_template('edit.html',username='zhiliao')
    return render_template('edit.html')

# before_request：是在之前执行的
# 在执行视图函数之前执行
# 这个函数只是一个装饰器，就是把需要设置为钩子函数的代码放在视图函数执行前执行
# 在每一个视图函数执行前都先执行钩子函数
@app.before_request
def my_brfore_request():
    if session.get('username'):
        g.username = session.get('username')

@app.context_processor
def my_context_processor():
    # username = session.get('username')
    # if username:
    #     return {'username': username}
    return {'username':'ziliao'}

if __name__ == '__main__':
    app.run(debug=True)
