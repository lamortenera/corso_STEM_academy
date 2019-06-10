# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 11:24:03 2019

@author: ale
"""

from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/authors")
def authors():
    return render_template("authors.html")