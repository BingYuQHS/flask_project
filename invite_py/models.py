'''
******************************************************
    功能：数据库表的模型，每一个类对应数据库中的一张表
        还能指定模型与模型间的关联关系
******************************************************
'''
from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     telephone = db.Column(db.String(11),nullable=False)
#     username = db.Column(db.String(50),nullable=False)
#     password = db.Column(db.String(100),nullable=False)
#
#     def __init__(self,*args,**kwargs):
#         telephone = kwargs.get('telephone')
#         username = kwargs.get('username')
#         password = kwargs.get('password')
#
#         self.telephone = telephone
#         self.username = username
#         self.password = generate_password_hash(password)
#
#     def check_password(self,raw_password):
#         result = check_password_hash(self.password,raw_password)
#         return result
#

'''
 模型名：招标申报表
 表的字段：项目编号(int)、项目名称(String)、项目内容（Text）、申请时间(DateTime)。
'''
class DeclareForm(db.Model):
    __tablename__ = 'declareform'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Projectname = db.Column(db.String(100),nullable=False)
    Projectconten = db.Column(db.Text,nullable=False)
    # now()获取的是服务器第一次运行的时间
    # now获取的是当前系统的时间
    apply_time = db.Column(db.DateTime, default=datetime.now)

'''
 模型名：邀标书表
 表的字段：编号(int)、项目编号(int)、开标时间(DateTime)、
           开标地点(String)、招标内容(Text)、招标须知(Text)、备注(Text)。
'''
class Invite(db.Model):
    __tablename__ = 'invite'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    projectId = db.Column(db.Integer,db.ForeignKey('declareform.id'))
    openTime = db.Column(db.DateTime,nullable=False)
    openPosition = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    notice = db.Column(db.Text,nullable=False)
    remarks = db.Column(db.Text,nullable=True)
