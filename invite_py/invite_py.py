
'''
    文件说明：该文件是主app文件，系统的逻辑功能都写在该文件里
'''
from flask import Flask,render_template,request,redirect,url_for
import config
from exts import db
from models import DeclareForm,Invite
import time,datetime

# app的初始化
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

'''
    功能：编制邀标书首页显示
    作者：秦华山
    日期：2017.10.5
'''
@app.route('/')
def index():
    return render_template('index.html')

# 时间控件测试
@app.route('/dateTest/')
def dateTest():
    return render_template('dateTest.html')

'''
    功能：将编辑好的邀标书存入数据库，以便后期审核、查看
    作者：秦华山
    日期：2017.10.5
'''
@app.route('/commit/',methods=['POST'])
def commit():
    print('进入了commit!')
    # 第一步：从前台获取表单中的邀标书编辑信息
    id = int(request.form.get('id'))
    project_id = int(request.form.get('project_id'))

    # # 时间字符串
    # timestr = request.form.get('opentime')
    # # 将其转换为时间数组
    # timeArray = time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
    # # 转换为时间戳:
    # timeStamp = int(time.mktime(timeArray))
    # # 字符串转换成data
    # timeData = time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
    # print('时间字符串是：%s'%timestr)
    # print('时间数组是:',timeArray)
    # print('时间戳是：%d'% timeStamp)
    # print('日期是：' , timeData)
    # opentime = timestr

    opentime = request.form.get('starttime')
    openposition = request.form.get('openposition')
    content = request.form.get('content')
    notice = request.form.get('notice')
    remarks = request.form.get('remarks')

    # 第二步：验证邀标书编号是否存在，若邀标书已存在，这不能添加，给出相应提示
    invite = Invite.query.filter(Invite.id == id).first()
    if invite:
        return '该邀标书已存在！'
    else:
        # 第三步：验证项目编号是否存在，若不存在就不能为该项目制定邀标书
        project = DeclareForm.query.filter(DeclareForm.id == project_id).first()
        if project:
            # 第四步：根据前台数据，构造邀标书对象，并将该邀标书的信息存进数据库
            invite2 = Invite(projectId=project_id, openTime=opentime, openPosition=openposition,
                            content=content,notice=notice,remarks=remarks)
            db.session.add(invite2)
            db.session.commit()
            # 第五步：添加邀标书成功，就刷新首页页面
            return redirect(url_for('index'))
        else:
            return '项目编号不存在！'

'''
***************************************************************
    功能：这是整个系统程序功能实现的入口，
          在此处可以指定服务器运行的URL，可以定义端口号。
***************************************************************
'''
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
