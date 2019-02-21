# 该文件不是主文件运行，是被引用在manage.py中运行
from flask_script import Manager

DBManager = Manager()

@DBManager.command
def init():
    print('数据库初始化完成！')

@DBManager.command
def migrate():
    print('数据表迁移成功！')


