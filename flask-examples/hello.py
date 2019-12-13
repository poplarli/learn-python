#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    comments = [1,2,3,4,5];
    return render_template('user.html', name = name, comments = comments)

@app.route('/derive/<name>')
def derive(name):
    return render_template('derive.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

if __name__ == '__main__':
    app.run(debug = True)
