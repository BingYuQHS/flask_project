from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    class Person(object):
        def __init__(self,name,gender,age):
            self.name = name
            self.gender = gender
            self.age = age

    p = Person('qhs','女',20)
    contex = {
        'username':'qhs',
        'gender':'女',
        'age':20,
        'person':p,
        'websites':{
            'baidu':'www.baidu.com',
            'google':'www.google.com'
        }
    }

    return render_template('index.html',**contex)


if __name__ == '__main__':
    app.run()
