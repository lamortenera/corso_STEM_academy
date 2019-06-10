# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 11:24:03 2019

@author: ale
"""

import datetime
from utils import read_data, data_to_chart, datetime_to_str
from flask import Flask, Markup, render_template

def get_table_content(data):
    content = ""
    row_pattern = "<tr><td>{}</td><td>{}</td><td>{:.2f}</td></tr>"
    for row in data:
        content += row_pattern.format(row["datetime"], row["city"], row["temperature"])
    return content

app = Flask(__name__)
@app.route("/")
def index():
    data = read_data()
    table_content = get_table_content(data)
    data_to_chart(data)
    now_str = datetime_to_str(datetime.datetime.now())
    return render_template("index.html", 
        table_content=Markup(table_content), now_str=now_str)

@app.route("/authors")
def authors():
    return render_template("authors.html")