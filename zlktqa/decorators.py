
# 此文件专门用来写装饰器
from flask import redirect,session,url_for
from functools import wraps

# 自定义一个登录限制的装饰器
def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper