from flask import Flask
from exts import db
from models import Article
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

db.create_all()
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
