#配置文件

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '7623lwqs'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_python'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,
                                                                       HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = True