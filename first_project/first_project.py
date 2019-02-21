
#从flask这个框架中导入Flask这个类
from flask import Flask

#初始化一个Flask对象
#Flask()
#需要传递一个参数
#1、方便Flask框架寻找资源
#2、方便Flask插件比如Flask-Sqlalchemy出现错误的时候，好去寻找错误出现的位置
app = Flask(__name__)

#@app.route是一个装饰器
#@开头，并且在函数的上面，说明是装饰器
#这个装饰器的作用是做一个url与视图函数的映射
#127.0.0.1:5000/   --> 去请求hello_world这个函数，然后将结果返回给浏览器
@app.route('/')
def hello_world():
    return '我是第一个flask程序!'

#如果当前这个文件是作为入口程序运行，那么就执行app.run()
if __name__ == '__main__':
    #app.run()是启动一个应用服务器来接收用户的请求，一直处于监听状态
    #while True:
    #   Listen()
    app.run()
