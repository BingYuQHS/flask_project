from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/')
def search():
    # 打印参数字典
    print(request.args)
    print('用户提交的查询关键字是：%s' % request.args.get('q'))
    return 'search'

# 默认的视图函数只能采用get请求
# 如果使用post请求，就要写明
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print('username:%s' % username)
        print('password:%s'% password)
        return 'post requst'

if __name__ == '__main__':
    app.run(debug=True)
