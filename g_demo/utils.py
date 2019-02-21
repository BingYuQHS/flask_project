from flask import g
# 在这个文件中写一些工具类的函数，例如用户的登录日志

def login_log():
    print('日志文件中：当前登录用户是：%s' % g.username)

def login_ip_log():
    print('日志文件中：当前登录用户是：%s' % g.ip)