# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 11:24:03 2019

@author: ale
"""

from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "Pagina principale in costruzione"

@app.route("/authors")
def authors():
    return "Pagina autori in costruzione"