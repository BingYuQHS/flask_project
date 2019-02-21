from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

# article表
# create table article{
#     id int primary key autoincrement,
#     title varchar(100) not null,
#     content text not null
# }
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
db.create_all()


@app.route('/')
def hello_world():
    # # 增加
    # article = Article(title = '文章主题',content = '文章内容')
    # db.session.add(article)
    # # 事务提交
    # db.session.commit()

    # 查询
    # select * from article where title = '文章主题';
    # result = Article.query.filter(Article.title == '文章主题').all()
    # article1 = result[0]
    # print(article1.title)
    # print(article1.content)

    # article1 = Article.query.filter(Article.title == '文章主题').first()
    # print('title:%s'% article1.title)
    # print('content:%s' % article1.content)

    # # 修改
    # # 1、把需要改的数据查询出来
    # article1 = Article.query.filter(Article.title == '文章主题').first()
    # # 2、修改数据的内容
    # article1.title = 'new title'
    # # 3、做事务的提交
    # db.session.commit()

    # 删除
    # 1、把需要删除的数据查找出来
    article1 = Article.query.filter(Article.content == '文章内容').first()
    # 2、把这条数据删除
    db.session.delete(article1)
    # 3、做事务的提交
    db.session.commit()

    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
