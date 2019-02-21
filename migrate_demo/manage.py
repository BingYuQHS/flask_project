from flask_script import Manager
from  migrate_demo import app
from flask_migrate import Migrate,MigrateCommand
from exts import db
from models import Article


# 模型 --> 迁移文件 --> 表
manager = Manager(app)

# 第一步，使用migrate要先绑定app和db
migrate = Migrate(app,db)

# 把MigrateCommand命令添加到manager中,替代主app的db.create_all()
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()