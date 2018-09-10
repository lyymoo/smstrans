from wsgiref.simple_server import make_server
import json

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    #res = '<h1>hello, wsgi(web server gateway interface)</h1><h2>%s</h2>' % (environ, )
    #return [res.encode('utf-8')]
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    if method == 'GET' and path == '/':
        return handle_home(environ, start_response)
    elif method == 'GET' and path == '/detail':
        return handle_detail(environ, start_response)
    else:
        return [b'test']

def handle_home(environ, start_response):
    res = '<h1>home page</h1>'
    return [res.encode('utf-8')]

def handle_detail(environ, start_response):
    res = '<h1>home detail</h1>'
    return [res.encode('utf-8')]

httpd = make_server('', 81, application)
print('Serving HTTP on port 81......')

#httpd.serve_forever()

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '<h1>HOME</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''
    <form action="/signin" method="post">
    <p><input name="username"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">Sign In</button></p>
    </form>
    '''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()