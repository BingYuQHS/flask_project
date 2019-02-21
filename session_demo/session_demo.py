from flask import Flask,session
import os
from datetime import timedelta
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_FILETIME'] = timedelta(days=7)
# app.config['SECRET_KEY'] = 'ABCDE'
# 添加数据到session中
# 操作session时与操作字典相似
# 设置SECRET_KRY的值

@app.route('/')
def hello_world():
    session['username'] = 'zhiliao'
    # 设置过期时间
    session.permanent = True
    return 'Hello World!'

# 获取session
@app.route('/get/')
def get():
    # session('username') 如果不存在就抛出异常
    # session.get('username')如果不存在就返回None
    print(session.get('username'))
    return 'get success!'

# 删除session
@app.route('/delete/')
def delete():
    print(session.get('username'))
    session.pop('username')
    print(session.get('username'))
    return 'success!'

# 清除所有session数据
@app.route('/clear/')
def clear():
    print(session.get('username'))
    # 删除session中的所有数据
    session.clear()
    print(session.get('username'))
    return 'clear success!'


if __name__ == '__main__':
    app.run(debug=True)
