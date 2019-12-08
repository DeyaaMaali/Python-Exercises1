# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 09:34:03 2019

@author: OJO3
"""

from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return 'This is the Index page'
@app.route('/hello')
def hello():
    return "Hello World!"
@app.route('/members')
def member():
    return "Members page"


@app.route('/index/<int:marks>')
def Question2(marks):
    return render_template('index.html',marks=marks)


@app.route('/index')
def Question3():
    return render_template('index2.html')
if __name__=='__main__':
    app.run()