# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 11:24:03 2019

@author: ale
"""

import datetime
from utils import read_data, data_to_json, datetime_to_str, get_form_content, get_table_content, filter_data
from flask import Flask, Markup, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
    data = read_data()
    filter_option = request.args.get("filter")
    allowed_cities = None
    if filter_option and filter_option == "on":
        allowed_cities = request.args.getlist("filter_value")
        data = filter_data(data, allowed_cities)
    table_content = get_table_content(data)
    form_content = get_form_content(allowed_cities)
    charts_json = data_to_json(data)
    now_str = datetime_to_str(datetime.datetime.now())
    return render_template("index.html", 
        table_content=Markup(table_content), 
        form_content=Markup(form_content), 
        charts_json=charts_json,
        now_str=now_str)

@app.route("/authors")
def authors():
    return render_template("authors.html")
