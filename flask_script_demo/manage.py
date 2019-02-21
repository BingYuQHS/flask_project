from flask_script import Manager
from flask_script_demo import app
from db_script import DBManager

manager = Manager(app)

#和数据库相关的操作都放在一起，开辟一个文件db_script.py

@manager.command
def runserver():
    print('服务器跑起来了！！！')
manager.add_command('db',DBManager)

if __name__ == '__main__':
    manager.run()