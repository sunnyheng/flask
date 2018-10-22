# -*- coding:utf-8 -*-

from flask_script import Manager

from flask import Flask, request, make_response
from flask import redirect, abort


app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookies!</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/test')
def test():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s </p>' %user_agent


@app.route('/sunny')
def sunny():
    return redirect('http://www.imooc.com')


# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' %name




@app.route('/user/<id>')
def get_user(id):
    test_user = {1:'sun', 2:'heng', 3:'zhong'}
    user = test_user.get(int(id))
    #print test_user[int(id)]
    if not user:
        abort(404)
    return '<h1>Hello, %s!</h1>' % user



if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()