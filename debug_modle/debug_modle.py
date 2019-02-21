from flask import Flask
import config
app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    return 'debug模式！非常棒'


if __name__ == '__main__':
    #debug模式 app.run(debug=True)
    #1、可以直接看到错误信息
    #2、如果修改了python文件,程序可以自动加载，直接刷新页面即可
    app.run()
