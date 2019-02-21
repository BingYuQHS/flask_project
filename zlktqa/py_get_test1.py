# coding:utf8
# 在python3.3后urllib2已经不能再用，只能用urllib.request来代替
import urllib,urllib.request, urllib.parse

url = 'http://127.0.0.1:5000/login/'
# 定义请求数据，并对数据进行赋值
data = {}
data['question_id'] = '17777777777'
data['password'] = '222222'
# 对请求数据进行编码
# data = urllib.urlencode(data)
data = urllib.parse.urlencode(data)
# 将数据和url进行连接
request = url+'?'+data
# 打开请求，获取对象
requestResponse = urllib.request.urlopen(request)
# 读取服务器端返回的数据
ResponseStr = requestResponse.read()
# 打印数据
ResponseStr = ResponseStr.decode('unicode_escape')
print(ResponseStr)