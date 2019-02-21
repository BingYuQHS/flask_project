from flask import Flask
from exts import db
import config
from models import Article

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

# #将当前app置于app栈顶
# with app.app_context():
#     db.create_all()

# 新建Article模型，采用models分开的方式
# flask_scripts的方式
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
