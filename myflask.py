#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from flup.server.fcgi import WSGIServer
from flask import Flask, render_template, redirect, abort, url_for


app = Flask(__name__)

#def app(environ, start_response):
#    start_response('200 OK', [('Content-Type', 'text/html')])
#    return ['Hello World!\n', str(environ)]

@app.route('/')
def hello():
    return redirect(url_for('hello_user'))

@app.route('/test/')
def test():
    return os.getcwd()


@app.route('/hello/')
@app.route('/hello/<username>')
def hello_user(username = None):
    return render_template('hello.html', username = username)


if __name__ == '__main__':
    WSGIServer(app).run()
