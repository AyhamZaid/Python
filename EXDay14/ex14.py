# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:55:58 2019

@author: Ayham
"""

# Exercise 1 
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "This is Index Page!"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/members")
def members():
    return "Members Page"

# Exercise 2 
@app.route('/mark/<int:score>')
def scoree(score):
   return render_template('index.html', marks = score )


# Exercise 3
@app.route('/ex3')
def score():
   return render_template('index2.html') 

if __name__ == '__main__':
   app.run()