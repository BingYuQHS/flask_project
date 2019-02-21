'''
**********************************************************
    文件说明：该文件写的是命令行执行需要的脚本
    功能：创建数据库迁移厂库，可以同步更新数据库的表结构，
       而不影响数据库表中已存在的数据。
    作者：秦华山
    日期：2017.10.5
*********************************************************
'''
from flask_script import Manager
from invite_py import app
from flask_migrate import Migrate,MigrateCommand
from exts import db
from models import DeclareForm,Invite

'''
主要逻辑：
    模型 --> 迁移文件 --> 表
    创建迁移仓库 --> 创建迁移脚本 --> 更新数据库
'''
# 第一次迁移实际上相当于调用db.create_all()，但在后续迁移中，upgrade命令对表实施更新操作但不影响表中的内容。
manager = Manager(app)

# 第一步，使用migrate要先绑定app和db
migrate = Migrate(app,db)

# 把MigrateCommand命令添加到manager中,替代主app的db.create_all()
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
