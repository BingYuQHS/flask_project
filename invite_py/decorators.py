'''
***********************************************************************
    文件说明：此文件专门用来写装饰器
    功能：是一个自定义的登录限制的装饰器，有些功能登录成功后才能操作，
          在这些功能前加上该装饰器起一个限制作用
    作者：秦华山
    日期：2017.10.5
************************************************************************
'''
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