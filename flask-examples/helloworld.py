#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask import redirect
from flask import abort
app = Flask(__name__)

#route装饰器
@app.route('/')
def index():
    return '<h1>Hello</h1>'

@app.route('/user/<name>')
def user(name):
    if name == 'foo':
        abort(404)
    elif name == 'boo':
        #这里用http://www.baidu.com就能实现跳转，但是不加http就TM不行
        return redirect('http://www.baidu.com')
    return '<h1>Hello, %s</h1>' % name


from flask import request

@app.route('/agent/')
def a():
    user_agent = request.headers.get('User-Agent')
    return '<p>your brower is %s</p>' % user_agent



if __name__ == '__main__':
    app.run(debug = True)
