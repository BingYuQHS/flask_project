from flask import Flask,render_template,request,redirect,url_for,session,g
import config
from exts import db
from models import User,Question,Answer
from decorators import login_required
from sqlalchemy import or_

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)



@app.route('/')
def index():
    context = {
        # all()是将表中的所有数据取出
        # order_by('create_time')是按照时间从小到大排序，
        # 在前面加上'-'就实现了大时间在前面的效果
        'questions':Question.query.order_by('-create_time').all()
    }
    return render_template('index.html', **context)


# 用户登录
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # 获取用户输入的登录信息
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        # 在数据库中查找
        user = User.query.filter(User.telephone == telephone).first()
        if user and user.check_password(password):
            # 设置cookie
            session['user_id'] = user.id
            # 想在31天内都不需要重新登录
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return '用户名或密码错误，请重新登录！'

# 用户注册
@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        # 获取注册表单中的输入信息
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        print(telephone,username,password1,password2)
        # 手机号码验证，如果被注册了，就不能再注册了
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return '该手机号已被注册，请更换号码！'
        else:
            # 验证密码与确认密码一致
            if password1 != password2:
                return '两次密码不一致，请确认密码！'
            else:
                # 将一个用户的信息存进数据库
                user = User(telephone=telephone,username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                # 如果注册成功，就跳转到登录页面进行登录
                return redirect(url_for('login'))

# 注销登录
@app.route('/logout/')
def logout():
    # session.pop('user_id')
    session.clear()
    # 注销后跳转到登录页面
    return redirect(url_for('login'))

# 发布问答
@app.route('/question/',methods=['GET','POST'])
@login_required
def question():
  if request.method == 'GET':
      return render_template('question.html')
  else:
      # 获取用户要发布的问答信息
      title = request.form.get('title')
      content = request.form.get('content')
      question = Question(title=title,content=content)

      # 优化代码1，将其写在before_request钩子函数中，并使用g对象
      # user_id = session.get('user_id')
      # user = User.query.filter(User.id == user_id).first()

      question.author = g.user
      db.session.add(question)
      db.session.commit()
      return redirect(url_for('index'))

# 问答详情
@app.route('/detail/<question_id>/')
def detail(question_id):
    question_model = Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html',question=question_model)

# 问答评论，注意一定要用户登录后才能填写评论，因此要加上登录限制装饰器
@app.route('/add_answer/',methods=['POST'])
@login_required
def add_answer():
    # 从前台表单中获取评论内容
    content = request.form.get('answer_content')
    question_id = request.form.get('question_id')

    # 根据前台数据，构造问答对象answer
    answer = Answer(content=content)

    # 优化代码1，将其写在before_request钩子函数中，并使用g对象
    # user_id = session.get('user_id')
    # user = User.query.filter(User.id == user_id).first()

    answer.author = g.user
    question = Question.query.filter(Question.id == question_id).first()
    answer.question = question

    # 将问答评论添加到数据库
    db.session.add(answer)
    db.session.commit()
    # 刷新问答详情页面
    return redirect(url_for('detail',question_id=question_id))


# 查找问答 ?xxx=xxx
@app.route('/search/')
def search():
    # 获取关键字，使用的传参方式是GET
    q = request.args.get('q')
    # 根据关键字查询满足条件的模型，关键字在title或content中
    # 或 or_需要导入
    # order_by排序
    # 知识点：与 两种情况都满足的查询：
    # Question.query.filter(Question.title.contains(q),Question.content.contains(q))
    questions = Question.query.filter(or_(Question.title.contains(q),
                                          Question.content.contains(q))).order_by('-create_time')
    return render_template('index.html',questions=questions)

@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            g.user = user

@app.context_processor
def my_context_processor():
    # # 判断用户是否登录
    # user_id = session.get('user_id')
    # if user_id:
    #     # 根据浏览器的cookie中的user_id查找到相应用户
    #     user = User.query.filter(User.id == user_id).first()
    #     if user:
    #         return {'user':user}
    # # 上下文钩子函数无论如何都返回一个字典，哪怕是空字典
    # return {}

    # 优化代码2 ：执行流程
    # my_before_request -->视图函数(可用) -->my_context_processor(可用g)
    # hasattr(g,'user')是判断g对象有user这个属性
    if hasattr(g,'user'):
        return {'user': g.user}
    return {}

if __name__ == '__main__':
    app.run()
