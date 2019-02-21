'''
    功能：解决循环引用问题
        由于系统采用了MVC模式，将主app文件（逻辑功能）和models文件（映射的数据库表）
        分离开来，在操作数据库时，主app文件会调用models文件，models文件也会调用主app文件
        就存在循环引用问题。
    作者：秦华山
    日期：2017.10.5
'''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()