from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
# 文章表
# create table article(
# id int primary key autoincrement,
# title varcher(100) not null,
# content text not null,
# )
# 标签表
# create table tag(
# id int primary key autoincrement,
# name varcher(50) not null
# )
# 文章_标签表（文章：标签关系是多对多）
# create table article_tag(
# article_id int,
# tag_id int,
# primary key('article_id','tag_id'),
# foreign key 'article_id' referances ('article.id')
# foreign key 'tag_id' referances ('tag.id')
# )

article_tag = db.Table('article_tag',
        db.Column('article_id',db.Integer,db.ForeignKey('article.id'),primary_key=True),
        db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'),primary_key=True)
)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)

    # 添加一个关联属性（tags）
    tags = db.relationship('Tag',secondary=article_tag,backref=db.backref('articles'))

class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100),nullable=False)

db.create_all()

@app.route('/')
def index():
    # 1、添加数据
    # # 实例化对象
    # article1 = Article(title='aaa')
    # article2 = Article(title='bbb')
    # tag1 = Tag(name='111')
    # tag2 = Tag(name='222')
    #
    # # article1和article2分别引用两个标签
    # article1.tags.append(tag1)
    # article1.tags.append(tag2)
    # article2.tags.append(tag1)
    # article2.tags.append(tag2)
    #
    # # 添加数据
    # db.session.add(article1)
    # db.session.add(article2)
    # db.session.add(tag1)
    # db.session.add(tag2)
    #
    # db.session.commit()

    # 2、访问数据
    # 查询一篇文章（aaa）有哪些标签
    article1 = Article.query.filter(Article.title == 'aaa').first()
    tags = article1.tags
    for tag in tags:
        print(tag.name)
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
