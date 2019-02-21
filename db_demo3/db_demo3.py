from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

# 用户表
# create table users(
# id int primary key autoincrement,
# username varcher(100) not null
# )
# 文章表
# create table article(
# id int primary key autoincrement,
# title varcher(100) not null,
# content text not null,
# author_id int,
# foreign key 'author_id' references 'users.id'
# )
class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    author = db.relationship('Users',backref=db.backref('articles'))
db.create_all()

@app.route('/')
def index():
    # 想要添加一篇文章，因为文章必须依赖用户存在，所有先要添加一个user
    # user = Users(username='ziliao')
    # db.session.add(user)
    # db.session.commit()

    # article = Article(title='aaa',content='bbb',author_id=1)
    # db.session.add(article)
    # db.session.commit()

    # 法1、找标题为'aaa'文章的作者
    # article = Article.query.filter(Article.title == 'aaa').first()
    # author_id = article.author_id
    # user = Users.query.filter(Users.id == author_id).first()
    # print('username:%s' % user.username)

    # 法2、找标题为'aaa'文章的作者 以后article.author  author.articles



    # 创建一篇文章，利用 db.relationship
    # article = Article(title='aaa',content='bbb')
    # article.author = Users.query.filter(Users.id == 1).first()
    # db.session.add(article)
    # db.session.commit()

    # 找标题为'aaa'文章的作者
    # article = Article.query.filter(Article.title == 'aaa').first()
    # print('username: %s' % article.author.username)

    # 找出ziliao这个用户写过的所有文章
    # # 先添加一篇文章
    # # article = Article(title='111',content='222',author_id=1)
    # # db.session.add(article)
    # # db.session.commit()
    # 1、找到ziliao这个用户
    user = Users.query.filter(Users.username == 'ziliao').first()
    result = user.articles
    for article in result:
        print('-'*10)
        print(article.title)

    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
