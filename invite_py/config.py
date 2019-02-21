'''
    文件：配置文件
    功能：用于建立MySQL数据库连接、设置Debug模式方便程序调试
    作者：秦华山
    日期：2017.10.5
'''
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '7623lwqs'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_invite'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,
                                                                       HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = True